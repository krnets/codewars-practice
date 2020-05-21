// 7kyu - Find Shortest Word

const findShort = (str) => str.split(' ').reduce((shortest, current) => {
    return current.length < shortest.length ? current : shortest;
}).length



x = findShort("bitcoin take over the world maybe who knows perhaps")
q
x = findShort("turns out random test cases are easier than writing out basic ones")
x