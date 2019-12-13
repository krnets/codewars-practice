// 6kyu - Schrödinger's Boolean

/* Can a value be both true and false?

Define omniBool so that it returns true for the following:

omniBool == true && omniBool == false */

const omnibool = { n: 0, valueOf: () => this.n = !this.n }

q = omnibool == true
q
q = omnibool == false
q
q = (omnibool == true) && (omnibool == false)
q