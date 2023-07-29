year = int(input())

def leap_years(years):
    if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
        return print('1')
    else:
        return print('0')
    
leap_years(year)