from django.shortcuts import render

from food_diary.models import Food


def UserFood(request):
    return render(request, 'food_diary/user_food.html')

def ProductSelection(request):
    return render(request, 'food_diary/product_selection.html')

def Bakery(request):
    return render(request, 'food_diary/product_selection_bakery.html')

def Cereals(request):
    return render(request, 'food_diary/product_selection_cereals.html')

def Meat(request):
    meat = Food.objects.filter(type_of_food=1)
    return render(request, 'food_diary/product_selection_meat.html', {'meat': meat})

def VegFruit(request):
    return render(request, 'food_diary/product_selection_veg&fruit.html')

def CookedMeals(request):
    return render(request, 'food_diary/product_selection_cookedMeals.html')

def Seafood(request):
    return render(request, 'food_diary/product_selection_seafood.html')

def Sweets(request):
    return render(request, 'food_diary/product_selection_sweets.html')

def Milk(request):
    return render(request, 'food_diary/product_selection_milk.html')

