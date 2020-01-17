// 8kyu - Color Ghost

/* Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated */

class Ghost {
    constructor() {
        this.color = ['white', 'yellow', 'purple', 'red'][Math.floor(Math.random() * 4)]
    }
}

ghost = new Ghost();
q = ghost.color //=> "white" or "yellow" or "purple" or "red"
q
q = Math.random() * 4
q