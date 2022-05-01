from django.shortcuts import render, redirect

from calculator.models import Profile


def PersonalArea(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all().filter(user=request.user)
        return render(request, 'personal_area/personal_area.html', {'profile': profile})
    else:
        return redirect('login')
