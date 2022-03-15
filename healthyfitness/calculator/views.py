from django.shortcuts import render

from calculator.forms import CalculatorForm


def calcIMT(growth, weight):
    return str(round(weight/(0.0001*growth*growth), 1))


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


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


def calculator(request):
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
                if growth > 50 and age > 0 and weight > 1:
                    user_data = {'age': age, 'growth': growth, 'weight': weight, 'activity': activity,
                                 'aim': aim, 'gender': gender}
                    user_data_res = calcUserData(user_data)
                    IMT = calcIMT(growth, weight)
                    calories = str(user_data_res['calories'])
                    proteins = str(user_data_res['proteins'])
                    fats = str(user_data_res['fats'])
                    carbohydrates = str(user_data_res['carbohydrates'])
                    is_valid = True
    cont = {'res': is_valid,
            'error': error_info,
            'form': form,
            'imt': IMT,
            'calories': calories,
            'proteins': proteins,
            'fats': fats,
            'carbohydrates': carbohydrates,}
    return render(request, 'calculator/calculator.html', cont)