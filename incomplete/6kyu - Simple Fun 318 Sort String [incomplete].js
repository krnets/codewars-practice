// 6kyu - Simple Fun 318 Sort String

function sortString(s) {
    return [...s].sort((a,b) => a.localeCompare(b))
}

q = sortString("cba"),"abc"
q
q = sortString("Cba"),"abC"
q
q = sortString("cCBbAa"),"AaBbcC"
q
q = sortString("c b a"),"a b c"
q
q = sortString("-c--b--a-"),"-a--b--c-"
q
q = sortString("Codewars"),"aCdeorsw"
q
q = sortString(" MkWD{RB=//k-^ J@,xH Vfi uAz+$ kV _[ }a!}%pSBwn !kKB (b  q PQF +}wS  .kfU r wFNEs#NsR UVMdG")
// " AaBB{Bb=//D-^ d@,Ef FfF GHi+$ Jk _[ }k!}%kkKkM !MnN (N  p PqQ +}Rr  .RSS s suUUV#VVW wwwxz")
q
    