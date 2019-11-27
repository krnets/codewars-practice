// 6kyu - Character limits: How long is your piece of string?

/* Write Cara a function charCheck() with the arguments:

    "text": a string containing Cara's answer for the question
    "max": a number equal to the maximum number of characters allowed in the answer
    "spaces": a boolean which is True if spaces are included in the character count and False if they are not

The function charCheck() should return an array: [True, "Answer"] , 
where "Answer" is equal to the original text, if Cara's answer is short enough.
If her answer "text" is too long, return an array: [False, "Answer"]. 
The second element should be the original "text" string truncated to the length of the limit.
When the "spaces" argument is False, you should remove the spaces from the "Answer". */


// function charCheck(text, max, spaces) {
//     if (!spaces) text = text.replace(/\s/g, '')
//     return (text.length <= max) ? [true, text] : [false, text.slice(0, max)]
// }

function charCheck(text, max, spaces) {
    if (!spaces) text = text.replace(/\s/g, '')
    return [text.length <= max, text.slice(0, max)]
}

q = charCheck("I am applying for the role of Base Manager on Titan.", 60, true)
// [true, "I am applying for the role of Base Manager on Titan."]
// "The input text length is below the character limit."
q

q = charCheck("I am looking to relocate to the vicinity of Saturn for family reasons.", 70, true)
// [true, "I am looking to relocate to the vicinity of Saturn for family reasons."]
// "The input text length is below the character limit.
q

q = charCheck("As Deputy Base Manager on Phobos for five Martian years, I have significant relevant experience.", 90, false)
// [true, "AsDeputyBaseManageronPhobosforfiveMartianyears,Ihavesignificantrelevantexperience."]
// "Did you remove the spaces?"
q

q = charCheck("A challenging career moment came with the rapid depletion of water supplies on Phobos.", 80, false)
// [true, "AchallengingcareermomentcamewiththerapiddepletionofwatersuppliesonPhobos."]
// "Did you remove the spaces?"
q

q = charCheck("Despite what some have suggested, this had nothing to do with the decorative fountains I had installed in my private quarters.", 100, false)
// [true, "Despite what some have suggested, this had nothing to do with the decorative fountains I had installed in my private quarters."]
// "The input text length is above the character limit."
q

q = charCheck("Anyway what sort of society would we be if a Deputy Base Manager couldn't allow herself a few luxuries?", 70, false)
// [true, "Anyway what sort of society would we be if a Deputy Base Manager couldn't allow herself a few luxuries?"]
// "The input text length is above the character limit.
q

q = charCheck("I swiftly resolved the situation with base-wide water rationing.", 60, true)
// [true, "I swiftly resolved the situation with base-wide water rationing."]
// "Did you count the spaces as characters?"
q

q = charCheck("After four Martian weeks of not washing, several colonists complained of the smell.", 80, true)
// [true, "After four Martian weeks of not washing, several colonists complained of the smell."]
// "Did you count the spaces as characters?
q

q = charCheck("But, as I pointed out, anyone complaining about standing downwind was lying. There was no wind.", 75, true)
// [false, "But, as I pointed out, anyone complaining about standing downwind was lying"]
q

q = charCheck("I have no notice period on Phobos. I can start immediately.", 50, true)
// [false, "I have no notice period on Phobos. I can start imm"]
// "Your array should include a shortened version of the original text.
q
