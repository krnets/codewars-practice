### Number Shortening Filter

You might be familar with and have used Angular.js. Among other things, it lets you create your own filters that work as functions. 

You can then put these in a page to perform specific data changes, such as shortening a number to display a more concise notation.

In this kata, we will create a function which returns another function (or process, in Ruby) that shortens very long numbers. 

Given an initial array of values replace the Xth power of a given base. 

If the input of the returned function is not a numerical string, it should return the input itself as a string.

Here's an example, which is worth a thousand words:
```js
var filter1 = shortenMethods.ShortenNumberCreator(new string[] { "", "k", "m" }, 1000);
filter1("234324") == "234k";
filter1("98234324") == "98m";
filter1(new int[] { 1,2,3 }) == "1,2,3";

var filter2 = shortenMethods.ShortenNumberCreator(new string[] { "B", "KB", "MB", "GB" }, 1024);
filter2("32") == "32B";
filter2("2100") == "2KB";
filter2("pippi") == "pippi";
```
If you like to test yourself on kata related to actual work and interviews, consider trying this kata where you will build a breadcrumb generator

