// 6kyu - Regexp Basics - is it IPv4 address?

// String.prototype.ipv4Address = function () {
//     return /^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$/.test(this)
// }

// String.prototype.ipv4Address = function () {
//     return /^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$/.test(this);
// }

String.prototype.ipv4Address = function () {
    let s = this.split('.')
    return s.length == 4 && s.every(v => (n = Number(v), v == String(n) && n >= 0 && n < 256))
}

q = "".ipv4Address() // false
q
q = "127.0.0.1".ipv4Address() // true
q
q = "0.0.0.0".ipv4Address() // true
q
q = "255.255.255.255".ipv4Address() // true
q
q = "10.20.30.40".ipv4Address() // true
q
q = "10.256.30.40".ipv4Address() // false
q
q = "10.20.030.40".ipv4Address() // false
q
q = "127.0.1".ipv4Address() // false
q
q = "127.0.0.0.1".ipv4Address() // false
q
q = "..255.255".ipv4Address() // false
q
q = "127.0.0.1\n".ipv4Address() // false
q
q = "\n127.0.0.1".ipv4Address() // false
q
q = " 127.0.0.1".ipv4Address() // false
q
q = "127.0.0.1 ".ipv4Address() // false
q
q = " 127.0.0.1 ".ipv4Address() // false
q