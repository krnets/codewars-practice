function wordscore(word) {
    let letterPoints = {"a": 1,"b": 3,"c": 3,"d": 2,"e": 1,"f": 4,"g": 2,"h": 4,"i": 1,"j": 8,"k": 5,"l": 1,"m": 3,"n": 1,"o": 1,"p": 3,"q": 10,"r": 1,"s": 1,"t": 1,"u": 1,"v": 4,"w": 4,"x": 8,"y": 4,"z": 10}
    let result = 0
    
    for (let i of word)
        result += letterPoints[i]

    return word.length == 7 ? 
          (result *= word.length) + 50 : 
          (result *= word.length)
}

// let result = word.split('').reduce((total, curr) => total + letterPoints[curr], 0) * word.length

q = wordscore('great') // 30, "The expected score for 'great' was 30. "
q
q = wordscore('deceive') // 141, "'deceive' is seven letters, the expected result was 141"
q
q = wordscore('melon') // 35, "The expected score for 'melon' was 35."
q