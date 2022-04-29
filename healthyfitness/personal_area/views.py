from django.shortcuts import render


def PersonalArea(request):
    return render(request, 'personal_area/personal_area.html')
