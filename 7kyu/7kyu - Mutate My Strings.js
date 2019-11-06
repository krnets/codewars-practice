// 7kyu - Mutate My Strings

//  bubble gum
//  tubble gum
//  ^
//  tubble gum
//  turble gum
//    ^
//  turble gum
//  turtle gum
//     ^
//  turtle gum
//  turtle hum
//         ^
//  turtle hum
//  turtle ham
//          ^

function mutateMyStrings(stringOne, stringTwo) {
    let array = [stringOne]
    for (let i = 0; i < stringOne.length; i++)
        if (stringOne[i] != stringTwo[i])
            array.push(stringTwo.slice(0, i + 1) + stringOne.slice(i + 1))
    return array.join('\n') + '\n'
}

q = mutateMyStrings('bubble gum', 'turtle ham')
// 'bubble gum\ntubble gum\nturble gum\nturtle gum\nturtle hum\nturtle ham\n');
q