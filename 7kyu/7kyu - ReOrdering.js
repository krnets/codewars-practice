// 7kyu - ReOrdering

/* There is a sentence which has a mistake in its ordering.

The part with a capital letter should be the first word. */

function reOrdering(text) {
    let arr = text.split(' ')
    let capital = arr.filter(v => v[0].toUpperCase() == v[0])
    let lowercase = arr.filter(v => v != capital)
    return (capital.concat(lowercase)).join(' ')
}


q = reOrdering('ming Yao') // 'Yao ming'
q
q = reOrdering('Mano donowana') // 'Mano donowana'
q
q = reOrdering('wario LoBan hello') // 'LoBan wario hello'
q
q = reOrdering('bull color pig Patrick') // 'Patrick bull color pig'
q
q = reOrdering('jojo ddjajdiojdwo ana G nnibiial') // 'G jojo ddjajdiojdwo ana nnibiial'
q
q = reOrdering('is one of those rare names that s both exotic and simple Adira')
// 'Adira is one of those rare names that s both exotic and simple'
q
q = reOrdering('is an older name than annabel Amabel and a lot more distinctive')
// 'Amabel is an older name than annabel and a lot more distinctive'
q
q = reOrdering('JoJo') // 'JoJo'
q
q = reOrdering('a b c d e f g h i j k l m n o p q r s t u v w x y Z')
//  'Z a b c d e f g h i j k l m n o p q r s t u v w x y'
q
q = reOrdering('a b c d e f g h i j k l m N o p q r s t u v w x y z')
//  'N a b c d e f g h i j k l m o p q r s t u v w x y z'
q