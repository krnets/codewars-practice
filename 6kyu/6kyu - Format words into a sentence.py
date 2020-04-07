# 6kyu - Format words into a sentence

""" Complete the method so that it formats the words into a single comma separated value. 
The last word should be separated by the word 'and' instead of a comma. 
The method takes in an array of strings and returns a single formatted string. 
Empty string values should be ignored. 
Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

formatWords(['ninja', 'samurai', 'ronin']) // should return "ninja, samurai and ronin"
formatWords(['ninja', '', 'ronin']) // should return "ninja and ronin"
formatWords([]) // should return ""    """

# def format_words(words):
#     if words is None:
#         return ''
#     words = [x for x in words if x]
#     return ', '.join(words[:-1]) + ' and ' + words[-1] if len(words) > 1 else ''.join(words)


# def format_words(words):
#     if not words:
#         return ''
#     words = [x for x in words if x]
#     return ', '.join(words[:-1]) + ' and ' + words[-1] if len(words) > 1 else ''.join(words)

def format_words(words):
    return ' and '.join(', '.join(filter(bool, words or [])).rsplit(', ', 1))


q = format_words(['one', 'two', 'three', 'four'])  # 'one, two, three and four'
q
q = format_words(['one'])  # 'one'
q
q = format_words(['one', '', 'three'])  # 'one and three'
q
q = format_words(['', '', 'three'])  # 'three'
q
q = format_words(['one', 'two', ''])  # 'one and two'
q
q = format_words([])  # ''
q
q = format_words(None)  # ''
q
q = format_words([''])  # ''
q
