package going

fun movie(card: Int, ticket: Int, perc: Double): Int {
    var systemA = 0.0
    var systemB = card.toDouble()
    var currentTicketPrice = ticket.toDouble()
    var count = 0

    while (Math.ceil(systemB) >= systemA) {
        systemA += ticket
        currentTicketPrice *= perc
        systemB += currentTicketPrice
        count++
    }
    return count
}