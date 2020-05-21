// 6kyu - FIXME: Hello

class Dinglemouse {
    constructor() {
        this.props = {}
    }
    setAge(age) {
        this.props.age = ` I am ${age}.`
        return this
    }
    setSex(sex) {
        this.props.sex = ` I am ${sex == 'M' ? "male" : "female"}.`
        return this
    }
    setName(name) {
        this.props.name = ` My name is ${name}.`
        return this
    }
    hello() {
        return `Hello.` + Object.values(this.props).join('')
    }
}

dm = new Dinglemouse().setName("Batman")
q = dm.hello()
q
// Hello. My name is Batman.

dm = new Dinglemouse().setName("Bob").setAge(27).setSex('M')
q = dm.hello()
q
// Hello. My name is Bob. I am 27. I am male.

dm = new Dinglemouse().setAge(27).setSex('M').setName("Bob")
q = dm.hello()
q
// Hello. I am 27. I am male. My name is Bob.

dm = new Dinglemouse().setName("Alice").setSex('F')
q = dm.hello()
q
// Hello. My name is Alice. I am female.

dm = new Dinglemouse()
q = dm.hello()
q
// Hello.