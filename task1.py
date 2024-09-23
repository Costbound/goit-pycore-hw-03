from datetime import datetime

def get_days_from_today(date):
    today = datetime.now()
    selectedDate = datetime.fromisoformat(date)
    return today.toordinal() - selectedDate.toordinal()
    
print(get_days_from_today('2024-09-21'))
