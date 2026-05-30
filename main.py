import os

variables = []
error_mzg = ''
expression = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'x', 'y', 'z']


def initial_setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Truth Table Generator".center(70, '-'))
    # print("v : Disjunction\n^ : Conjunction\n~ : Negation\n- : Implication\n> : Bi-Implication\n")
    print("v : Disjunction\n^ : Conjunction\n~ : Negation\n")


def verify_valid_char(inp):
    if len(inp) <= 1:
        return False
    for i in inp:
        if i.isdigit():
            return False
        # if (i not in ['(', ')', 'v', '^', '-', '>', '~', ' ']) and (not i.isalnum()):
        if (i not in ['(', ')', 'v', '^', '~', ' ']) and (not i.isalnum()):
            return False
    return True


def verify_valid_paranthasis(inp):
    stack = []
    for i in inp:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False


def verify_valid_logic(inp):
    for i in range(len(inp)):
        # if inp[i] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
        if inp[i] not in ['(', ')', 'v', '^', '~', ' ']:
            if i == 0:
                if inp[i + 1] not in ['(', ')', 'v', '^', '~', ' ']:
                    return False
            elif i == len(inp) - 1:
                if inp[i - 1] not in ['(', ')', 'v', '^', '~', ' ']:
                    return False
            else:
                if (inp[i - 1] not in ['(', ')', 'v', '^', '~', ' ']) or (inp[i + 1] not in ['(', ')', 'v', '^', '~', ' ']):
                    return False
        elif inp[i] in ['v', '^', '-', '>', '~']:
            if i == 0:
                # if inp[i + 1] in ['v', '^', '-', '>', '~']:
                if inp[i + 1] in ['v', '^', '~']:
                    return False
            elif i == len(inp) - 1:
                if inp[i - 1] in ['v', '^', '~']:
                    return False
            else:
                if (inp[i - 1] in ['v', '^', '~']) or (inp[i + 1] in ['v', '^', '~']):
                    return False
    return True


def identify_variables(inp):
    global variables

    for i in inp:
        # if i not in ['(', ')', 'v', '^', '-', '>', '~', ' '] and i not in variables:
        if i not in ['(', ')', 'v', '^', '~', ' '] and i not in variables:
            variables.append(i)


def rearrange_logic(inp):
    # unicodes = {'v': ' ∨ ', '^': ' ∧ ', '-': ' → ', '>': ' ↔ ', '~': ' ¬'}
    unicodes = {'v': ' ∨ ', '^': ' ∧ ', '~': ' ¬'}
    temp = inp

    for i in unicodes.keys():
        if i in unicodes.keys():
            temp = temp.replace(i, unicodes[i])
    return temp


def generate_truth_table(inp):
    global variables, expression

    logic_values = []
    unicodes = {'∨': '|', '∧': '&', '¬': '~'}

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Truth Table Generator".center(70, '-'))
    print(f'Truth table of expression : {expression}')

    for i in unicodes:
        if i in unicodes.keys():
            expression = expression.replace(i, unicodes[i])

    # for i in range(len(expression) - 1, -1, -1):
    #     if expression[i] == '→':
    #         temp = ['', '']
    #         temp[0] = expression[i + 1:]
    #         temp[1] = expression[:i]
    #         print(temp)
    #         if verify_valid_paranthasis(temp[0]) and verify_valid_paranthasis(temp[1]):
    #             expression = f'~ ({temp[1]}) | ({temp[0]})'
    #         elif verify_valid_paranthasis(temp[0]):
    #             expression = f'~ ({temp[1]}) | (({temp[0]})'
    #         elif verify_valid_paranthasis(temp[1]):
    #             expression = f'~ ({temp[1]})) | ({temp[0]})'
    #         else:
    #             expression = f'~ ({temp[1]})) | (({temp[0]})'
    #     # if i == '↔':
    #     #     temp = expression.split(i)
    #     #     expression = f'~ ({temp[0]}) | ({temp[1]})'
    
    # print(expression)

    for i in variables:
        logic_values.append(0)
        print(f'{i.upper()}\t', end='')
    print('_')

    for i in range(2**len(variables)):
        temp = expression
        for k in range(len(variables)):
            temp = temp.replace(variables[k], str(logic_values[k]))
        for j in logic_values:
            print(f'{j}\t', end='')
        print(eval(temp))
        logic_values[len(logic_values) - 1] += 1
        for j in range(len(logic_values) - 1, -1, -1):
            if logic_values[j] > 1:
                logic_values[j] = 0
                logic_values[j - 1] += 1



def main():
    global error_mzg, expression

    initial_setup()
    print(error_mzg)
    inp = input(": ").lower()
    if inp == 'e':
        exit()
    if not verify_valid_char(inp):
        error_mzg = f"{inp} has invalid characters."
        return main()
    if not verify_valid_paranthasis(inp):
        error_mzg = f"{inp} has invalid paranthesis."
        return main()
    if not verify_valid_logic(inp):
        error_mzg = f"{inp} has invalid logic."
        return main()
    
    identify_variables(inp)
    expression = rearrange_logic(inp)
    generate_truth_table(inp)


if __name__ == '__main__':
    main()