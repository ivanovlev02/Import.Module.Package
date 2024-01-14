from datetime import datetime, date, time

def calculate_salary():
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    print(f'Текущая дата: {date.today()}\nТекущее время: {current_time}')