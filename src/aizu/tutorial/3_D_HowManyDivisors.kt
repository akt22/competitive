package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input).let { if (it.isNotEmpty()) println(it) }
    }
}

private fun resolve(inputs: List<Int>): String {
    val (a, b, c) = inputs
    var count = 0
    for (i in (a..b)) {
        if (c % i == 0) count += 1
    }
    return count.toString()
}
