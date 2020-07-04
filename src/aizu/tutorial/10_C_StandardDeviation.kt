package aizu.tutorial

fun main(args: Array<String>?): Unit {
    var count = 0
    while (true) {
        val input = readLine()?.trim()?.split(" ")?.map(String::toInt) ?: return
        if (count % 2 != 0) resolve(input)
        if (count % 2 == 0 && input[0] == 0) break
        count += 1
    }
}

private fun resolve(input: List<Int>) {
    val avg = input.average()
    val s = input.map { Math.pow(it - avg, 2.0) }.sum()
    println(Math.sqrt(s / input.size))
}
