# 5kyu - The Hashtag Generator

""" The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false """

# def generate_hashtag(s):
#     hashtag = '#' + ''.join(word.title() for word in s.split())
#     return hashtag if s and len(hashtag) <= 140 else False

def generate_hashtag(s):
    hashtag = '#' + ''.join(s.title().replace(' ', ''))
    return hashtag if s and len(hashtag) <= 140 else False


q = generate_hashtag(''), False # 'Expected an empty string to return False'
q
q = generate_hashtag('Do We have A Hashtag')[0], '#' # 'Expeted a Hashtag (#) at the beginning.'
q
q = generate_hashtag('Codewars'), '#Codewars' # 'Should handle a single word.'
q
q = generate_hashtag('Codewars      '), '#Codewars' # 'Should handle trailing whitespace.'
q
q = generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice' # 'Should remove spaces.'
q
q = generate_hashtag('codewars is nice'), '#CodewarsIsNice' # 'Should capitalize first letters of words.'
q
q = generate_hashtag('CodeWars is nice'), '#CodewarsIsNice' # 'Should capitalize all letters of words - all lower case but the first.'
q
q = generate_hashtag('c i n'), '#CIN' # 'Should capitalize first letters of words even when single letters.'
q
q = generate_hashtag('codewars  is  nice'), '#CodewarsIsNice' # 'Should deal with unnecessary middle spaces.'
q
q = generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False # 'Should return False if the final word is longer than 140 chars.'
q