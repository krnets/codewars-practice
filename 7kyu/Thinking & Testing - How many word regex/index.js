function testit(str) {
    return (str.match(/w.*?o.*?r.*?d/gi) || []).length
}

//How many "word" in these sentence? Use your fingers and toes to count
q = testit("word") // 1, ""
q
q = testit("hello world") // 1, ""
q
q = testit("I love codewars.") // 0 ""
q
q = testit("My cat waiting for a dog.") // 1 ""
q
q = testit("We often read book, a word hidden in the book.") // 2  ""
q
q = testit("When you in order to do something by a wrong way, your heart will missed somewhere.") // 2 ""
q
q = testit("This sentence have one word.") // 1 ""
q
q = testit("This sentence have two word, not one word.") // 2 ""
q
q = testit("One word + one word = three word ;-)") // 3 ""
q
q = testit("Can you find more word for me?") // 1 ""
q
//click "Submit" try more testcase...