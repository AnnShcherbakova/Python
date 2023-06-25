#Выполните функцию проверки скобок для двух видов скобок:
# круглых и квадратных.  pars = {")":"(","]":"["} def paren_checker(string): stack =[]
def paren_checker(string):
    stack = []
    a = {")": "(", "]": "["}

    for s in string:
        if s in ["(", "["]:
            stack.append(s)
        elif s in [")", "]"]:
            if len(stack) > 0 and stack[-1] == a[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(paren_checker("([)]"))
print(paren_checker("[()]"))
print(paren_checker("([)]"))
print(paren_checker("[[()]]"))