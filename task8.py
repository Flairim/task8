import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()

    current_day_of_week = today.weekday()

    birthdays_per_day = {i: [] for i in range(7)}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        days_until_birthday = (birthday - today).days

        if days_until_birthday < 0:
            days_until_birthday += 365

        if days_until_birthday == 0:
            day_to_greet = current_day_of_week
        else:
            day_to_greet = (current_day_of_week + days_until_birthday) % 7

        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        while day_name[day_to_greet] in ["Saturday", "Sunday"]:
            day_to_greet = (day_to_greet + 1) % 7

        birthdays_per_day[day_name[day_to_greet]].append(name)

    if not any(birthdays_per_day.values()):
        return {}
    else:
        return birthdays_per_day

