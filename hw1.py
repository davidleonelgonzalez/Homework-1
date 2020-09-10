# David Gonzalez
# 1630338

print('Birth Calculator')
print('Current day')
cur_month = int(input('Month:'))
cur_day = int(input('Day:'))
cur_year = int(input('Year:'))

print('Birthday')
birth_month = int(input('Month:'))
birth_day = int(input('Day:'))
birth_year = int(input('Year:'))

num_years = cur_year - birth_year - 2
if birth_month < cur_year:
    num_years += 1
elif cur_month == birth_month:
    if birth_day < cur_day:
        num_years += 1
if cur_month == birth_month and cur_day == birth_day:
    print('Happy Birthday')
print('You are ' + str(num_years), 'years old.')
print()
