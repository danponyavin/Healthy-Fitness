from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render

from calculator.models import Profile
from water_tracker.models import Water_tracker


def AddWater(request):
    glasses = '0 стаканов'
    user_id = Profile.objects.get(user=request.user)
    if request.POST.get('add_water_inp'):
        add_water_inp = request.POST.get('add_water_inp')
        if int(add_water_inp) >= 0:
            if Water_tracker.objects.filter(id_users=user_id, day_create=date.today()):
                user_water = Water_tracker.objects.filter(id_users=user_id, day_create=date.today())
                current_amount = user_water[0]
                current_amount.number_of_glasses = int(add_water_inp)
                current_amount.save()
            else:
                user_water = Water_tracker(id_users=user_id, number_of_glasses=int(add_water_inp))
                user_water.save()
            return HttpResponseRedirect('add_water')
    if Water_tracker.objects.filter(id_users=user_id, day_create=date.today()):
        info = Water_tracker.objects.filter(id_users=user_id, day_create=date.today())
        glasses = print_amount_of_glasses(info[0])
    return render(request, 'water_tracker/add_water.html', {'glasses': glasses})


def WaterTracker(request):
    return render(request, 'water_tracker/water_tracker.html')


def print_amount_of_glasses(info):
    if int(info.number_of_glasses) % 10 == 0:
        return f'{int(info.number_of_glasses)} стаканов'
    if int(info.number_of_glasses) in (11, 12, 13, 14, 15, 16, 17, 18, 19):
        return f'{int(info.number_of_glasses)} стаканов'
    if int(info.number_of_glasses) % 10 in (2, 3, 4):
        return f'{int(info.number_of_glasses)} стакана'
    if int(info.number_of_glasses) % 10 in (5, 6, 7, 8, 9):
        return f'{int(info.number_of_glasses)} стаканов'
    if int(info.number_of_glasses) % 10 == 1:
        return f'{int(info.number_of_glasses)} стакан'
