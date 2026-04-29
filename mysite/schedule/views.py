from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .forms import MeetingForm


# Create a meeting
@login_required
def create_meeting(request):

    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.organiser = request.user   # VERY IMPORTANT
            meeting.save()
            return redirect('meeting_list')

    else:
        form = MeetingForm()

    return render(request, 'schedule/create_meeting.html', {'form': form})


# View all meetings (upcoming schedule)
@login_required
def meeting_list(request):
    meetings = Meeting.objects.all().order_by('meeting_date', 'meeting_time')

    return render(request, 'schedule/meeting_list.html', {
        'meetings': meetings
    })