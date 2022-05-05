from django.shortcuts import render


def AddWater(request):
    return render(request, 'water_tracker/add_water.html')


def WaterTracker(request):
    return render(request, 'water_tracker/water_tracker.html')
