function gcd(p, q) {
    p
    q
    if (q == 0) {
        return p
    } else {
        return gcd(q, p % q)
    }
}

const gcd = (p, q) => q === 0 ? p : gcd (q, p % q)
// z = gcd(105, 24)
// z

z = gcd(999,33)
z
