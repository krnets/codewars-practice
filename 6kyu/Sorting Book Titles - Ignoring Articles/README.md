### Sorting Book Titles: Ignoring Articles

When sorting lists of book titles alphabetically, articles (the, an, or a) in the beginning of the title should be ignored, and moved to the end.

For example, given a list that contains A Petition to Magic and Heritage of Deceit, Heritage of Deceit should be sorted before A Petition to Magic.

The remainder of the title should be sorted as if the article was appended to the end of the title.

For example, A Petition to Magic becomes Petition to Magic, A for purposes of sorting, and The Great Gatsby becomes Great Gatsby, The.

Write a method that receives a list of book titles as strings, and returns a new, sorted list, which follows the above rules.

You should not modify the original title. It should be returned as-is in the resulting list.

If null is passed to the method, it should return null. If an empty list is passed, the method should return an empty list.

Note: only exclude articles if they appear in the beginning of the title. For example, if a title happens to include the word The in the middle, that word should not be excluded.

Also, do not exclude articles if the entire title is an article (for example, a book titled simply The should remain The for purposes of sorting).

