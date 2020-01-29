// 7kyu - Conference Traveller

/* Lucy loves to travel. 
Luckily she is a renowned computer scientist and gets to travel to international conferences using her department's budget.

Each year, Society for Exciting Computer Science Research (SECSR) organizes several conferences around the world. 
Lucy always picks one conference from that list that is hosted in a city she hasn't been to before, and if that leaves her 
with more than one option, she picks the conference that she thinks would be most relevant for her field of research.

Write a function conferencePicker that takes in two arguments:

    citiesVisited, a list of cities that Lucy has visited before, given as an array of strings.
    citiesOffered, a list of cities that will host SECSR conferences this year, given as an array of strings. 
    citiesOffered will already be ordered in terms of the relevance of the conferences for Lucy's research 
    (from the most to the least relevant).

The function should return the city that Lucy should visit, as a string.

Also note:

    You should allow for the possibility that Lucy hasn't visited any city before.
    SECSR organizes at least two conferences each year.
    If all of the offered conferences are hosted in cities that Lucy has visited before, 
    the function should return 'No worthwhile conferences this year!'

Example:

citiesVisited = ['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'];
citiesOffered = ['Stockholm','Paris','Melbourne'];

conferencePicker (citiesVisited, citiesOffered);
// ---> 'Paris' */


function conferencePicker(citiesVisited, citiesOffered) {
    return citiesOffered.filter(v => !citiesVisited.includes(v))[0] || 'No worthwhile conferences this year!'
}

q = conferencePicker(['Mexico City', 'Johannesburg', 'Stockholm', 'Osaka', 'Saint Petersburg', 'London'], ['Stockholm', 'Paris', 'Melbourne']) // 'Paris'
q
q = conferencePicker(['Buenos Aires', 'Mexico City', 'Johannesburg'], ['Melbourne', 'Moscow']) // 'Melbourne'
q
q = conferencePicker(['Tokyo', 'Madrid', 'Melbourne', 'Sydney', 'Rio De Janeiro', 'Saint Petersburg', 'Brisbane', 'Paris', 'Houston'], ['Sydney', 'Chicago', 'Paris']) // 'Chicago'
q
q = conferencePicker([], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']) //'Philadelphia'
q
q = conferencePicker(['London', 'Berlin', 'Mexico City', 'Melbourne', 'Buenos Aires', 'Hong Kong', 'Madrid', 'Paris'], ['Berlin', 'Melbourne']) // 'No worthwhile conferences this year!'
q