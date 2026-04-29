from django.shortcuts import render


def inbox(request):
    return render(request, "messaging/inbox.html")


def sent_messages(request):
    return render(request, "messaging/sent.html")


def drafts(request):
    return render(request, "messaging/drafts.html")


def send_message(request):
    return render(request, "messaging/send.html")


def message_detail(request, id):
    return render(request, "messaging/detail.html", {"id": id})


def vote_view(request):
    return render(request, "messaging/vote.html")


def summary_view(request):
    return render(request, "messaging/summary.html")