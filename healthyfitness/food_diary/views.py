import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from calculator.models import Profile
from food_diary.models import Food, Diary_of_food


def UserFood(request):
    error = "У Вас нет записей по выбранной дате!"
    total_amount = {'weight': 0, 'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}
    current_user = Profile.objects.get(user=request.user)
    meals_today = ''

    if request.POST.get('id'):
        record_id = request.POST.get('id')
        record = Diary_of_food.objects.get(id=record_id)
        record.delete()



    search_query = request.GET.get('search', '')
    if search_query:
        meals_today = Diary_of_food.objects.filter(day_create=search_query, id_users=current_user)
    else:
        today = datetime.date.today()
        meals_today = Diary_of_food.objects.filter(day_create=today, id_users=current_user)
    for i in range(len(meals_today)):
        total_amount['weight'] += meals_today[i].grams
        total_amount['calories'] += meals_today[i].consumed_kkal
        total_amount['proteins'] += meals_today[i].consumed_proteins
        total_amount['fats'] += meals_today[i].consumed_fats
        total_amount['carbohydrates'] += meals_today[i].consumed_carbohydrates
    return render(request, 'food_diary/user_food.html', {'data': meals_today, 'value': search_query, 'total': total_amount,
                                                         'error': error})

def ProductSelection(request):
    return render(request, 'food_diary/product_selection.html')

def Bakery(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=6)
    else:
        data = Food.objects.filter(type_of_food=6)
    return render(request, 'food_diary/product_selection_bakery.html', {'data': data, 'error': error, 'value': search_query})

def Cereals(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=3)
    else:
        data = Food.objects.filter(type_of_food=3)
    return render(request, 'food_diary/product_selection_cereals.html', {'data': data, 'error': error, 'value': search_query})

def Meat(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=1)
    else:
        data = Food.objects.filter(type_of_food=1)
    return render(request, 'food_diary/product_selection_meat.html', {'data': data, 'error': error, 'value': search_query})

def VegFruit(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=7)
    else:
        data = Food.objects.filter(type_of_food=7)
    return render(request, 'food_diary/product_selection_veg&fruit.html', {'data': data, 'error': error, 'value': search_query})

def CookedMeals(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=10)
    else:
        data = Food.objects.filter(type_of_food=10)
    return render(request, 'food_diary/product_selection_cookedMeals.html', {'data': data, 'error': error, 'value': search_query})

def Seafood(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=2)
    else:
        data = Food.objects.filter(type_of_food=2)
    return render(request, 'food_diary/product_selection_seafood.html', {'data': data, 'error': error, 'value': search_query})

def Sweets(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=5)
    else:
        data = Food.objects.filter(type_of_food=5)
    return render(request, 'food_diary/product_selection_sweets.html', {'data': data, 'error': error, 'value': search_query})

def Milk(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=4)
    else:
        data = Food.objects.filter(type_of_food=4)
    return render(request, 'food_diary/product_selection_milk.html', {'data': data, 'error': error, 'value': search_query})

def Drinks(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=8)
    else:
        data = Food.objects.filter(type_of_food=8)
    return render(request, 'food_diary/product_selection_drinks.html', {'data': data, 'error': error, 'value': search_query})

def Nuts_and_oils(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=9)
    else:
        data = Food.objects.filter(type_of_food=9)
    return render(request, 'food_diary/product_selection_nuts&oils.html', {'data': data, 'error': error, 'value': search_query})

def Herbs_and_spices(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=11)
    else:
        data = Food.objects.filter(type_of_food=11)
    return render(request, 'food_diary/product_selection_herbs&spices.html', {'data': data, 'error': error, 'value': search_query})

def Fast_food(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query, type_of_food=12)
    else:
        data = Food.objects.filter(type_of_food=12)
    return render(request, 'food_diary/product_selection_fast_food.html', {'data': data, 'error': error, 'value': search_query})


def Search(request):
    search_query = request.GET.get('search', '')
    error = "К сожалению, по Вашему запросу ничего не найдено..."
    if request.POST.get('product_weight'):
        product_weight = request.POST.get('product_weight')
        if int(product_weight) > 0:
            product = request.POST.get('id')
            info = Food.objects.filter(id=product)
            product_info = {'id': product, 'product_name': info[0].name_of_product, 'weight': int(product_weight),
                            'kkal': info[0].kkal, 'proteins': info[0].proteins, 'fats': info[0].fats, 'carbohydrates': info[0].carbohydrates}
            product_info = calculate_food_data(product_info)
            user_id = Profile.objects.get(user=request.user)
            food_id = Food.objects.get(id=product_info["id"])
            user_choice = Diary_of_food(id_users=user_id, id_food=food_id, grams=product_info['weight'],
                                                                       consumed_kkal=product_info['kkal'],
                                                                       consumed_proteins=product_info['proteins'],
                                                                       consumed_fats=product_info['fats'],
                                                                       consumed_carbohydrates=product_info['carbohydrates'])
            user_choice.save()
            return HttpResponseRedirect('search')
    if search_query:
        data = Food.objects.filter(name_of_product__iregex=search_query)
        return render(request, 'food_diary/product_search.html', {'data': data, 'error': error, 'value': search_query})
    else:
        return render(request, 'food_diary/product_search.html')


def calculate_food_data(info):
    index = info['weight']/100
    info['kkal'] = round(info['kkal']*index, 2)
    info['fats'] = round(info['fats']*index, 2)
    info['proteins'] = round(info['proteins']*index, 2)
    info['carbohydrates'] = round(info['carbohydrates']*index, 2)
    return info


