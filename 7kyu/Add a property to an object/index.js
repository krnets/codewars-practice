// 7kyu - Add a property to an object

/* Write a function that adds a named property to an object. It must be possible to set the property to a new value. 
If the property already exists on the object, and error should be thrown. */

function addProperty(obj, prop, value) {
    if (obj.hasOwnProperty(prop)) {
        throw Error('property already exists')
    } else {
        obj[prop] = value
    }
    return obj
}

obj = {};
obj
q = addProperty(obj, "name", "Palle")
q
// it("Should set the value of the property", function() {
q = obj.name === "Palle"
q
obj
// it("Should allow setting the new property to another value", function() {
obj.name = "Dylan";
obj
q = obj.name === "Dylan"
q
obj
// it("Should throw an error if the property already exists", function() {
q = addProperty(obj, "name", "Palle");
q
obj