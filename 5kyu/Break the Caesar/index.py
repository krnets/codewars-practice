# 5kyu - Break the Caesar!

""" The Caesar cipher is a notorious (and notoriously simple) algorithm for encrypting a message: 
each letter is shifted a certain constant number of places in the alphabet. 

For example, applying a shift of 5 to the string "Hello, world!" yields "Mjqqt, btwqi!", which is jibberish.

In this kata, your task is to decrypt Caesar-encrypted messages using nothing but your wits, your computer, 
and a set of the 1000 (plus a few) most common words in English in lowercase (made available to you as a 
preloaded variable named WORDS, which you may use in your code as if you had defined it yourself).
Given a message, your function must return the most likely shift value as an integer.

A few hints:

    Be wary of punctuation
    Shift values may not be higher than 25 """

WORDS = {'speak', 'floor', 'so', 'took', 'tall', 'trip', 'supply', 'chief', 'yard', 'town', 'block', 'pitch', 'example', 'cow', 'hurry', 'beat', 'whole', 'blue', 'plural', 'truck', 'mean', 'but', 'lazy', 'she', 'yet', 'slave', 'day', 'war', 'mine', 'miss', 'slow', 'quart', 'bar', 'stead', 'east', 'north', 'race', 'hit', 'if', 'was', 'heard', 'hot', 'bit', 'design', 'fill', 'think', 'a', 'collect', 'count', 'able', 'early', 'require', 'ring', 'only', 'live', 'doctor', 'through', 'talk', 'certain', 'wing', 'four', 'thing', 'air', 'degree', 'eight', 'silver', 'track', 'board', 'machine', 'can', 'multiply', 'those', 'experiment', 'hold', 'led', 'most', 'river', 'ease', 'step', 'better', 'store', 'thick', 'exercise', 'hope', 'me', 'gone', 'year', 'friend', 'last', 'finish', 'broke', 'sentence', 'while', 'piece', 'yellow', 'meant', 'final', 'segment', 'bad', 'out', 'prepare', 'excite', 'include', 'temperature', 'woman', 'shop', 'valley', 'afraid', 'pull', 'sit', 'meat', 'dog', 'wrote', 'small', 'grand', 'enemy', 'car', 'add', 'send', 'ready', 'cook', 'pose', 'pattern', 'consonant', 'case', 'month', 'kept', 'produce', 'meet', 'head', 'rise', 'size', 'measure', 'solution', 'major', 'planet', 'wood', 'island', 'common', 'hair', 'feet', 'settle', 'said', 'coast', 'rub', 'fun', 'foot', 'lead', 'question', 'my', 'effect', 'move', 'method', 'indicate', 'to', 'shoe', 'caught', 'column', 'behind', 'wheel', 'call', 'figure', 'who', 'tire', 'blood', 'heart', 'gun', 'west', 'summer', 'search', 'too', 'tree', 'might', 'speech', 'drink', 'part', 'fraction', 'process', 'receive', 'seven', 'raise', 'train', 'operate', 'minute', 'roll', 'history', 'flat', 'at', 'time', 'product', 'sight', 'still', 'cover', 'ice', 'season', 'arm', 'high', 'between', 'string', 'thousand', 'pair', 'dear', 'remember', 'work', 'press', 'especially', 'path', 'corn', 'jump', 'division', 'farm', 'ten', 'quotient', 'hear', 'such', 'family', 'steam', 'interest', 'support', 'consider', 'white', 'believe', 'cool', 'real', 'fly', 'bank', 'bat', 'pound', 'rather', 'done', 'fruit', 'glad', 'all', 'oxygen', 'print', 'fast', 'black', 'show', 'gather', 'rich', 'object', 'mother', 'milk', 'swim', 'animal', 'event', 'least', 'table', 'imagine', 'notice', 'field', 'after', 'street', 'among', 'bring', 'check', 'atom', 'always', 'begin', 'few', 'cost', 'may', 'shape', 'insect', 'complete', 'total', 'the', 'money', 'saw', 'before', 'box', 'south', 'had', 'big', 'buy', 'skill', 'matter', 'see', 'under', 'leg', 'third', 'though', 'radio', 'ago', 'state', 'camp', 'is', 'went', 'try', 'forward', 'provide', 'safe', 'them', 'repeat', 'your', 'morning', 'crowd', 'clear', 'fire', 'walk', 'hole', 'job', 'wind', 'his', 'by', 'color', 'sense', 'get', 'build', 'system', 'loud', 'instant', 'view', 'success', 'what', 'deep', 'bed', 'group', 'thin', 'made', 'student', 'side', 'open', 'wall', 'soft', 'together', 'book', 'wish', 'corner', 'name', 'he', 'oil', 'sail', 'death', 'us', 'divide', 'ship', 'never', 'develop', 'poem', 'age', 'original', 'act', 'full', 'edge', 'close', 'trouble', 'electric', 'grew', 'school', 'every', "don't", 'fresh', 'ground', 'observe', 'this', 'winter', 'life', 'girl', 'wtf', 'guess', 'famous', 'stone', 'short', 'shine', 'young', 'been', 'self', 'story', 'guide', 'let', 'felt', 'during', 'works', 'locate', 'captain', 'horse', 'root', 'sea', 'put', 'dry', 'choose', 'center', 'from', 'lift', 'chick', 'kill', 'each', 'rail', 'down', 'please', 'use', 'wire', 'yes', 'nature', 'form', 'pretty', 'music', 'opposite', 'area', 'place', 'house', 'take', 'warm', 'end', 'suggest', 'suffix', 'condition', 'six', 'stay', 'old', 'rule', 'subtract', 'carry', 'seed', 'note', 'soon', 'whose', 'strong', 'watch', 'magnet', 'just', 'spot', 'have', 'run', 'either', 'person', 'quiet', 'son', 'or', 'whether', 'drive', 'order', 'seat', 'garden', 'great', 'control', "won't", 'liquid', 'much', 'thought', 'modern', 'stream', 'bought', 'did', 'win', 'current', 'same', 'busy', 'mountain', 'enough', 'that', 'lady', 'ask', 'once', 'bread', 'sister', 'tiny', 'second', 'fig', 'follow', 'against', 'energy', 'spread', 'lone', 'blow', 'course', 'first', 'than', 'wave', 'forest', 'particular', 'sent', 'brother', 'round', 'type', 'soldier', 'colony', 'cut', 'silent', 'sun', 'sky', 'poor', 'paragraph', 'plain', 'told', 'continue', 'hard', 'eye', 'card', 'unit', 'special', 'natural', 'line', 'human', 'look', 'feed', 'represent', 'create', 'voice', 'over', 'teach', 'smile', 'does', 'mount', 'branch', 'chord', 'symbol', 'reason', 'glass', 'people', 'began', 'office', 'world', 'subject', 'cold', 'continent', 'more', 'go', 'probable', 'say', 'body', 'hundred', 'section', 'correct', 'engine', 'suit', 'weight', 'night', 'rain', 'on', 'bell', 'master', 'grow', 'long', 'ball', 'sing', 'lost', 'team', 'claim', 'gas', 'cross', 'sure', 'you', 'hour', 'now', 'gray', 'metal', 'protect', 'prove', 'mark', 'numeral', 'serve', 'grass', 'describe', 'ear', 'decide', 'chart', 'nose', 'select', 'appear', 'fox', 'fight', 'slip', 'hello', 'set', 'finger', 'keep', 'moment', 'spend', 'shout', 'care', 'laugh', 'learn', 'some', 'circle', 'change', 'both', 'vary', 'score', 'find', 'man', 'nation', 'fall', 'dance', 'rope', 'cent', 'simple', 'game', 'shoulder', 'post', 'force', 'point', 'trade', 'sign', 'quick', 'stick', 'of', 'tell', 'lake', 'proper', 'fear', 'light', 'log', 'him', 'flower', 'happen', 'market', 'equal', 'anger', 'found', 'jumps', 'necessary', 'start', 'plant', 'are', 'in', 'port', 'they', 'sleep', 'fact', 'about', 'should', 'wild', 'organ', 'sand', 'eat', 'brought', 'region', 'king', 'surprise', 'danger', 'country', 'separate', 'straight', 'speed', 'molecule', 'chair', 'one', 'lot', 'wash', 'hunt', 'boat', 'write', 'stand', 'come', 'ran', 'enter', 'shore', 'nine', 'egg', 'position', 'inch', 'smell', 'window', 'other', 'parent', 'copy', 'period', 'road', 'visit', 'class', 'there', 'word', 'share', 'melody', 'main', 'crop', 'surface', 'want', 'again', 'sugar', 'we', 'make', 'verb', 'substance', 'left', 'when', 'true', 'baby', 'brown', 'food', 'up', 'discuss', 'rose', 'salt', 'hill', 'stood', 'decimal', 'law', 'back', 'for', 'page', 'term', 'iron', 'length', 'character', 'neck', 'also', 'clock', 'triangle', 'ocean', 'room', 'invent', 'dead', 'tail', 'element', 'above', 'happy', 'else', 'gold', 'like', 'populate', 'touch', 'sheet', 'agree', 'why', 'similar', 'kind', 'general', 'am', 'science', 'near', 'chance', 'problem', 'catch', 'gentle', 'red', 'snow', 'draw', 'basic', 'cell', 'huge', 'instrument', 'art', 'fit', 'cotton', 'mix', 'tool', 'experience', 'little', 'far', 'home', 'clothe', 'their', 'do', 'answer', 'favor', 'mass', 'dark', 'contain', 'century', 'any', 'stretch', 'dress', 'vowel', 'break', 'several', 'bear', 'low', 'an', 'range', 'sharp', 'will', 'fish', 'cry', 'bone', 'mouth', 'practice', 'tube', 'best', 'duck', 'picture', 'usual', 'paint', 'cloud', 'which', 'need', 'no', 'drop', 'wonder', 'many', 'syllable', 'star', 'connect', 'expect', 'wear', 'possible', 'very', 'front', 'station', 'single', 'water', 'past', 'large', 'arrive', 'stop', 'apple', 'then', 'held', 'give', 'her', 'soil', 'late', 'direct', 'base', 'hat', 'turn', 'value', 'earth', 'land', 'neighbor', 'five', 'ride', 'broad', 'would', 'skin', 'shell', 'next', 'beauty', 'bottom', 'until', 'map', 'join', 'study', 'pick', 'space', 'arrange', 'push', 'heavy', 'oh', 'reply', 'way', 'save', 'paper', 'sell', 'must', 'often', 'even', 'city', 'play', 'key', 'wait', 'language', 'exact', 'two', 'gave', 'spoke', 'idea', 'children', 'heat', 'joy', 'read', 'off', 'clean', 'help', 'sound', 'came', 'song', 'quite', 'motion', 'reach', 'property', 'burn', 'well', 'flow', 'shall', 'born', 'pass', 'week', 'rest', 'how', 'die', 'industry', 'equate', 'right', 'except', 'middle', 'depend', 'mile', 'here', 'new', 'spell', 'pay', 'sudden', 'deal', 'scale', 'throw', 'tone', 'climb', 'seem', 'determine', 'mind', 'sat', 'knew', 'plan', 'square', 'noon', 'phrase', 'written', 'differ', 'be', 'wrong', 'these', 'rock', 'offer', 'village', 'bird', 'where', 'cat', 'result', 'cause', 'occur', 'wife', 'weather', 'thank', 'dictionary', 'million', 'test', 'got', 'power', 'fell', 'govern', 'bright', 'band', 'our', 'ever', 'thus', 'green', 'strange', 'dollar', 'nothing', 'list', 'love', 'feel', 'less', 'child', 'row', 'and', 'fair', 'plane', 'evening', 'boy', 'compare', 'men', 'tie', 'free', 'noise', 'know', 'lay', 'perhaps', 'face', 'material', 'good', 'double', 'noun', 'company', 'since', 'party', 'letter', 'solve', 'door', 'crease', 'top', 'desert', 'travel', 'distant', 'moon', 'father', 'fine', 'allow', 'twenty', 'could', 'dad', 'nor', 'fat', 'spring', 'difficult', 'coat', 'as', 'were', 'it', 'level', 'with', 'number', 'three', 'toward', 'capital', 'record', 'has', 'teeth', 'hand', 'lie', 'wide', 'listen', 'own', 'charge', 'present', 'match', 'half', 'steel', 'leave', 'women', 'dream'}

from re import sub
from string import ascii_lowercase as abc

def break_caesar(message):
    found_words = []
    message = sub('[^\w\s]+', '', message.lower())

    for i in range(26):
        rotated = message.translate(str.maketrans(abc, abc[-i:] + abc[:-i]))
        found_words.append(sum(1 for w in rotated.split() if w in WORDS))

    return found_words.index(max(found_words))

q = break_caesar("DAM? DAM! DAM.") # 7
q
q = break_caesar("Mjqqt, btwqi!") # 5
q
q = break_caesar("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.") # 13
q