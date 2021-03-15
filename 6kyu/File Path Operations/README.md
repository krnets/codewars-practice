### File Path Operations

This kata requires you to write an object that receives a file path and does operations on it.

The purpose of this kata is to use string parsing, so you're not supposed to import external libraries.

Testing:
```c#
FileMaster FM = new FileMaster("/Users/person1/Pictures/house.png");
FM.extension(); // output: "png"
FM.filename(); // output: "house"
FM.dirpath(); // output: "/Users/person1/Pictures/"
```
