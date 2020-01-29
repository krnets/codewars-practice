// 7kyu - Price VAT Calculator

/* Create a simple vat calculator class for retrieving the net value and the vat amount from a gross price.
Within the class create the two methods getNet(grossPrice) and getVat(grossPrice).
What is passed to you: vatRate - number 0 - 100 (%) grossPrice - Gross price value
Rounding is achieved using toFixed(2) but the return value has to be the rounded Number not String.

Vat = Net * vatRate
Net + Vat = grossPrice

Note : you have to re-arrange those two definitions to come up with the equations needed. */


function Calculator(vat) {
    this.getNet = grossPrice => +((100 * grossPrice) / (100 + vat)).toFixed(2)
    this.getVat = grossPrice => +((vat * grossPrice) / (100 + vat)).toFixed(2)
}

var calc = new Calculator(20)
q = calc.getNet(100) // 83.33
q
q = calc.getVat(100) // 16.67
q