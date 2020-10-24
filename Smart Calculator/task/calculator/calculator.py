# write your code here


def sign(str_):
    if '-' in str_:
        if len(str_) % 2:
            return False
    return True


def calculator():
    expression = input().split(' ')
    if expression[0] == '/exit':
        print("Bye!")
        return
    elif expression[0] == '/help':
        print("The program calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.")
    elif expression[0] == '':
        pass
    else:
        if len(expression) == 1:
            print(expression[0])
        else:
            i = 1
            result = int(expression[0])
            while i < len(expression):
                if expression[i].isdigit():
                    if sign(expression[i - 1]):
                        result += int(expression[i])
                    else:
                        result -= int(expression[i])
                i += 1
            print(result)
    return True


while True:
    if calculator():
        pass
    else:
        break
