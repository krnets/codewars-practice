### "com", "gov", "org" first

Write a code that orders collection of Uris based on it's domain next way that it will returns fisrt Uris with domain "com", "gov", "org" (in alphabetical order of their domains) and then all other Uris ordered in alphabetical order of their domains In addition to that

* content of Uri should not be changed,
* other part of Uri doesn't affect sorting. (uris "c.com","b.com","a.com" can be placed in any order inside their group, so both "c.com","b.com","a.com" and "a.com","c.com","b.com" are correct, till they are stand before *.org)

e.g.
```
"http://www.google.en/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"

should be sorted into

"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.en/?x=jsdfkj"

