const smallEnough = (a, limit) => a.every(value => value <= limit)

q = smallEnough([66, 101], 200)  // true
q
q = smallEnough([78, 117, 110, 99, 104, 117, 107, 115], 100) // false
q
q = smallEnough([101, 45, 75, 105, 99, 107], 107) // true
q
q = smallEnough([80, 117, 115, 104, 45, 85, 112, 115], 120) // true
q