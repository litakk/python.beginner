# #### datetime.datetime.now() :
# - Return the current local date and time.
# - RU: Возвращает текущую локальную дату и время.
import datetime
print(datetime.datetime.now())

# #### datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]) :
# - The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. 
#    The remaining arguments may be ints, longs, or floats, and may be positive or negative.
# - RU: Требуются аргументы год, месяц и день. tzinfo может быть None или экземпляром подкласса tzinfo.
#    Оставшиеся аргументы могут быть целыми числами, длинными или плавающими, и могут быть положительными или отрицательными.
print(datetime.datetime(2020, 5, 17, 12, 30, 0, 0))

# ### Timedelta
# - EN: The timedelta class is used to represent the difference between two dates or times.
# - RU: Класс timedelta используется для представления разницы между двумя датами или временем.
# import datetime
print(datetime.timedelta(days=365, hours=5, minutes=1))

# - timedelta can add days, seconds and microseconds to a datetime object
# - RU: timedelta может добавлять дни, секунды и микросекунды к объекту datetime
import datetime
now = datetime.now()
print(now)
# >>> datetime.datetime(2023, 7, 31, 12, 30, 10, 999999)

print(now + datetime.timedelta(days=365))
# >>> datetime.datetime(*2024*, 7, 30, 12, 30, 10, 999999)

# ```