package aizu.tutorial

fun main(args: Array<String>?): Unit {
    var count = 0
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        count += 1
        if (count % 2 != 0) continue
        resolve(input)
    }
}

private fun resolve(inputs: List<Int>) {
    println(inputs.reversed().joinToString(" "))
}
