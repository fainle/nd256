from utils.stack2 import Stack


def checkout_equation(string):
    p = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    stack = list()
    for i in string:
        if i in "{[(":
            stack.append(i)

        if i in ")]}":
            if not stack:
                return False
            top = stack[-1]
            if p.get(top) == i:
                stack.pop()
            else:
                return False

    return len(stack) == 0


# str1 = "{}[](){[()]}"
str2 = "(])"

# assert checkout_equation(str1) is True
assert checkout_equation(str2) is False
