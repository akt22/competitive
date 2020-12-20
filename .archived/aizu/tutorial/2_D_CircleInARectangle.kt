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
    val (w, h, x, y, r) = inputs
    if (x < 0 || y < 0) return "No"

    if ((0 <= x - r) &&
            (x + r <= w) &&
            (0 <= y - r) &&
            (y + r <= h)) return "Yes"
    return "No"
}
