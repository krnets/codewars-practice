function checkExam(array1, array2) {
    let score = 0
    for (let i = 0; i < array1.length; i++) {
        if (array1[i] == array2[i]) {
            score += 4
        } else if (array2[i] == '') {
            continue
        } else {
            score--
        }
    }
    return score < 0 ? 0 : score
}

q = checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) // 6);
q
q = checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) // 7);
q
q = checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) // 16);
q
q = checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) // 0);  
q