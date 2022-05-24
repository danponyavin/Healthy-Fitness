from django.shortcuts import render


def AddWeight(request):
    return render(request, 'weight/add_weight.html')

def WeightTracker(request):
    return render(request, 'weight/weight_tracker.html')
