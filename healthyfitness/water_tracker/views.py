from django.http import HttpResponseRedirect
from django.shortcuts import render

from calculator.models import Profile
from water_tracker.models import Water_tracker


def AddWater(request):
    if request.POST.get('add_water_inp'):
        add_water_inp = request.POST.get('add_water_inp')
        if int(add_water_inp) > 0:
            user_id = Profile.objects.get(user=request.user)
            user_water = Water_tracker(id_users=user_id, number_of_glasses=int(add_water_inp))
            user_water.save()
            return HttpResponseRedirect('water_tracker')
    return render(request, 'water_tracker/add_water.html')


def WaterTracker(request):
    return render(request, 'water_tracker/water_tracker.html')
