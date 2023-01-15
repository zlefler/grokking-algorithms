def balance_parens(string):
    parens = {'(': ')', '[': ']', '{': '}'}

    stack = []

    for char in string:
        if char in parens:
            stack.append(char)
        elif not stack:
            return False
        elif parens[stack.pop()] != char:
            return False
    return True


a1 = '()()(())()'  # true
a2 = '{}()[](()){[]}'  # true
a3 = '()())(()'  # false
a4 = '([)]'  # false

print(balance_parens(a1))
print(balance_parens(a2))
print(balance_parens(a3))
print(balance_parens(a4))
