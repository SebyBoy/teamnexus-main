from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Department, Team, TeamMember, Dependency


class DepartmentViewTests(TestCase):
    """Test cases for the Department pages."""

    def setUp(self):
        """Set up test data before each test."""
        # Create a test user
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass1234!'
        )
        # Create test departments
        self.dept1 = Department.objects.create(
            name='Cloud Engineering',
            specialisation='Cloud infrastructure'
        )
        self.dept2 = Department.objects.create(
            name='Mobile Engineering',
            specialisation='Mobile apps'
        )
        # Create test teams
        self.team1 = Team.objects.create(
            name='Platform Squad',
            mission='Build cloud infrastructure',
            responsibilities='Cloud deployments',
            department=self.dept1
        )
        self.team2 = Team.objects.create(
            name='DevOps Team',
            mission='Enable continuous delivery',
            responsibilities='CI/CD pipelines',
            department=self.dept1
        )
        # Create dependency
        self.dependency = Dependency.objects.create(
            upstream_team=self.team1,
            downstream_team=self.team2
        )

    def test_department_list_redirects_if_not_logged_in(self):
        """Unauthenticated users should be redirected to login."""
        response = self.client.get(reverse('organisation:department_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_department_list_loads_when_logged_in(self):
        """Authenticated users should see the department list."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(reverse('organisation:department_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Engineering')
        self.assertContains(response, 'Mobile Engineering')

    def test_department_search_works(self):
        """Search should filter departments by name."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(
            reverse('organisation:department_list'), {'q': 'Cloud'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Engineering')
        self.assertNotContains(response, 'Mobile Engineering')

    def test_department_search_no_results(self):
        """Search with no matches should return empty results."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(
            reverse('organisation:department_list'), {'q': 'Nonexistent'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Cloud Engineering')

    def test_department_detail_loads(self):
        """Department detail page should show teams."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(
            reverse('organisation:department_detail', args=[self.dept1.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Engineering')
        self.assertContains(response, 'Platform Squad')

    def test_department_detail_invalid_id(self):
        """Invalid department ID should return 404."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(
            reverse('organisation:department_detail', args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_organisation_chart_loads(self):
        """Organisation chart should show all departments and dependencies."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(reverse('organisation:organisation_chart'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Engineering')
        self.assertContains(response, 'Platform Squad')

    def test_organisation_chart_shows_dependencies(self):
        """Organisation chart should show team dependencies."""
        self.client.login(username='testuser', password='TestPass1234!')
        response = self.client.get(reverse('organisation:organisation_chart'))
        self.assertContains(response, 'Platform Squad')
        self.assertContains(response, 'DevOps Team')


class AuthTests(TestCase):
    """Test cases for login and register."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass1234!'
        )

    def test_login_page_loads(self):
        """Login page should load successfully."""
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        """Valid login should redirect to departments."""
        response = self.client.post(reverse('core:login'), {
            'username': 'testuser',
            'password': 'TestPass1234!'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_with_invalid_credentials(self):
        """Invalid login should stay on login page."""
        response = self.client.post(reverse('core:login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_register_page_loads(self):
        """Register page should load successfully."""
        response = self.client.get(reverse('core:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_new_user(self):
        """Valid registration should create a new user."""
        response = self.client.post(reverse('core:register'), {
            'username': 'newuser',
            'password1': 'NewPass1234!',
            'password2': 'NewPass1234!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())