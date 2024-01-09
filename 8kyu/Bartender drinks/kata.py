def get_drink_by_profession(param):
    match param.title():
        case "Jabroni": return "Patron Tequila"
        case "School Counselor": return "Anything with Alcohol"
        case "Programmer": return "Hipster Craft Beer"
        case "Bike Gang Member": return "Moonshine"
        case "Politician": return "Your tax dollars"
        case "Rapper": return "Cristal"
        case _: return "Beer"
