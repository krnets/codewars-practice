function londonCityHacker(journey) {
    let result = 0
    for (let i = 0; i < journey.length; i++) {
        if (isNaN(journey[i]))
            result += 2.40
        else {
            result += 1.50
            if (typeof journey[i + 1] == "number")
                i++
        }
    }
    return '£' + result.toFixed(2)
}

q = londonCityHacker([12, 'Central', 'Circle', 21]) // "£7.80"
q
q = londonCityHacker(['Piccidilly', 56]) // "£3.90"
q
q = londonCityHacker(['Northern', 'Central', 'Circle']) // "£7.20"
q
q = londonCityHacker(['Piccidilly', 56, 93, 243]) // "£5.40"
q
q = londonCityHacker([386, 56, 1, 876]) // "£3.00"
q
q = londonCityHacker([]) // "£0.00"
q