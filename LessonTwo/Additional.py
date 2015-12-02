# Create a game  - "guess arithmetic actions" that can give such result
# 1?15?3.....?=12 / number of inputs can be different
import itertools


def guess_me():
    while True:
        input_value = raw_input("\nPlease input numbers in format (first "
                                "number,second number,third number, ....,"
                                "result)\n>").split(",")
        input_float_values_in_str_list = [str(float(x)) for x in input_value]
        actions_list = ["+", "-", "/", "*"]
        ex_result = float(input_float_values_in_str_list[-1])
        # Creating possible combinations of actions
        actions = itertools.\
            product(actions_list, repeat=len(input_float_values_in_str_list)-2)
        expressions_list = list()
        # Creating expressions to eval
        guessed = False
        for action in actions:
            expr = zip(input_float_values_in_str_list[:-2], action)
            expr_1 = list()
            for r in range(len(expr)):
                expr_1.append(''.join(expr[r]))
            expr_1.append((input_float_values_in_str_list[-2]))
            expressions_list.append(''.join(expr_1))

        for w in expressions_list:
            expression = ''.join(w)
            try:
                ev_result = eval(expression)
                if ev_result == ex_result:
                    guessed = True
                    print expression + " -> " + str(ex_result)
            except ZeroDivisionError:
                pass
        if not guessed:
            print "Its impossible combination!!!"

guess_me()
