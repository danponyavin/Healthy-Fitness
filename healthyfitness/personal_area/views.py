from django.shortcuts import render

from calculator.models import Profile


def PersonalArea(request):
    profile = Profile.objects.all().filter(user=request.user)
    return render(request, 'personal_area/personal_area.html', {'profile': profile})
