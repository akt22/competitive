package aizu.tutorial


fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input).let { if (it.isNotBlank()) println(it) }
    }
}

private fun resolve(inputs: List<Int>): String {
    val (h, w) = inputs
    if (h == 0 || w == 0) return ""
    val width = "#".repeat(w)
    return "$width\n".repeat(h)
}
