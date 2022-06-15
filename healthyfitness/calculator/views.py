from datetime import date

from django.shortcuts import render, redirect
from calculator.forms import CalculatorForm
from calculator.models import Profile
from weight.models import Weight_trecker
from calculator.calculator_functions import calcIMT, isfloat, getUserData, calcUserData, dbUserData, data_valid


def calculator(request):
    global dbUserData
    is_valid = error_info = False
    form = CalculatorForm(request.POST)
    userInfo = {'calories': '', 'proteins': '', 'fats': '', 'carbohydrates': '', 'IMT': 0}
    if request.method == 'POST':
        if form.is_valid():
            temp = request.POST
            error_info = True
            if isfloat(temp["weight"]) and temp["growth"].isnumeric() and temp["age"].isnumeric():
                userDataNumbers = {'age': int(temp["age"]), 'growth': int(temp["growth"]),
                                   'weight': float(temp["weight"]),
                                   'activity': int(temp["user_activity"]), 'aim': int(temp["user_aim"]),
                                   'gender': int(temp["gender"])}
                if data_valid(userDataNumbers):
                    dbUserData = {'age': userDataNumbers['age'], 'growth': userDataNumbers['growth'],
                                  'weight': userDataNumbers['weight']}
                    userDataResults = calcUserData(userDataNumbers)
                    dbUserData.update(getUserData(userDataNumbers))
                    dbUserData['calories'] = userDataResults['calories']
                    dbUserData['proteins'] = userDataResults['proteins']
                    dbUserData['fats'] = userDataResults['fats']
                    dbUserData['carbohydrates'] = userDataResults['carbohydrates']
                    userInfo = {'calories': str(dbUserData['calories']), 'proteins': str(dbUserData['proteins']),
                                'fats': str(dbUserData['fats']), 'carbohydrates': str(dbUserData['carbohydrates']),
                                'IMT': calcIMT(dbUserData['growth'], dbUserData['weight'])}
                    is_valid = True
    if "save_data" in request.POST:
        user_photo = Profile.objects.filter(user=request.user)[0].photo
        user_info = Profile(user=request.user, age=dbUserData["age"], weight=dbUserData["weight"],
                            gender=dbUserData["gender"], growth=dbUserData["growth"],
                            user_aim=dbUserData["user_aim"],
                            Activity_level=dbUserData["activity_level"], needed_kkal=dbUserData["calories"],
                            needed_proteins=dbUserData["proteins"], needed_fats=dbUserData["fats"],
                            needed_carbohydrates=dbUserData["carbohydrates"], photo=user_photo)
        user_info.save()
        return redirect('personalArea')
    cont = {'res': is_valid,
            'error': error_info,
            'form': form,
            'imt': userInfo['IMT'],
            'calories': userInfo['calories'],
            'proteins': userInfo['proteins'],
            'fats': userInfo['fats'],
            'carbohydrates': userInfo['carbohydrates'], }
    return render(request, 'calculator/calculator.html', cont)
