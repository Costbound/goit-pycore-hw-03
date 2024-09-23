from datetime import datetime

def get_days_from_today(date):
    today = datetime.now()
    try:
        selectedDate = datetime.fromisoformat(date)
        return today.toordinal() - selectedDate.toordinal()
    except ValueError:
        print('Entered value must be a date in YYYY-MM-DD format')
    
print(get_days_from_today('2024-10-02'))
