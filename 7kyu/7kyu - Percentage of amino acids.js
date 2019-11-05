const aaPercentage = (seq, codes='AILMFWYV') => Math.round(([...seq].filter(val => codes.includes(val)).length / seq.length) * 100)


q = aaPercentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) // 5
q
q = aaPercentage("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]) // 55
q
q = aaPercentage("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]) // 70
q
q = aaPercentage("MSRSLLLRFLLFLLLLPPLP") // 65
q