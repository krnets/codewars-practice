fun infected(s: String): Double {
    var healthy = 0
    var infected = 0

    s.split('X')
        .forEach {
            if (it.contains('1'))
                infected += it.length
            else healthy += it.length
        }

    if (healthy + infected == 0)
        return 0.0

    return 100.0 * infected / (healthy + infected)
}