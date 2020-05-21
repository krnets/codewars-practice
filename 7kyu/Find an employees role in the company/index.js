// 7kyu - Find an employees role in the company

/* You get a new job working for Eggman Movers. Your first task is to write a method that will allow the admin staff 
to enter a person’s name and return what that person's role is in the company.

You will be given an array of object literals holding the current employees of the company. 
You code must find the employee with the matching firstName and lastName and then return the role 
for that employee or if no employee is not found it should return "Does not work here!"

The array is preloaded and can be referenced using the variable employees ($employees in Ruby). It uses the following structure.

let employees = [ {firstName: "Dipper", lastName: "Pines", role: "Boss"}, ...... ]

There are no duplicate names in the array and the name passed in will be a single string with a space between 
the first and last name i.e. Jane Doe or just a name. */


function findEmployeesRole(name) {
    [first, last] = name.split(' ')
    for (const key of employees)
        if (key.firstName == first && key.lastName == last)
            return key.role
    return 'Does not work here!'
}

// function findEmployeesRole(name) {
//     let [employee] = employees.filter(x => `${x.firstName} ${x.lastName}` === name);
//     return employee ? employee.role : "Does not work here!";
// }

// const findEmployeesRole = n => (n = employees.find(e => `${e.firstName} ${e.lastName}` === n)) ? n.role : 'Does not work here!';

let employees = [{ firstName: "Morty", lastName: "Smith", role: "Truck Driver" }, { firstName: "Anna", lastName: "Bell", role: "Admin"}]
q = findEmployeesRole("Dipper Pines") // "Does not work here!"
q
q = findEmployeesRole("Morty Smith") // "Truck Driver"
q
q = findEmployeesRole("Anna Bell") // "Admin"
q