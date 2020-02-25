// Beta - Transform an array into a string

const transform = array => array.map(String).join('')

q = transform(["BmX", false, 784]) // "BmXfalse784"
q
q = transform([4, -56, true, "box"]) // "4-56truebox"
q