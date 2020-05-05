package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        val (a) = input
        println(execute(a))
    }
}

private fun execute(a: Int): String {
    val (hour, mod) = Pair(a / (60 * 60), a % (60 * 60))
    val (minute, second) = Pair(mod / 60, mod % 60)
    return "$hour:$minute:$second"
}
