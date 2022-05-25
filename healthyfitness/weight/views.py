from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from calculator.models import Profile
from weight.models import Weight_trecker


def AddWeight(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.filter(user=request.user)[0]
        user_id = Profile.objects.get(user=request.user)
        current_weight = current_user.weight
        if request.POST.get('weight_inp'):
            new_weight = request.POST.get('weight_inp')
            if Weight_trecker.objects.filter(id_users=user_id, day_create=date.today()):
                user_weight = Weight_trecker.objects.filter(id_users=user_id, day_create=date.today())[0]
                user_weight.weight = new_weight
                user_weight.save()
            else:
                user_weight = Weight_trecker(id_users=user_id, weight=new_weight)
                user_weight.save()
            Profile.objects.filter(user=request.user).update(weight=new_weight)
            return HttpResponseRedirect('add_weight')
        cont = {'current_weight': current_weight}
        return render(request, 'weight/add_weight.html', cont)
    else:
        return redirect('login')


def WeightTracker(request):
    if request.user.is_authenticated:
        return render(request, 'weight/weight_tracker.html')
    else:
        return redirect('login')
