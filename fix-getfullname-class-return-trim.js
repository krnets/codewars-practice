class Dinglemouse {

    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName
    }

    getFullName() {
        return (this.firstName + ' ' + this.lastName).trim()
        // return this.firstName && this.lastName ?
        //        this.firstName + ' ' + this.lastName :
        //        this.firstName ? this.firstName : this.lastName
    }
}


q = new Dinglemouse("Clint", "Eastwood").getFullName() // "Clint Eastwood");
q