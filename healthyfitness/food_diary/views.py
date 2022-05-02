from django.shortcuts import render

from food_diary.models import Food


def UserFood(request):
    return render(request, 'food_diary/user_food.html')

def ProductSelection(request):
    return render(request, 'food_diary/product_selection.html')

def Bakery(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=6)
    else:
        data = Food.objects.filter(type_of_food=6)
    return render(request, 'food_diary/product_selection_bakery.html', {'data': data, 'error': error})

def Cereals(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=3)
    else:
        data = Food.objects.filter(type_of_food=3)
    return render(request, 'food_diary/product_selection_cereals.html', {'data': data, 'error': error})

def Meat(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=1)
    else:
        data = Food.objects.filter(type_of_food=1)
    return render(request, 'food_diary/product_selection_meat.html', {'data': data, 'error': error})

def VegFruit(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=7)
    else:
        data = Food.objects.filter(type_of_food=7)
    return render(request, 'food_diary/product_selection_veg&fruit.html', {'data': data, 'error': error})

def CookedMeals(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=10)
    else:
        data = Food.objects.filter(type_of_food=10)
    return render(request, 'food_diary/product_selection_cookedMeals.html', {'data': data, 'error': error})

def Seafood(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=2)
    else:
        data = Food.objects.filter(type_of_food=2)
    return render(request, 'food_diary/product_selection_seafood.html', {'data': data, 'error': error})

def Sweets(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=5)
    else:
        data = Food.objects.filter(type_of_food=5)
    return render(request, 'food_diary/product_selection_sweets.html', {'data': data, 'error': error})

def Milk(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=4)
    else:
        data = Food.objects.filter(type_of_food=4)
    return render(request, 'food_diary/product_selection_milk.html', {'data': data, 'error': error})

def Drinks(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=8)
    else:
        data = Food.objects.filter(type_of_food=8)
    return render(request, 'food_diary/product_selection_drinks.html', {'data': data, 'error': error})

def Nuts_and_oils(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=9)
    else:
        data = Food.objects.filter(type_of_food=9)
    return render(request, 'food_diary/product_selection_nuts&oils.html', {'data': data, 'error': error})

def Herbs_and_spices(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=11)
    else:
        data = Food.objects.filter(type_of_food=11)
    return render(request, 'food_diary/product_selection_herbs&spices.html', {'data': data, 'error': error})

def Fast_food(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=12)
    else:
        data = Food.objects.filter(type_of_food=12)
    return render(request, 'food_diary/product_selection_fast_food.html', {'data': data, 'error': error})

def Search(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query)
        return render(request, 'food_diary/product_search.html', {'data': data, 'error': error})
    else:
        return render(request, 'food_diary/product_search.html')