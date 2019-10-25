// const nerdify = txt => txt.replace(/a/gi, '4').replace(/e/gi, '3').replace(/l/g, '1')
// const nerdify = t => t.replace(/[aelAE]/g, a => ({'a': 4,'e': 3,'l': 1} [a.toLowerCase()]));
const nerdify = txt => txt.replace(/[AaEel]/g, c => "44331"["AaEel".indexOf(c)])

q = nerdify("Fund4m3nt41s") // "Fund4m3nt41s"
q
q = nerdify("Seven") // "S3v3n"
q
q = nerdify("Los Angeles") // "Los 4ng313s"
q
q = nerdify("Seoijselawuue") // "S3oijs314wuu3"
q