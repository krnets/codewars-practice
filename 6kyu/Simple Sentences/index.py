""" 6kyu - Simple Sentences

Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:

    words;
    commas in the middle;
    multiple periods at the end.

Sentence making rules:

    there must always be a space between words;
    there must not be a space between a comma and word on the left;
    there must always be one and only one period at the end of a sentence.

Example:

make_sentence(['hello', ',', 'my', 'dear']) #  returns 'hello, my dear.' """


# def make_sentences(parts):
#     return '{}.'.format(''.join(' ' + x if x.isalnum() else x for x in parts).strip(' .'))

def make_sentences(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'


q = make_sentences(['hello', 'world']), 'hello world.'
q
q = make_sentences(['Quick', 'brown', 'fox', 'jumped', 'over', 'the',
                    'lazy', 'dog']), 'Quick brown fox jumped over the lazy dog.'
q

q = make_sentences(['hello', ',', 'my', 'dear']), 'hello, my dear.'
q
q = make_sentences(['one', ',', 'two', ',', 'three']), 'one, two, three.'
q
q = make_sentences(['One', ',', 'two', 'two', ',', 'three', 'three', 'three',
                    ',', '4', '4', '4', '4']), 'One, two two, three three three, 4 4 4 4.'
q

q = make_sentences(['hello', 'world', '.']), 'hello world.'
q
q = make_sentences(['Bye', '.']), 'Bye.'
q

q = make_sentences(['hello', 'world', '.', '.', '.']), 'hello world.'
q
q = make_sentences(['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.',
                    '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']), 'The Earth rotates around The Sun in 365 days, I know that.'
q
