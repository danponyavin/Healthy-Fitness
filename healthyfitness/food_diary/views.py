from django.shortcuts import render


def UserFood(request):
    return render(request, 'food_diary/user_food.html')

def ProductSelection(request):
    return render(request, 'food_diary/product_selection.html')
