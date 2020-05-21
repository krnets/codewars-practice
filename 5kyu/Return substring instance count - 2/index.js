// 5kyu - Return substring instance count - 2

/* Complete the solution so that it returns the number of times the search_text is found within the full_text.
searchSubstr( fullText, searchText, allowOverlap = true )
so that overlapping solutions are (not) counted. If the searchText is empty, it should return 0. */

// function searchSubstr(fullText, searchText, allowOverlap) {
//     if (searchText == '')
//         return 0
//     if (allowOverlap == false)
//         return (fullText.match(new RegExp(`(?=${searchText})`)) || []).length
//     else
//         return (fullText.match(new RegExp(`(?=${searchText})`, 'g')) || []).length
// }

const searchSubstr = (fullText, searchText, allowOverlap) => searchText == '' ? 0 :
    fullText.match(RegExp(allowOverlap ? `(?=${searchText})` : searchText, 'g') || []).length

// const searchSubstr = (fullText, searchText, allowOverlap) => searchText == '' ? 0 :
//     fullText.match(new RegExp((allowOverlap || (allowOverlap == undefined)) ? `(?=${searchText})` : fullText, 'g')).length

// const searchSubstr = (fullText, searchText, allowOverlap) => fullText && searchText ? fullText.match(RegExp(allowOverlap ? `(?=${searchText})` : searchText, 'g') || []).length : 0
// const searchSubstr = (text, search, overlap) => text && search ? text.match(RegExp(overlap ? `(?=${search})` : search, 'g') || []).length : 0
// const searchSubstr = (text, search, overlap) => search == '' ? 0 : text.match(RegExp(overlap ? `(?=${search})` : search, 'g') || []).length
// const searchSubstr = (f, s, ol = true) => f && f.length && s && s.length ? (i => i != -1 ? 1 + searchSubstr(f.slice(i + 1 + (ol ? 0 : s.length)), s) : 0)(f.indexOf(s)) : 0;

q = searchSubstr('aa_bb_cc_dd_bb_e', 'bb') // 2
q
q = searchSubstr('aaabbbcccc', 'bbb') // 1
q
q = searchSubstr('aaa', 'aa') // 2
q
q = searchSubstr('aaa', '') // 0
q
q = searchSubstr('aaa', 'aa', false) // 1
q