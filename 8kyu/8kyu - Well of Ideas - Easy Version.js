function well(arr) {
    // return [...arr].filter(el => el !== 'bad').length == 0 ? 'Fail!' 
    //      : [...arr].filter(el => el !== 'bad').length <= 2 ? 'Publish!' 
    //      : 'I smell a series!'
    let ideas = [...arr].filter(el => el == 'good').length
    return ideas == 0 ? 'Fail!' :
           ideas <= 2 ? 'Publish!' :
           'I smell a series!'
}

q = well(['bad', 'bad', 'bad']) // 'Fail!');
q
q = well(['good', 'bad', 'bad', 'bad', 'bad']) // 'Publish!');
q
q = well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']) //'I smell a series!')
q

const assertEquals = (fn, cmp) => fn == cmp

q = assertEquals(well(['bad', 'bad', 'bad']), 'Fail!');
q
q = assertEquals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!');
q
q = assertEquals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!');
q