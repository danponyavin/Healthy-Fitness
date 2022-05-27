from django.shortcuts import render, redirect


def AddSport(request):
    if request.user.is_authenticated:
        return render(request, 'sport/add_sport.html')
    else:
        return redirect('login')


def SportDiary(request):
    if request.user.is_authenticated:
        return render(request, 'sport/sport_diary.html')
    else:
        return redirect('login')
