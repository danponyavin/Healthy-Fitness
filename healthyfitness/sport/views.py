from django.shortcuts import render


def AddSport(request):
    return render(request, 'sport/add_sport.html')


def SportDiary(request):
    return render(request, 'sport/sport_diary.html')
