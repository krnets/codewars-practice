// 7kyu - Simple Fun 152: Invite More Women

const inviteMoreWomen = L => L.reduce((total, curr) => total + curr)  > 0

q = inviteMoreWomen([1, -1, 1])  // true
q
q = inviteMoreWomen([1, 1, 1])  // true
q
q = inviteMoreWomen([-1, -1, -1])  // false
q
q = inviteMoreWomen([1, -1])  // false
q