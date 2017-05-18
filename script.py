from __future__ import division
from datetime import datetime
import math
import sys

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
    bracket_open = []
    bracket_close = []
    parenthesis = []
    index = 0
    zip_list = []
    power = 1
    for i in x:
        if i == '(':
            bracket_open.append(x.index(i) + index)
        elif i == ')':
            bracket_close.append(x.index(i) + index)
        x = x[x.index(i) + 1:len(x) + 1]
        index += 1
    new_expr = expression
    if len(bracket_open) >= 2 and len(bracket_close) >= 2:
        for i in zip(bracket_close, bracket_open[1:len(bracket_open) + 1]):
            expr = new_expr
            number = ''
            for c in expr[i[0] + 1:i[1]]:
                if c.isdigit() and expr[expr.index(c) + 1] == ' ':
                    number += c
                    final_numbers.append(int(number))
                    number = ''
                elif c.isdigit() and expr[expr.index(c) + 1].isdigit():
                    number += c
                    expr = expr[expr.index(c) + 1:len(expr) + 1]
                elif c.isdigit():
                    final_numbers.append(int(c))
                elif c == '*' and expr[expr.index(c) + 1] == '*':
                    if power % 2 != 0:
                        power += 1
                    elif power % 2 == 0:
                        final_symbols.append('**')
                        power += 1
                elif c in symbols:
                    final_symbols.append(c)
        for i in zip(bracket_open, bracket_close):
            zip_list.append(i)
        for i in zip_list:
            if zip_list.index(i) == 0:
                expr = new_expr
                number = ''
                for c in expr[0:i[0]]:
                    if c.isdigit() and expr[expr.index(c) + 1] == ' ':
                        number += c
                        final_numbers.append(int(number))
                        number = ''
                    elif c.isdigit() and expr[expr.index(c) + 1].isdigit():
                        number += c
                        expr = expr[expr.index(c) + 1:len(expr) + 1]
                    elif c.isdigit():
                        final_numbers.append(int(c))
                    elif c == '*' and expr[expr.index(c) + 1] == '*':
                        if power % 2 != 0:
                            power += 1
                        elif power % 2 == 0:
                            final_symbols.append('**')
                            power += 1
                    elif c in symbols:
                        final_symbols.append(c)
            elif zip_list.index(i) == len(zip_list):
                expr = new_expr
                number = ''
                for c in expr[i[1] + 1:len(expr) + 1]:
                    if c.isdigit() and expr[expr.index(c) + 1] == ' ':
                        number += c
                        final_numbers.append(int(number))
                        number = ''
                    elif c.isdigit() and expr[expr.index(c) + 1].isdigit():
                        number += c
                        expr = expr[expr.index(c) + 1:len(expr) + 1]
                    elif c.isdigit():
                        final_numbers.append(int(c))
                    elif c == '*' and expr[expr.index(c) + 1] == '*':
                        if power % 2 != 0:
                            power += 1
                        elif power % 2 == 0:
                            final_symbols.append('**')
                            power += 1
                    elif c in symbols:
                        final_symbols.append(c)
            parenthesis.append(new_expr[i[0]:i[1] + 1])
        for i in parenthesis:
            expression_parenthesis(i)
    elif len(bracket_open) == 0 and len(bracket_close) == 0:
        expr = new_expr
        number = ''
        for i in expr:
            if i.isdigit() and expr[expr.index(i) + 1] == ' ':
                number += i
                final_numbers.append(int(number))
                number = ''
            elif i.isdigit() and expr[expr.index(i) + 1].isdigit():
                number += i
                expr = expr[expr.index(i) + 1:len(expr) + 1]
            elif i.isdigit():
                final_numbers.append(int(i))
            elif i == '*' and expr[expr.index(i) + 1] == '*':
                if power % 2 != 0:
                    power += 1
                elif power % 2 == 0:
                    final_symbols.append('**')
                    power += 1
            elif i in symbols:
                final_symbols.append(i)
    elif len(bracket_open) == 1 and len(bracket_close) == 1:
        for i in zip(bracket_open, bracket_close):
            expr = new_expr
            number = ''
            parenthesis.append(new_expr[i[0]:i[1] + 1])
            for c in expr[0:i[0]]:
                if c.isdigit() and expr[expr.index(c) + 1] == ' ':
                    number += c
                    final_numbers.append(int(number))
                    number = ''
                elif c.isdigit() and expr[expr.index(c) + 1].isdigit():
                    number += c
                    expr = expr[expr.index(c) + 1:len(expr) + 1]
                elif c.isdigit():
                    final_numbers.append(int(c))
                elif c == '*' and expr[expr.index(c) + 1] == '*':
                    if power % 2 != 0:
                        power += 1
                    elif power % 2 == 0:
                        final_symbols.append('**')
                        power += 1
                elif c in symbols:
                    final_symbols.append(c)
            expr = new_expr
            number = ''
            for c in expr[i[1] + 1:len(expr) + 1]:
                if c.isdigit() and expr[expr.index(c) + 1] == ' ':
                    number += c
                    final_numbers.append(int(number))
                    number = ''
                elif c.isdigit() and expr[expr.index(c) + 1].isdigit():
                    number += c
                    expr = expr[expr.index(c) + 1:len(expr) + 1]
                elif c.isdigit():
                    final_numbers.append(int(c))
                elif c == '*' and expr[expr.index(c) + 1] == '*':
                    if power % 2 != 0:
                        power += 1
                    elif power % 2 == 0:
                        final_symbols.append('**')
                        power += 1
                elif c in symbols:
                    final_symbols.append(c)
        for i in parenthesis:
            expression_parenthesis(i)
    final_result(final_numbers, final_symbols)


def expression_parenthesis(x):
    """
    :type x:str 
    """
    numbers = []
    signs = []
    index = 0
    result = 0
    characters = []
    power = 1
    for i in x[1:len(x) - 1]:
        if i.isdigit() or i in symbols:
            characters.append(i)
    expr = x
    number = ''
    for i in expr:
        if i.isdigit() and expr[expr.index(i) + 1] == ' ':
            number += i
            numbers.append(int(number))
            number = ''
        elif i.isdigit() and expr[expr.index(i) + 1].isdigit():
            number += i
            expr = expr[expr.index(i) + 1:len(expr) + 1]
        elif i.isdigit():
            numbers.append(int(i))
        elif i == '*' and characters[characters.index(i) + 1] == '*':
            if power % 2 != 0:
                power += 1
            elif power % 2 == 0:
                signs.append('**')
                power += 1
        elif i in symbols:
            signs.append(i)
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
    final_numbers.insert(expression.index(x), result)


def final_result(x, y):
    """
    :type x:list
    :type y:list
    """
    index = 0
    result = 0
    for i in y:
        if i == '+' and index == 0:
            result += x[index] + x[index + 1]
            index += 1
        elif i == '+' and index > 0:
            result += x[index + 1]
            index += 1
        elif i == '-' and index == 0:
            result += x[index] - x[index + 1]
            index += 1
        elif i == '-' and index > 0:
            result -= x[index + 1]
            index += 1
        elif i == '*' and index == 0:
            result += x[index] * x[index + 1]
            index += 1
        elif i == '*' and index > 0:
            result *= x[index + 1]
            index += 1
        elif i == '/' and index == 0:
            result += x[index] / x[index + 1]
            index += 1
        elif i == '/' and index > 0:
            result /= x[index + 1]
            index += 1
        elif i == '**' and index == 0:
            result += x[index] ** x[index + 1]
            index += 1
        elif i == '**' and index > 0:
            result **= x[index + 1]
    print result

expression_split(expression)
