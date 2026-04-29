from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Meeting
from .forms import MeetingForm


def schedule_page(request):
    # Show only upcoming meetings
    meetings = Meeting.objects.filter(
        meeting_date__gte=timezone.now().date()
    ).order_by('meeting_date', 'meeting_time')

    # Optional filter by selected date
    filter_date = request.GET.get('date')

    if filter_date:
        meetings = meetings.filter(meeting_date=filter_date)

    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            meeting = form.save(commit=False)

            # Temporary host until login is fully connected
            meeting.host = User.objects.first()

            meeting.save()
            return redirect('schedule_page')

    else:
        form = MeetingForm()

    return render(request, 'schedule/schedule_page.html', {
        'meetings': meetings,
        'form': form,
        'filter_date': filter_date,
    })