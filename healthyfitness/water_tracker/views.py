from django.shortcuts import render, redirect

from water_tracker.forms import WaterForm


def AddWater(request):

    if request.method == 'POST':
        form = WaterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_water')
    else:
        form = WaterForm

    return render(request, 'water_tracker/add_water.html', {'form': form,})


def WaterTracker(request):
    return render(request, 'water_tracker/water_tracker.html')
