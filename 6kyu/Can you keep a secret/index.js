// 6kyu - Can you keep a secret?

/* There's no such thing as private properties on a coffeescript object! But, maybe there are?

Implement a function createSecretHolder(secret) which accepts any value as secret and returns an object with ONLY two methods

    getSecret() which returns the secret
    setSecret() which sets the secret */

// function createSecretHolder(secret) {
//     return {
//         setSecret: function (v) {
//             secret = v
//         },
//         getSecret: function () {
//             return secret
//         }
//     }
// }

// function createSecretHolder(secret) {
//     function getSecret() {
//         return secret;
//     }
//     function setSecret(s) {
//         secret = s;
//     }
//     return { getSecret, setSecret };
// }

function createSecretHolder(secret) {
    return {
        setSecret: function (v) { secret = v },
        getSecret: function ()  { return secret }
    }
}

// function createSecretHolder(secret) {
//     return {
//         getSecret: ()  => secret,
//         setSecret: (v) => secret = v,
//     }
// }


obj = createSecretHolder(5)
obj
q = obj.getSecret() // returns 5
q
q = obj.setSecret(2)
q
q = obj.getSecret() // returns 2
q