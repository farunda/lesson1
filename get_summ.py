#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

def get_summ(one, two, delimeter=' '):
    return str(one).upper() + str(delimeter) + str(two).upper()

first = input('enter one ')
second = input('enter two ')

print(get_summ(first, second))