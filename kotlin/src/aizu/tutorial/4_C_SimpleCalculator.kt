package aizu.tutorial


fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ') ?: return
        if (input.size != 3) {
            return
        }
        resolve(input).let { if (it.isNotEmpty()) println(it) }
    }
}

private fun resolve(inputs: List<String>): String {
    val (_a, op, _b) = inputs
    if (op == "?") return ""
    val (a, b) = listOf(_a, _b).map(String::toInt)
    return when {
        (op == "+") -> "${a + b}"
        (op == "-") -> "${a - b}"
        (op == "*") -> "${a * b}"
        else -> "${a / b}"
    }
}
