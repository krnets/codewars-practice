### Did you mean ...?

I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term `berr` is more similar to `beer` (1 letter to be replaced) than to `barrel` (3 letters to be changed in total).


Code Examples:
```java
Dictionary fruits = new Dictionary(new String[]{"cherry", "pineapple", "melon", "strawberry", "raspberry"});

fruits.findMostSimilar("strawbery"); // must return "strawberry"
fruits.findMostSimilar("berry"); // must return "cherry"

Dictionary things = new Dictionary(new String[]{"stars", "mars", "wars", "codec", "codewars"});
things.findMostSimilar("coddwars"); // must return "codewars"

Dictionary languages = new Dictionary(new String[]{"javascript", "java", "ruby", "php", "python", "coffeescript"});
languages.findMostSimilar("heaven"); // must return "java"
languages.findMostSimilar("javascript"); // must return "javascript" (same words are obviously the most similar ones)
``` 
.
.
.
``` csharp
var fruits = new Kata(new List<string> { "cherry", "pineapple", "melon", "strawberry", "raspberry" });
fruits.FindMostSimilar("strawbery"); // must return "strawberry"
fruits.FindMostSimilar("berry"); // must return "cherry"

things = new Dictionary(new List<string> { "stars", "mars", "wars", "codec", "codewars" });
things.FindMostSimilar("coddwars"); // must return "codewars"

languages = new Dictionary(new List<string> { "javascript", "java", "ruby", "php", "python", "coffeescript" });
languages.FindMostSimilar("heaven"); // must return "java"
languages.FindMostSimilar("javascript"); // must return "javascript" (same words are obviously the most similar ones)
```

I know, many of you would disagree that Java is more similar to heaven than all the other ones, but in this kata it is ;)

Additional notes:

* there is always exactly one possible correct solution



