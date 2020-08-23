from utils.stack2 import Stack


def checkout_equation(string):
    stack = Stack()

    p = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for s in string:
        if s in "{[(":
            stack.push(s)
        if s in ")]}":
            top = stack.top()
            if p.get(top) == s:
                stack.pop()
            else:
                return False

    return stack.is_empty()


str1 = "{}[](){[()]}"
str2 = "([{)]}"
str3 = "(])"

assert checkout_equation(str1) is True
assert checkout_equation(str2) is False
assert checkout_equation(str3) is False
