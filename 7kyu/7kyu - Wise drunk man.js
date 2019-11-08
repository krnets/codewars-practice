// 7kyu - Wise drunk man

// const wdm = talk => talk.replace(/hiccup|puke/g, '').split(/\s+/).join(' ').trim()
const wdm = talk => talk.replace(/hiccup|puke/g, '').trim().replace(/ +/g, ' ')

q = wdm("puke All's well hiccup     that ends hiccup well puke")
// "All's well that ends well"
q
q = wdm('puke make hiccup hiccup money puke puke puke and hiccup hiccup puke spend hiccup puke puke it hiccup wisely.')
//'make money and spend it wisely.'
q