// const noSpace = str => [...str].filter(v => v != ' ').join('')
const noSpace = str => str.replace(/\s/g , '')


q = noSpace('8 j 8   mBliB8g \t imjB8B8 \t jl  B') // '8j8mBliB8gimjB8B8jlB')
q
q = noSpace('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd') // '88Bifk8hB8BB8BBBB888chl8BhBfd');
q
q = noSpace('8aaaaa dddd r     ') // '8aaaaaddddr');
q