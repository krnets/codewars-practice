// 6kyu - Count the smiley faces!

const countSmileys = arr => arr.filter(v => v.match(/(:|;)(-|~)?(\)|D)/)).length


q = countSmileys([]) // 0
q
q = countSmileys([':D', ':~)', ';~D', ':)']) // 4
q
q = countSmileys([':)', ':(', ':D', ':O', ':;']) // 2
q
q = countSmileys([';]', ':[', ';*', ':$', ';-D']) // 1
q