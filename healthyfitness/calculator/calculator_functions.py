
dbUserData = {'age': 0, 'weight': 0, 'gender': "", 'growth': 0, 'activity_level': "", 'user_aim': "",
              'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}


def data_valid(userDataNumbers: dict) -> bool:
    return 59 < userDataNumbers['growth'] < 231 and 9 < userDataNumbers['age'] < 101 \
           and 25 < userDataNumbers['weight'] < 210


def calcIMT(growth, weight):
    res = ""
    try:
        res = str(round(weight / (0.0001 * growth * growth), 1))
    except ZeroDivisionError:
        res = "Wrong weight or growth"
    return res


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def getUserData(data):
    gender_dict = {1: "Мужчина", 2: "Женщина"}
    activity_dict = {1: "Отсутствие активности", 2: "Низкая активность", 3: "Средняя активность",
                     4: "Высокая активность", 5: "Экстремальная активность"}
    aim_dict = {1: "Похудение", 2: "Поддержание веса", 3: "Набор мышечной массы"}
    dbUserData["gender"] = gender_dict[data["gender"]]
    dbUserData["activity_level"] = activity_dict[data["activity"]]
    dbUserData["user_aim"] = aim_dict[data["aim"]]
    return dbUserData


def calcCalories(data):
    activity_index = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    aim_index = {1: 0.9, 2: 1, 3: 1.1}
    if data["gender"] == 1:
        calories = round((10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5) *
                         activity_index[data["activity"]] * aim_index[data["aim"]])
    else:
        calories = round((10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] - 161) *
                         activity_index[data["activity"]] * aim_index[data["aim"]])
    return calories


def calcUserData(data: dict):
    if not data_valid(data):
        return {'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}

    indicators = {1: [0.4, 0.3, 0.3], 2: [0.3, 0.3, 0.4], 3: [0.35, 0.2, 0.45]}
    calories = calcCalories(data)
    proteins = round(calories * indicators[data["aim"]][0] / 4)
    fats = round(calories * indicators[data["aim"]][1] / 9)
    carbohydrates = round(calories * indicators[data["aim"]][2] / 4)
    result = {'calories': calories, 'proteins': proteins, 'fats': fats, 'carbohydrates': carbohydrates}
    return result
