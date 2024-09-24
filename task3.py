import re

def normalize_phone(phone_number: str):
    regexp = r'[^+\d]'
    filtered_phone = re.sub(regexp, '', phone_number)
    
    result = ''
    if filtered_phone.startswith('+38') and len(filtered_phone) == 13:
        result = filtered_phone
    elif filtered_phone.startswith('0038') and len(filtered_phone) == 14:
        result = f'+380{filtered_phone[3:]}'
    elif filtered_phone.startswith('38') and len(filtered_phone) == 12:
        result = f'+{filtered_phone}'
    elif len(filtered_phone) == 10:
        result = f'+38{filtered_phone}'
    else:
        print('Wrong phone format')
        return
    
    return result
    
print(normalize_phone('00asg38(05hgdf0)1asf23-?"|"|32-34'))
