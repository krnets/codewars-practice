const changeCase = (identifier, targetCase) => {
    if (!/^(snake|camel|kebab)$/.test(targetCase))
        return undefined;

    if (/(-.*[_A-Z])|(_.*[-A-Z])|([A-Z].*[_-])/.test(identifier))
        return undefined;

    let output = '';

    switch (targetCase) {
        case 'snake':
            output = identifier.replace(/[A-Z-]/g,
                char => (char === '-' ? '_' : '_' + char.toLowerCase()));
            break;
        case 'camel':
            output = identifier.replace(/[_-][a-z]/g,
                char => char[1].toUpperCase());
            break;
        case 'kebab':
            output = identifier.replace(/[A-Z_]/g,
                char => (char === '_' ? '-' : '-' + char.toLowerCase()));
            break;
    }

    return output;
}

// q = changeCase("little-shop-of-horrors", "kebab") // 'little-shop-of-horrors'
// q
// q = changeCase("doHTMLrequest", "kebab") // "do-h-t-m-l-request"
// q
// q = changeCase("doHTMLRequest", "kebab") // "do-h-t-m-l-request"
// q
// q = changeCase("fromCamelCase", "kebab") // "from-camel-case"
// q
// q = changeCase("from_snake_case", "kebab") // "from-snake-case"
// q

// q = changeCase("fromCamelCase", "snake") // "from_camel_case")
// q
// q = changeCase("from-kebab-case", "snake") // "from_kebab_case"
// q
// q = changeCase("little_shop_of_horrors", "snake") // 'little_shop_of_horrors'
// q

// q = changeCase("from_snake_case", "camel") // "fromSnakeCase"
// q
// q = changeCase("from-kebab-case", "camel") // "fromKebabCase"
// q
// q = changeCase("from-k-e-b-ab-case", "camel") // "fromKebabCase"
// q
// q = changeCase("guluznumosyet-i-ojfkcmolqikg-wcszrjummr", "camel") 
// q

q = changeCase("invalid-inPut_bad", "kebab") // undefined
q
// q = changeCase("valid-input", "huh???") // undefined
// q
// q = changeCase("", "camel") // ""
// q