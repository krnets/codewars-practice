// function howManyDalmatians(number) {
//     var dogs = ["Hardly any", 
//                 "More than a handful!", 
//                 "Woah that's a lot of dogs!", 
//                 "101 DALMATIANS!!!"];
        
//     return number <= 10 ? dogs[0] 
//          : number <= 50 ? dogs[1] 
//          : number == 101 ? dogs[3] 
//          : dogs[2]
// }

function howManyDalmatians(number) {
    
    return number == 101 ? "101 DALMATIANS!!" :
           number <= 10  ? "Hardly any" :
           number <= 50  ? "More than a handful" :
           "Woah that's a lot of dogs!"
}

q = howManyDalmatians(1)
q

q = howManyDalmatians(26) // "More than a handful!");
q

q = howManyDalmatians(8) //"Hardly any");
q

q = howManyDalmatians(14) // "More than a handful!");
q

q = howManyDalmatians(80) // "Woah that's a lot of dogs!");
q

q = howManyDalmatians(100) //, "Woah that's a lot of dogs!");
q

q = howManyDalmatians(101) //, "101 DALMATIANS!!!");
q