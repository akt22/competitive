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

private fun resolve(inputs: List<Int>) {
    val (n) = inputs

    for (i in 1..n) {
        if (i % 3 == 0 || i % 10 == 3 || i.toString().contains("3")) {
            print(" $i")
        }
    }
    println()
}
