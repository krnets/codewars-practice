// 7kyu - List Filtering

// const filter_list = l => l.filter(v => typeof v !== 'string')
const filter_list = l => l.filter(v => typeof v === 'number')

q = filter_list([1, 2, 'a', 'b']) // [1,2]
q
q = filter_list([1, 'a', 'b', 0, 15]) // [1,0,15]
q
q = filter_list([1, 2, 'aasf', '1', '123', 123]) // [1,2,123]
q