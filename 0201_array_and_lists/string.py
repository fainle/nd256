def string_reverser(string):
    s_len = len(string)
    new_string = ''

    while s_len:
        new_string += string[s_len - 1]
        s_len -= 1

    return new_string


def word_flipper(our_string):
    new_word_list = []
    word_list = our_string.split(' ')
    for i in word_list:
        new_word_list.append(string_reverser(i))

    return ' '.join(str(word) for word in new_word_list)


def word_flipper2(our_string):
    word_list = our_string.split(' ')
    for i in range(len(word_list)):
        word_list[i] = word_list[i][::-1]

    return ' '.join(str(word) for word in word_list)


s = string_reverser('hello')

assert 'olleh' == string_reverser('hello')
assert '123' == string_reverser('321')
assert 'aaa' == string_reverser('aaa')

w = word_flipper2('abc efg hello')
print(w)
