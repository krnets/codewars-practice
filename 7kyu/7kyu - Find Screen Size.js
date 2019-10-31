function findScreenHeight(width, ratio) {
    return width + "x" + width / eval(ratio.slice(":").replace(/:/gi, '\/'))
}

q = findScreenHeight(1024,"4:3") // "1024x768")
q
q = findScreenHeight(1280,"16:9") // "1280x720"
q
q = findScreenHeight(3840,"32:9") // "3840x1080"
q

// describe("test4:3", function() {
//     it("should return 1024x768", function(){
//         Test.assertEquals(findScreenHeight(1024,"4:3"), "1024x768");
//     });
// });
// describe("test16:9", function() {
//     it("should return 1280x720", function(){
//         Test.assertEquals(findScreenHeight(1280,"16:9"), "1280x720");
//     });
// });
// describe("test32:9", function() {
//     it("should return 3840x1080", function(){
//         Test.assertEquals(findScreenHeight(3840,"32:9"), "3840x1080");
//     });
// });