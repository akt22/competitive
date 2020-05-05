package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input).let { if (it.isNotEmpty()) println(it) }
    }
}

private fun resolve(inputs: List<Int>): String {
    val (a, b) = inputs
    val ans = a.toDouble() / b.toDouble()
    val mod = a % b
    return "${ans.toInt()} $mod " + "%.5f".format(ans)
}
