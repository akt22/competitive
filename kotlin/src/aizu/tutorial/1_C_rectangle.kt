package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        val (a, b) = input
        if (a == 0 || b == 0) return
        println(execute(a, b).let { "${it.first} ${it.second}" })
    }
}

private fun execute(a: Int, b: Int): Pair<Int, Int> {
    return Pair(a * b, 2 * a + 2 * b)
}
