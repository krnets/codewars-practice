# 6kyu - Count words

""" Kate likes to count words in text blocks. 
By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:

Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp. 
contains "words" ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']

Kate doesn't like some of words and doesn't count them. 
Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

Today Kate's too lazy and have decided to teach her computer to count "words" for her.

Input: "Hello there, little user5453 374 ())$."
Output: 4

Input: "I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. 
My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, 
and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. 
Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop 
smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything."
Output: 112 """

import re

def word_count(s):
    exclude = ["a", "the", "on", "at", "of", "upon", "in", "as"]
    return len([word for word in re.sub(r"[^a-z]", " ", s.lower()).split() if word not in exclude])


q = word_count("hello there")  # 2
q
q = word_count("hello there and a hi")  # 4
q
q = word_count("I'd like to say goodbye")  # 6
q
q = word_count("Slow-moving user6463 has been here")  # 6
q
q = word_count("%^&abc!@# wer45tre")  # 3
q
q = word_count("abc123abc123abc")  # 3
q
q = word_count("Really2374239847 long ^&#$&(*@# sequence")  # 3
q

long_text = """
I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.
"""

q = word_count(long_text)  # 112
q
