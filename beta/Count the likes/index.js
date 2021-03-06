// Beta - Count the likes

/* Your grandfather criticises your overuse of the word 'like', claiming that it makes up more than 
5% of the total words you speak.

You argue that it is much lower than this and so to settle the debate, you have been fitted with a 
recorder that stores every word you say as a string in an array.

Your task is to make an algorithm that returns true if 'like' accounts for more than 5% of words 
in the array, otherwise false (if no words are spoken, return false also).

evalLikes(['I','am','sooo','like','tired']) // ==> true;
evalLikes(['THIS','IS','LIKE','TERRIBLE']) // ==> true;
evalLikes(['likely','story']) // ==> false;

Your solution must be case-insensitive but you do not need to worry about punctuation (the device 
you have been fitted with automatically filters this out). */

// const evalLikes = words => words.filter(v => /^like$/i.test(v)).length / words.length > 0.05

const evalLikes = words => words.filter(v => v.toLowerCase() == 'like').length / words.length > 0.05

q = evalLikes(['today', 'was', 'so', 'like', 'awesome']) // true
q
q = evalLikes(['yesterday', 'was', 'even', 'ummm', 'better']) // false
q