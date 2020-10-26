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
    val (x, y) = inputs
    if (x == 0 && y == 0) return ""
    return if (x < y) return "$x $y" else "$y $x"
}
