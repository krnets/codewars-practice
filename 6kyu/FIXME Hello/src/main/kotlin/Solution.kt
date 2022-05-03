/*
class Dinglemouse {
    private var linkedHashMap = linkedMapOf("greeting" to "Hello.")

    fun setAge(age: Int): Dinglemouse {
        linkedHashMap["age"] = "I am $age."
        return this
    }
    fun setSex(sex: Char): Dinglemouse {
        linkedHashMap["sex"] = "I am %s.".format(if (sex == 'M') "male" else "female")
        return this
    }
    fun setName(name: String): Dinglemouse {
        linkedHashMap["name"] = "My name is $name."
        return this
    }
    fun hello(): String = linkedHashMap.values.reduce { acc, s -> "$acc $s" }
}
*/

class Dinglemouse {
    private var props = linkedMapOf("greeting" to "Hello.")

    fun setAge(age: Int): Dinglemouse = apply { props["age"] = "I am $age." }
    fun setSex(sex: Char): Dinglemouse = apply { props["sex"] = "I am %s.".format(if (sex == 'M') "male" else "female") }
    fun setName(name: String): Dinglemouse = apply { props["name"] = "My name is $name." }
    fun hello(): String = props.values.joinToString(" ")
}
