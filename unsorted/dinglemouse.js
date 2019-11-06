class Dinglemouse {
    constructor() {
        this.name = this.age = this.sex = 0
    }
    setAge(age) {
        this.age = age
        return this
    }
    setSex(sex) {
        this.sex = sex
        return this
    }
    setName(name) {
        this.name = name
        return this
    }
    hello() {
        return `Hello. My name is ${this.name}. I am ${this.age}. I am ${this.sex == 'M' ? "male" : "female"}.`
    }}

dm = new Dinglemouse().setName("Bob").setAge(27).setSex('M')
dm
q = dm.hello()
q
//         let expected = "Hello. My name is Bob. I am 27. I am male."
//         doTest(expected, dm.hello())
//     })

//     it("test27MaleBob", function(){
dm = new Dinglemouse().setAge(27).setSex('M').setName("Bob")
dm
q = dm.hello()
q
//         let expected = "Hello. I am 27. I am male. My name is Bob."
//         doTest(expected, dm.hello())
//     })

//     it("testAliceFemale", function(){
//         let dm = new Dinglemouse().setName("Alice").setSex('F')
//         let expected = "Hello. My name is Alice. I am female."
//         doTest(expected, dm.hello())
//     })

//     it("testBatman", function(){
//         let dm = new Dinglemouse().setName("Batman")
//         let expected = "Hello. My name is Batman."
//         doTest(expected, dm.hello())
//     })
// })