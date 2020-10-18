package aizu.tutorial

fun main(args: Array<String>?): Unit {
    var count = 0
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        count += 1
        if (count % 2 != 0) continue
        resolve(input).let { if (it.isNotEmpty()) println(it) }
    }
}

private fun resolve(inputs: List<Int>): String {
    var (min, max, sum) = Triple(1000000, -1000000, 0L)
    for (i in inputs) {
        if (i < min) min = i
        if (i > max) max = i
        sum += i.toLong()
    }
    return "$min $max $sum"
}
