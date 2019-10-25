function romanize(cyrillic) {
    let alphabet = {'а': "a",'б': "b",'в': "v",'г': "g",'д': "d",'е': "e",'ё': "e",'ж': "zh",'з': "z",'и': "i",'й': "i",'к': "k",'л': "l",'м': "m",'н': "n",'о': "o",'п': "p",'р': "r",'с': "s",'т': "t",'у': "u",'ф': "f",'х': "kh",'ц': "ts",'ч': "ch",'ш': "sh",'щ': "shch",'ъ': "ie",'ы': "y",'ь': "",'э': "e",'ю': "iu",'я': "ia",}
    let romanized = cyrillic.toLowerCase().replace(/[абвгдеёжзийклмнопрстуфхцчшщъыьэюя]/g, (char) => alphabet[char])
    return romanized.replace(/(^|\s)[a-z]/g, char => char.toUpperCase())
    // return cyrillic.split("").map(v => alphabet[v]).join("");

}


q = romanize("Иван Иванович") // "Ivan Ivanovich"
q
q = romanize("Анастасия Иванов") //, "Anastasiia Ivanov"
q
q = romanize("Настя Попов") //, "Nastia Popov"
q
q = romanize("Никита Смирнов") //, "Nikita Smirnov"
q
q = romanize("Влад Соколов") //, "Vlad Sokolov"
q
q = romanize("Ольга Кузнецова") //, "Olga Kuznetsova"
q
q = romanize("Александр Васильев") //, "Aleksandr Vasilev"
q
q = romanize("Цветочек Михайлов") //, "Tsvetochek Mikhailov"
q
q = romanize("Дима Петров") //, "Dima Petrov"
q