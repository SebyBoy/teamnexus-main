from django.shortcuts import render

def base(request):
    return render(request, "teams/base.html")