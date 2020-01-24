// 7kyu - Greed

/* In my "getQuotes" function, I am trying to extract only the quotes from a string.

getQuotes('"example quote #1" some text "example quote #2"'); 
// should return ["\"example quote #1\"","\"example quote #2\""]

However, my test results are not as expected. can you find out what I did wrong? */

var reg = /".+?"/g

function getQuotes(string) {
    return string.match(reg);
}

q = getQuotes('"Winners never quit and quitters never win." - Vince Lombardi, "My motto is, \'Never quit.\'" - Henry Rollins')
q
// ["\"Winners never quit and quitters never win.\"","\"My motto is, 'Never quit.'\""]