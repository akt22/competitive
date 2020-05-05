package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input)
    }
}

private fun resolve(input: List<Int>) {
    val (m, f, r) = input
    if (m == -1 && f == -1 && r == -1) return
    when {
        (m == -1 || f == -1) -> println("F")
        (m + f >= 80) -> println("A")
        (m + f >= 65) -> println("B")
        (m + f >= 50) -> println("C")
        (m + f >= 30 && r >= 50) -> println("C")
        (m + f >= 30 && r < 50) -> println("D")
        else -> println("F")
    }
}
