const cubeOdd = arr => arr.some(isNaN) ? undefined : arr.filter(n => n % 2).reduce((a,b) => a + Math.pow(b, 3), 0)

let assertEquals = (fn, cmp) => fn == cmp
q = cubeOdd([1, 2, 3, 4]) // 28
q
q = assertEquals(cubeOdd([1, 2, 3, 4]), 28);
q
q = assertEquals(cubeOdd([-3, -2, 2, 3]), 0);
q
q = assertEquals(cubeOdd(["a", 12, 9, "z", 42]), undefined);
q
q = cubeOdd(["a", 12, 9, "z", 42])
q
q = cubeOdd([-3, -2, 2, 3]) //, 0);
q