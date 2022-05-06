from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from calculator.forms import CalculatorForm
from calculator.models import Profile


def calcIMT(growth, weight):
    return str(round(weight/(0.0001*growth*growth), 1))


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_user_data(data):
    if data["gender"] == 1:
        db_user_data["gender"] = "Мужчина"
    else:
        db_user_data["gender"] = "Женщина"
    if data["activity"] == 1:
        db_user_data["activity_level"] = "Отсутствие активности"
    elif data["activity"] == 2:
        db_user_data["activity_level"] = "Низкая активность"
    elif data["activity"] == 3:
        db_user_data["activity_level"] = "Средняя активность"
    elif data["activity"] == 4:
        db_user_data["activity_level"] = "Высокая активность"
    elif data["activity"] == 5:
        db_user_data["activity_level"] = "Экстремальная активность"
    if data["aim"] == 1:
        db_user_data["user_aim"] = "Похудение"
    elif data["aim"] == 2:
        db_user_data["user_aim"] = "Поддержание веса"
    elif data["aim"] == 3:
        db_user_data["user_aim"] = "Набор мышечной массы"
    return db_user_data


def calcUserData(data):
    activity_index = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    aim_index = {1: 0.9, 2: 1, 3: 1.1}
    indicators = {1: [0.4, 0.3, 0.3], 2: [0.3, 0.3, 0.4], 3: [0.35, 0.2, 0.45]}
    if data["gender"] == 1:
        calories = round((10*data["weight"] + 6.25*data["growth"] - 5*data["age"] + 5) *
                         activity_index[data["activity"]]*aim_index[data["aim"]])
    else:
        calories = round((10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] - 161) *
                         activity_index[data["activity"]]*aim_index[data["aim"]])
    proteins = round(calories * indicators[data["aim"]][0] / 4)
    fats = round(calories * indicators[data["aim"]][1] / 9)
    carbohydrates = round(calories * indicators[data["aim"]][2] / 4)
    result = {'calories': calories, 'proteins': proteins, 'fats': fats, 'carbohydrates': carbohydrates}
    return result


db_user_data = {'age': 0, 'weight': 0, 'gender': "", 'growth': 0, 'activity_level': "", 'user_aim': "",
                'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}

def calculator(request):
    global db_user_data
    is_valid = False
    error_info = False
    IMT = 0
    user_data_res = {}
    form = CalculatorForm(request.POST)
    calories = ''
    proteins = ''
    fats = ''
    carbohydrates = ''
    if request.method == 'POST':
        if form.is_valid():
            temp = request.POST
            error_info = True
            if isfloat(temp["weight"]) and temp["growth"].isnumeric() and temp["age"].isnumeric():
                age = int(temp["age"])
                growth = int(temp["growth"])
                weight = float(temp["weight"])
                activity = int(temp["user_activity"])
                aim = int(temp["user_aim"])
                gender = int(temp["gender"])
                if 59 < growth < 231 and 9 < age < 101 and 25 < weight < 210:
                    db_user_data = {'age': age, 'growth': growth, 'weight': weight}
                    user_data = {'age': age, 'growth': growth, 'weight': weight, 'activity': activity,
                                 'aim': aim, 'gender': gender}
                    user_data_res = calcUserData(user_data)
                    get_user_data(user_data)
                    IMT = calcIMT(growth, weight)
                    calories = str(user_data_res['calories'])
                    proteins = str(user_data_res['proteins'])
                    fats = str(user_data_res['fats'])
                    carbohydrates = str(user_data_res['carbohydrates'])
                    db_user_data['calories'] = int(calories)
                    db_user_data['proteins'] = int(proteins)
                    db_user_data['fats'] = int(fats)
                    db_user_data['carbohydrates'] = int(carbohydrates)
                    is_valid = True

    if "save_data" in request.POST:
        Profile.objects.filter(user=request.user).update(age=db_user_data['age'], weight=db_user_data['weight'],
                                                         growth=db_user_data['growth'],
                                                         gender=db_user_data['gender'],
                                                         Activity_level=db_user_data['activity_level'],
                                                         user_aim=db_user_data['user_aim'],
                                                         needed_kkal=db_user_data['calories'],
                                                         needed_proteins=db_user_data['proteins'],
                                                         needed_fats=db_user_data['fats'],
                                                         needed_carbohydrates=db_user_data['carbohydrates'])
        return redirect('home')

    cont = {'res': is_valid,
            'error': error_info,
            'form': form,
            'imt': IMT,
            'calories': calories,
            'proteins': proteins,
            'fats': fats,
            'carbohydrates': carbohydrates,}
    return render(request, 'calculator/calculator.html', cont)



