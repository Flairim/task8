import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()

    current_day_of_week = today.weekday()

    birthdays_per_day = {i: [] for i in range(7)}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        days_until_birthday = (birthday - today).days

        if days_until_birthday == 0:  
            day_to_greet = current_day_of_week
        else:
            day_to_greet = (current_day_of_week + days_until_birthday) % 7

        birthdays_per_day[day_to_greet].append(name)
        
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day_index in range(7):
        day_name = days_of_week[day_index]
        names = ', '.join(birthdays_per_day[day_index])
        if names:
            print(f"{day_name}: {names}")
            