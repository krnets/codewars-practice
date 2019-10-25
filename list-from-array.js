function Node(data, next = null) {
    this.data = data
    this.next = next
}

function listFromArray(arr) {
    return [...arr]
}

function length(head) {
    return !head? 0 : length(head.next)
}

q = length(null) // 0);
q
q = length(listFromArray([1, 2, 3, 4])) // 4);
q