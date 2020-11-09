from _collections import deque


class Expression:
    def __init__(self):
        self.values = dict()

    def sign(self, str_):
        if '-' in str_:
            if len(str_) % 2:
                return False
        return True

    def oper(self, operator, b, a):
        a = int(a)
        b = int(b)
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "/":
            return a / b
        elif operator == "*":
            return a * b

    def calculate(self, expression):
        expression = expression.split()
        for i in range(len(expression)):
            if any(expression[i].count(x) > 1 for x in ["/", "*"]):
                print("Invalid expression")
                return True
            if expression[i] in self.values.keys():
                expression[i] = self.values[expression[i]]
        if len(expression) == 1:
            expression = expression[0].replace("+", "")
            if expression.replace("-", "").isdigit():
                print(expression.replace("--", ""))
            else:
                print("Unknown variable")
        else:
            # expr = [x for x in expression.split(" ") if x != " "]
            expr = expression
            weight = {"(": 0,
                      ")": 0,
                      "+": 1,
                      "-": 1,
                      "/": 2,
                      "*": 2
                      }
            stack = deque()
            result = deque()

            for i in range(len(expr)):
                if expr[i] in ["+", "-", "/", "*"]:
                    if len(stack) == 0:
                        stack.append(expr[i])
                    elif weight[expr[i]] <= weight[stack[-1]]:
                        result.append(self.oper(stack.pop(), result.pop(), result.pop()))
                        stack.append(expr[i])
                    else:
                        stack.append(expr[i])
                elif "(" in expr[i]:
                    stack.append(expr[i][0])
                    result.append(expr[i][1:])
                elif ")" in expr[i]:
                    result.append(expr[i][0:-1])
                    while len(stack) > 0:
                        if "(" in stack[-1]:
                            stack.pop()
                            break
                        result.append(stack.pop())
                else:
                    result.append(expr[i])
            stack.reverse()
            while len(result) > 1:
                if result[-1] in ["+", "-", "*", "/"]:
                    result.append(self.oper(result.pop(), result.pop(), result.pop()))
                elif result[-2] in ["+", "-", "*", "/"]:
                    result.append(self.oper(stack.popleft(), result.pop(),
                                            self.oper(result.pop(), a=result.pop(), b=result.pop())))
                else:
                    result.append(self.oper(stack.popleft(), result.pop(), result.pop()))
            print(result[0])
            # return True

    def if_correct(self, key, value):
        key = key.strip()
        value = value.strip()
        if key.strip().isalpha():
            if value.replace("+", "").replace("-", "").strip().isdigit():
                self.values[key] = value
                return True
            elif value in self.values.values():
                self.values.__setattr__(key, value)
                return True
            elif value in self.values.keys():
                self.values[key] = self.values[value]
                return True
            else:
                print("Invalid assignment")
        else:
            print("Invalid identifier")
        return True

    def input(self):
        expression = input()
        if '=' in expression:
            if expression.count('=') > 1:
                print("Invalid assignment")
                return True
            else:
                key, value = expression.split('=')
                return self.if_correct(key, value)
        elif expression.count("(") != expression.count(")"):
            print("Invalid expression")
            return True
        elif expression.startswith('/'):
            if expression == '/exit':
                print("Bye!")
                return False
            elif expression == '/help':
                print("The program calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.")
            else:
                print("Unknown command")
        elif expression == '':
            pass
        else:
            self.calculate(expression)
        return True


expr = Expression()
while expr.input():
    pass
