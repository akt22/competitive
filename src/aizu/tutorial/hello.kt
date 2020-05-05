package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        val (x) = input
        if (x == 0) return
        println(execute(x))
    }
}

private fun execute(x: Int): Int {
    return x * x * x
}
