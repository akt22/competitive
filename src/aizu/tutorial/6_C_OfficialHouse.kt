package aizu.tutorial


fun main(args: Array<String>?): Unit {
    val rowNumber = readLine()?.trim()?.split(' ')?.map(String::toInt)
    if (rowNumber !is List<Int>) {
        return
    }
    val (n) = rowNumber

    var lodge = createLodge()
    for (i in 1..n) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        lodge = event(lodge, input)
    }
    resolve(lodge)
}

private fun createLodge(): MutableMap<String, Int> {
    val lodge = mutableMapOf<String, Int>()
    (1..4).forEach { s ->
        (1..3).forEach { f ->
            (1..10).forEach { r ->
                lodge["$s$f$r"] = 0
            }
        }
    }
    return lodge
}

private fun event(lodge: MutableMap<String, Int>, inputs: List<Int>): MutableMap<String, Int> {
    val (b, f, r, v) = inputs
    lodge["$b$f$r"] = lodge["$b$f$r"]!!.plus(v)
    return lodge
}

private fun resolve(lodge: MutableMap<String, Int>) {
    var res = ""
    for ((index, value) in lodge.values.withIndex()) {
        res += " $value"
        res += (if ((index + 1) % 10 == 0) "\n" else "")
        if ((index + 1) % 30 == 0) res += "#".repeat(20) + "\n"
    }
    println(res.substring(0 until res.length - 22))
}
