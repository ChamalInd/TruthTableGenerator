import os

variables = []
error_mzg = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'x', 'y', 'z']


def initial_setup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Truth Table Generator".center(50, '-'))
    print("v : Disjunction\n^ : Conjunction\n~ : Negation\n- : Implication\n> : Bi-Implication\n")


def verify_valid_char(inp):
    for i in inp:
        if i.isdigit():
            return False
        if (i not in ['(', ')', 'v', '^', '-', '>', '~', ' ']) and (not i.isalnum()):
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
        if inp[i] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
            if i == 0:
                if inp[i + 1] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
                    return False
            elif i == len(inp) - 1:
                if inp[i - 1] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
                    return False
            else:
                if (inp[i - 1] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']) or (inp[i + 1] not in ['(', ')', 'v', '^', '-', '>', '~', ' ']):
                    return False
        else:
            if i == 0:
                if inp[i + 1] in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
                    return False
            elif i == len(inp) - 1:
                if inp[i - 1] in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
                    return False
            else:
                if (inp[i - 1] in ['(', ')', 'v', '^', '-', '>', '~', ' ']) or (inp[i + 1] in ['(', ')', 'v', '^', '-', '>', '~', ' ']):
                    return False
    return True


def identify_variables(inp):
    for i in inp:
        if i not in ['(', ')', 'v', '^', '-', '>', '~', ' ']:
            variables.append(i)


def main():
    global error_mzg
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
    else:
        identify_variables(inp)
    print(variables)


if __name__ == '__main__':
    main()