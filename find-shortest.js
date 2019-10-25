// Test.describe("Example tests",_=>{
// Test.assertEquals(findShort("bitcoin take over the world maybe who knows perhaps"), 3);
// Test.assertEquals(findShort("turns out random test cases are easier than writing out basic ones"), 3); 
// });


const findShort = (str) => str.split(' ').reduce((shortest, current) => {
    return current.length < shortest.length ? current : shortest;
}).length



let x = findShort("bitcoin take over the world maybe who knows perhaps")
x = findShort("turns out random test cases are easier than writing out basic ones")
x