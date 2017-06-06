from __future__ import division
import math
import sys

final_numbers = [5, 4, 8, 6, 7, 3]
final_symbols = ['**', '/', '-', '+', '*']


def final_result(x, y):
    """
    :type x:list
    :type y:list
    """
    result = 0
    if '**' in y:
        for i in y:
            if i == '**':
                x.insert(y.index(i), (x[y.index(i)] ** x[y.index(i) + 1]))
                del x[y.index(i) + 1:y.index(i) + 3]
                y = y[0:y.index(i)] + y[y.index(i) + 1:len(y) + 1]
    if '*' in y and '/' in y:
        for i in y:
            if i == '*':
                x.insert(y.index(i), (x[y.index(i)] * x[y.index(i) + 1]))
                del x[y.index(i) + 1:y.index(i) + 3]
                y = y[0:y.index(i)] + y[y.index(i) + 1:len(y) + 1]
            elif i == '/':
                x.insert(y.index(i), (x[y.index(i)] / x[y.index(i) + 1]))
                del x[y.index(i) + 1:y.index(i) + 3]
                y = y[0:y.index(i)] + y[y.index(i) + 1:len(y) + 1]
    elif '*' in y:
        for i in y:
            if i == '*':
                x.insert(y.index(i), (x[y.index(i)] * x[y.index(i) + 1]))
                del x[y.index(i) + 1:y.index(i) + 3]
                y = y[0:y.index(i)] + y[y.index(i) + 1:len(y) + 1]
    elif '/' in y:
        for i in y:
            if i == '/':
                x.insert(y.index(i), (x[y.index(i) / x[y.index(i) + 1]]))
                del x[y.index(i) + 1:y.index(i) + 3]
                y = y[0:y.index(i)] + y[y.index(i) + 1:len(y) + 1]
    if ('+' in y or '-' in y) and ('*' not in y and '/' not in y):
        for i in y:
            if i == '+' and result == 0:
                result += x[y.index(i)] + x[y.index(i) + 1]
            elif i == '+' and result > 0:
                result += x[y.index(i) + 1]
            elif i == '-' and result == 0:
                result += x[y.index(i)] - x[y.index(i) + 1]
            elif i == '-' and result > 0:
                result -= x[y.index(i) + 1]
    if len(x) == 1:
        result += x[0]
    print result


final_result(final_numbers, final_symbols)
