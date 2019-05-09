# def is_isogram(string):
#     string = string.lower()
#     for i in string:
#         if string.count(i) > 1 or string == "":
#             return False
#     return True


# print(is_isogram('qshhghsmwjhlthxinnlntiyt'))

# s = 'qshhghsmwjhlthxinnlntiyt'
# print(set(s))


def is_isogram(string):
    return len(string) == len(set(string.lower()))


print(is_isogram("asfasflooakdsk"))
