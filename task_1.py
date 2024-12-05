# Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime

def get_days_from_today(date:str)->int | None:
    try:
        date_input= datetime.strptime(date,'%Y-%m-%d').date()
    except ValueError:
        print('Enter the date in the format: "YYYY-MM-DD" !')
        return None
    except:
        print('Something went wrong !')
        return None
    
    date_now = datetime.now().date()
    
    return datetime.toordinal(date_now)-datetime.toordinal(date_input)


str_date = input('Enter date ("YYYY-MM-DD") >>>')

print(get_days_from_today(str_date))