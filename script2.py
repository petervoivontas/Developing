from __future__ import division
from datetime import datetime
import math

now = datetime.now()
hours = now.hour
if len(str(hours)) == 1:
    hours = '0' + str(hours)
minutes = now.minute
if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)

print "%s:%s %s/%s/%s" % (hours, minutes, now.day, now.month, now.year)
print '' \
      ''

expression = raw_input('Type here: ')
final_numbers = []
final_symbols = []
symbols = ['+', '-', '*', '/', '**']


def expression_split(x):
    """
    :type x:str 
    """
    absolute_open = []
    absolute_close = []
    bracket_open = []
    bracket_close = []
    pindex = 0
    abs_index = 0
    power = 1
    for i in x:
        if i == '(':
            bracket_open.append(x.index(i) + pindex)
        elif i == ')':
            bracket_close.append(x.index(i) + pindex)
        x = x[x.index(i) + 1:len(x) + 1]
        pindex += 1
    abs_expr = expression
    for i in abs_expr:
        if i == '|' and len(absolute_open) == len(absolute_close):
            absolute_open.append(abs_expr.index(i) + abs_index)
        elif i == '|' and len(absolute_open) > len(absolute_close):
            absolute_close.append(abs_expr.index(i) + abs_index)
        abs_index += 1
        abs_expr = abs_expr[abs_expr.index(i) + 1:len(abs_expr) + 1]
    new_expr = expression
    number = ''
    while len(new_expr) > 0 and new_expr != ' ':
        for i in new_expr:
            if i not in new_expr:
                break
            elif i.isdigit() and (new_expr[new_expr.index(i) + 1] == ' ' or (new_expr.index(i)) + 1 == len(new_expr)):
                number += i
                if '.' in number:
                    final_numbers.append(float(number))
                elif '.' not in number:
                    final_numbers.append(int(number))
                number = ''
            elif i.isdigit() and (new_expr[new_expr.index(i) + 1].isdigit() or new_expr[new_expr.index(i) + 1] == '.'):
                number += i
                new_expr = new_expr[new_expr.index(i) + 1:len(new_expr) + 1]
            elif i.isdigit():
                final_numbers.append(int(i))
            elif i == '*' and new_expr[new_expr.index(i) + 1] == '*':
                if power % 2 != 0:
                    power += 1
                elif power % 2 == 0:
                    final_symbols.append('**')
                    power += 1
            elif i in symbols:
                final_symbols.append(i)
            elif i == '(':
                for c in zip(bracket_open, bracket_close):
                    if c[0] == expression.index(i):
                        expression_parenthesis(expression[c[0]:c[1] + 1])
                    new_expr = new_expr[0:c[0]] + new_expr[c[1] + 1:len(new_expr) + 1]
            elif i == '|':
                for c in zip(absolute_open, absolute_close):
                    if c[0] == expression.index(i):
                        absolute_value(expression[c[0]:c[1] + 1])
                    new_expr = (new_expr[0:c[0]] + new_expr[c[1] + 1:len(new_expr) + 1])
        else:
            break
    final_result(final_numbers, final_symbols)


def expression_parenthesis(x):
    """
    :type x:str 
    """
    numbers = []
    signs = []
    index = 0
    result = 0
    power = 1
    expr = x
    number = ''
    for i in expr:
        if i.isdigit() and (expr[expr.index(i) + 1] == ' ' or expr[expr.index(i) + 1] == ')'):
            number += i
            if '.' in str(number):
                numbers.append(float(number))
            elif '.' not in str(number):
                numbers.append(int(number))
            number = ''
        elif (i.isdigit() or i == '.') and (expr[expr.index(i) + 1].isdigit() or expr[expr.index(i) + 1] == '.'):
            number += i
            expr = expr[expr.index(i) + 1:len(expr) + 1]
        elif i.isdigit():
            numbers.append(int(i))
        elif i == '*' and expr[expr.index(i) + 1] == '*':
            if power % 2 != 0:
                power += 1
            elif power % 2 == 0:
                signs.append('**')
                power += 1
        elif i in symbols:
            signs.append(i)
    if len(signs) > 0:
        for i in signs:
            if i == '+' and index == 0:
                result += numbers[index] + numbers[index + 1]
                index += 1
            elif i == '+' and index > 0:
                result += numbers[index + 1]
                index += 1
            elif i == '-' and index == 0:
                result += numbers[index] - numbers[index + 1]
                index += 1
            elif i == '-' and index > 0:
                result -= numbers[index + 1]
                index += 1
            elif i == '*' and index == 0:
                result += numbers[index] * numbers[index + 1]
                index += 1
            elif i == '*' and index > 0:
                result *= numbers[index + 1]
                index += 1
            elif i == '/' and index == 0:
                result += numbers[index] / numbers[index + 1]
                index += 1
            elif i == '/' and index > 0:
                result /= numbers[index + 1]
                index += 1
            elif i == '**' and index == 0:
                result += numbers[index] ** numbers[index + 1]
                index += 1
            elif i == '**' and index > 0:
                result **= numbers[index + 1]
                index += 1
    elif len(signs) == 0:
        result += numbers[0]
    if '.' not in str(result):
        final_numbers.append(int(result))
    elif '.' in str(result):
        final_numbers.append(result)


def absolute_value(x):
    """
    :type x:str 
    """
    expr = x
    numbers = []
    signs = []
    characters = []
    index = 0
    result = 0
    number = ''
    power = 1
    for i in x:
        if i.isdigit():
            characters.append(i)
        elif i in symbols:
            characters.append(i)
    for i in expr:
        if i.isdigit() and (expr[expr.index(i) + 1] == ' ' or expr[expr.index(i) + 1] == '|'):
            number += i
            if '.' in str(number):
                numbers.append(float(number))
            elif '.' not in str(number):
                numbers.append(int(number))
            number = ''
        elif (i.isdigit() or i == '.') and (expr[expr.index(i) + 1].isdigit() or expr[expr.index(i) + 1] == '.'):
            number += i
            expr = expr[expr.index(i) + 1:len(expr) + 1]
        elif i.isdigit():
            numbers.append(int(i))
        elif i == '*' and characters[characters.index(i) + 1] == '*':
            if power % 2 != 0:
                power += 1
            elif power % 2 == 0:
                signs.append('**')
        elif i in symbols:
            signs.append(i)
    if len(signs) > 0:
        for i in signs:
            if i == '+' and index == 0:
                result += numbers[index] + numbers[index + 1]
                index += 1
            elif i == '+' and index > 0:
                result += numbers[index + 1]
                index += 1
            elif i == '-' and index == 0:
                result += numbers[index] - numbers[index + 1]
                index += 1
            elif i == '-' and index > 0:
                result -= numbers[index + 1]
                index += 1
            elif i == '*' and index == 0:
                result += numbers[index] * numbers[index + 1]
                index += 1
            elif i == '*' and index > 0:
                result *= numbers[index + 1]
                index += 1
            elif i == '/' and index == 0:
                result += numbers[index] / numbers[index + 1]
                index += 1
            elif i == '/' and index > 0:
                result /= numbers[index + 1]
                index += 1
            elif i == '**' and index == 0:
                result += numbers[index] ** numbers[index + 1]
                index += 1
            elif i == '**' and index > 0:
                result **= numbers[index + 1]
                index += 1
    elif len(signs) == 0:
        result += numbers[0]
    if '.' in str(result):
        final_numbers.append(math.fabs(result))
    elif '.' not in str(result):
        final_numbers.append(int(math.fabs(result)))


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


expression_split(expression)
