"""
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
"""


def camel_case(s):
    s = s.lstrip(" ")
    s = s.rstrip(" ")
    s = s.capitalize()
    s = s.split(" ")
    solution = [item.capitalize() for item in s]
    return "".join(solution)


# def camel_case(string):
#     return string.title().replace(" ", "")
