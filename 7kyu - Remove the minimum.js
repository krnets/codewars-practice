// 7kyu - Remove the minimum

function removeSmallest(numbers) {
    let low = {
        num: Infinity,
        idx: 0
    }

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < low['num']) {
            low['num'] = numbers[i]
            low['idx'] = i
        }
    }

    return numbers.slice(0, low['idx']).concat(numbers.slice(low['idx'] + 1))

}


q = removeSmallest([11, 12, 30, 14, 52])
q

function removeSmallest_2(numbers) {
    let indexOfMin = numbers.indexOf(Math.min(...numbers));
    return [...numbers.slice(0, indexOfMin), 
            ...numbers.slice(indexOfMin + 1)];
  }


q = removeSmallest_2([11, 2, 3, 41, 52])
q

const removeSmallest_3 = numbers => numbers
        .filter((n,i) => i !== numbers.indexOf(Math.min(...numbers)));

q = removeSmallest_3([113, 21, 36, 41, 59])
q

nb = [113, 21, 36, 41, 59]
q = Math.max(...nb)
q
