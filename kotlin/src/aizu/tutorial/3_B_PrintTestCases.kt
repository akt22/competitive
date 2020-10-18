package aizu.tutorial

fun main(args: Array<String>?): Unit {
    var index = 1
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) return
        val (x) = input
        if (x == 0) return
        println("Case $index: $x")
        index += 1
    }
}
