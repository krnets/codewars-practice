const vowelChange = (str, vow) => str.replace(/[aeiou]/g, vow)

q = vowelChange("Hannah Hannah bo-bannah Banana fanna fo-fannah Fee, fy, mo-mannah. Hannah!",'i')
//  'Hinnih Hinnih bi-binnih Binini finni fi-finnih Fii, fy, mi-minnih. Hinnih!'
q
q = vowelChange('adira wants to go to the park', 'o')
// 'odoro wonts to go to tho pork'
q