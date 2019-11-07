// 7kyu - Friend or Foe

const friend = friends => friends.filter(v => v.length == 4)


q = friend(["Ryan", "Kieran", "Mark"]) // ["Ryan", "Mark"]
q
q = friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) // ["Ryan"]
q
q = friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) // ["Jimm", "Cari", "aret"]
q
q = friend(["Love", "Your", "Face", "1"]) // ["Love", "Your", "Face"]
q