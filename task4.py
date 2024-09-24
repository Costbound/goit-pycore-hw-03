from datetime import datetime, timedelta
import calendar

def get_upcoming_birthdays(users: list):
    result= []
    
    for user in users:
        congratulation_date = get_upcoming_birthday(user['birthday'])
        if congratulation_date:
            congratulation_date_str = f'{congratulation_date.year}.{congratulation_date.month:02}.{congratulation_date.day:02}'
            result.append({'name': user['name'], 'congratulation_date': congratulation_date_str})
    
    return result

#------------------------------------------------------------------
def get_upcoming_birthday(date):
    birthday = datetime.strptime(date, "%Y.%m.%d").date()
    today = datetime.today().date()
    
    #Check if next birthday this year or next
    next_birthday = get_next_birthday(birthday)
        
    #Check how much days to next birthday and if more than 7 return None
    days_to_birthday = next_birthday.toordinal() - today.toordinal()
    
    if days_to_birthday > 7:
        return None
    
    #Check weekday of next birthday and if this date is weekend change congratulation date to next Monday
    congratulation_date = get_congratulation_date(next_birthday)

    return congratulation_date
    
#------------------------------------------------------------------
def get_next_birthday(birthday: datetime):
    today = datetime.today().date()
    
    #In case birthday is on 29th February, transfer it to 1st March if now is not leap year
    birthday_this_year = ''
    
    if birthday.month == 2 and birthday.day == 29:
        if calendar.isleap(today.year):
            birthday_this_year = birthday.replace(year=today.year)
        else:
            birthday_this_year = birthday.replace(year=today.year, month=3, day=1)
    else:
        birthday_this_year = birthday.replace(year=today.year)

    #Get next birthday date
    next_birthday = birthday_this_year
    
    if birthday_this_year < today:
        if calendar.isleap(birthday_this_year.year):
            next_birthday += timedelta(days=366)
        else:
            next_birthday += timedelta(days=365)
    
    return next_birthday

#------------------------------------------------------------------
def get_congratulation_date(next_birthday: datetime):
    birthday_weekday = next_birthday.weekday()
    congratulation_date = next_birthday
    
    if birthday_weekday == 5:
        congratulation_date += timedelta(days=2)
    elif birthday_weekday == 6:
        congratulation_date += timedelta(days=1)
        
    return congratulation_date

users = [
    {"name": "John Doe", "birthday": "1992.09.28"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Judy Smuth", "birthday": "1990.10.01"}
]

print(get_upcoming_birthdays(users))
