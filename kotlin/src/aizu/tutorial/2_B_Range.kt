package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        println(resolve(input))
    }
}

private fun resolve(inputs: List<Int>): String {
    val (a, b, c) = inputs
    return when {
        (a < b) && (b < c) -> "Yes"
        else -> "No"
    }
}
