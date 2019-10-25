function redacted(doc1, doc2) {
    for (let i = 0; i < doc1.length; i++) {
        if (doc1[i] == 'X' && doc2[i] == '\n' || doc1[i] != 'X' && doc1[i] != doc2[i])
            return false;
    }
    return doc1.length === doc2.length
}


// var doc1 = "TOP SECRET:\nThe missile launch code for Sunday XXXXXXXXXX is:\nXXXXXXXXXXXXXXXXX";
// var doc2 = "TOP SECRET:\nThe missile launch code for Sunday 5th August is:\n7-ZERO-8X-ALPHA-1";
// q = redacted(doc1, doc2)
// q
// var doc1 = "The name of the mole is Professor XXXXX";
// var doc2 = "The name of the mole is Professor Dinglemouse";
var doc1 = "xxxxxxxx xxxxxxx xxxxxxxxxxxxxxxxxxx\nxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxx xxxxxxxxxxxxx xxxxx";
var doc2 = "area-51. medical report. 23/oct/1969\ne.t. subject 4 was given an asprin after reporting sick for duty today";
q = redacted(doc1, doc2)
q

// describe("SampleTests", function(){
//     it("ex1", function(){
//         var doc1 = "TOP SECRET:\nThe missile launch code for Sunday XXXXXXXXXX is:\nXXXXXXXXXXXXXXXXX";
//         var doc2 = "TOP SECRET:\nThe missile launch code for Sunday 5th August is:\n7-ZERO-8X-ALPHA-1";
//         Test.assertEquals(redacted(doc1, doc2), true);
//     });
//     it("ex2", function(){
//         var doc1 = "The name of the mole is Professor XXXXX";
//         var doc2 = "The name of the mole is Professor Dinglemouse";
//         Test.assertEquals(redacted(doc1, doc2), false);
//     });
//     it("ex3", function(){
//         var doc1 = "xxxxxxxx xxxxxxx xxxxxxxxxxxxxxxxxxx\nxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxx xxxxxxxxxxxxx xxxxx";
//         var doc2 = "area-51. medical report. 23/oct/1969\ne.t. subject 4 was given an asprin after reporting sick for duty today";
//         Test.assertEquals(redacted(doc1, doc2), true);
//     });
// });