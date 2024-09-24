from datetime import datetime

def get_upcoming_birthdays(users: list):
    result= []
    
    for user in users:
        get_upcoming_birthday(user['birthday'])
    
    return

def get_upcoming_birthday(date):
    birthday = datetime.strptime(date, "%Y.%m.%d").date()
    today = datetime.today().date()
    birthday_this_year = birthday.replace(year=today.year)
    next_birthday = ''
    
    if birthday_this_year < today:
        next_year = datetime(year=today.year + 1, month = 1, day = 1).date()
        next_birthday = birthday_this_year.replace(year=birthday_this_year.year + 1)
    else:
        next_birthday = birthday_this_year
        
    if (next_birthday.toordinal() - today.toordinal()) > 7:
        print('Too far to birthday')
        print('-----------------------')
        return None
    
    print(birthday)
    print(today)
    print(next_birthday, (next_birthday.toordinal() - today.toordinal()))
    print('-----------------------')

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Judy Smuth", "birthday": "1990.10.01"}
]

print(get_upcoming_birthdays(users))
