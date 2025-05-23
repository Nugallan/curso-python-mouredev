### Dates ###

from datetime import datetime # importación del módulo 'datetime' para trabajar con fechas

now = datetime.now()

def print_date(date):
  print(date.year)
  print(date.month)
  print(date.day)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 12, 19)

print_date(year_2023)

from datetime import time

# Objeto 'time' sirve para encapsular tiempo
current_time = time(21, 6, 0) # Podemos introducir 'h', 'm', 's'

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6) # También podemos definirlo

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2023 - now # Podemos restar entre fechas
print(diff)

diff = year_2023.date() - current_date
print(diff)

from datetime import timedelta # 'timedelta' Nos permite trabajar con diferencias de fechas

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(200, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
