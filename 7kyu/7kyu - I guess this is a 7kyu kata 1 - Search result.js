// 7kyu - I guess this is a 7kyu kata #1: Search result

/* You are using a search engine and type some keywords. For the sake of simplicity, 
we simplify all the keywords into one letter. For example, "abc" represents three keywords: a, b and c. 
We have a lot of search results, please pick out the results that contain all the keywords.

keywords="abc", searchResult=["ab","abc","abcd","bcd"]
You should return: ["abc","abcd"]

Key words can have different order, also may not be continuous and You don't need to sort them out or to remove the same result:

keywords="abc", 
searchResult=["ab","cba","abc","axbxc","ddd","abc","cxab","aabbcc"]
You should return: ["cba","abc","axbxc","abc","cxab","aabbcc"]

Key words may contains uppercase letters:

keywords="Yes", 
searchResult=["yes","Yes","Yeah","Yestoday"]
You should return: ["Yes","Yestoday"]

Complete function finalResult that accepts two arguments keywords and searchResult, 
return all valid results that contains all keywords.

Argument keywords is always a string that contains uppercase or lowercase letters; 
Argument searchResult is always a string array that contains any strings. */

const finalResult = (keywords, searchResult) => searchResult.filter(x => [...keywords].every(y => x.includes(y)))

q = finalResult("abc", ["ab", "abc", "abcd", "bcd"]) // ["abc","abcd"]
q
q = finalResult("abc", ["ab", "cba", "abc", "axbxc", "ddd", "abc", "cxab", "aabbcc"]) // ["cba","abc","axbxc","abc","cxab","aabbcc"]
q
q = finalResult("Yes", ["yes", "Yes", "Yeah", "Yestoday"]) // ["Yes","Yestoday"]
q