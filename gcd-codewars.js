// const mygcd = (x,y) => x % y == 0 ? y : mygcd(y, x % y)
const mygcd = (x,y) => y ? mygcd(y, x % y) : x


q = mygcd(30,12) // 6
q
q = mygcd(8,9) // 1
q
q = mygcd(1,1)
q