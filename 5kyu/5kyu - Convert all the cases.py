# 5kyu - Convert all the cases!

""" In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

You must write a function that changes to a given case. It must be able to handle all three case types:

py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""

Your function must deal with invalid input as shown, though it will only be passed strings. 
Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase. """


import re

# def change_case(identifier, targetCase):
#     if targetCase not in {'kebab', 'snake', 'camel'} or re.findall(r'(-.*[_A-Z])|(_.*[-A-Z])|([A-Z].*[_-])', identifier):
#         return None
#     if targetCase is 'camel':
#         return re.sub(r'[_-][a-z]', lambda c: c.group(0)[1].upper(), identifier)
#     if targetCase is 'snake':
#         return re.sub(r'[A-Z-]', lambda c: '_' if c.group(0) == '-' else '_' + c.group(0).lower(), identifier)
#     if targetCase is 'kebab':
#         return re.sub(r'[A-Z_]', lambda c: '-' if c.group(0) == '_' else '-' + c.group(0).lower(), identifier)


def change_case(identifier, targetCase):
    if ('_' in identifier) + ('-' in identifier) + (identifier.lower() != identifier) > 1:
        return
    if targetCase is 'snake':
        return re.sub('([A-Z])', r'_\1', identifier.replace('-', '_')).lower()
    if targetCase is 'kebab':
        return re.sub('([A-Z])', r'-\1', identifier.replace('_', '-')).lower()
    if targetCase is 'camel':
        return re.sub('([_-])([a-z])', lambda m: m.group(2).upper(), identifier)


q = change_case("snakeCase", "snake")  # "snake_case"
q
q = change_case("some-lisp-name", "camel")  # "someLispName"
q
q = change_case("some-lisp-name", "snake")  # "some_lisp_name"
q
q = change_case("map_to_all", "kebab")  # "map-to-all"
q
q = change_case("doHTMLRequest", "kebab")  # "do-h-t-m-l-request"
q
q = change_case("invalid-inPut_bad", "kebab")  # None
q
q = change_case("valid-input", "huh???")  # None
q
q = change_case("", "camel")  # ""
q