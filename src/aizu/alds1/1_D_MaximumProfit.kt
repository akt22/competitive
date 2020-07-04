package aizu.alds1

fun main(args: Array<String>) {
    val num = readLine()?.trim()?.toInt() ?: return
    var m = Double.NEGATIVE_INFINITY
    var hold = readLine()?.trim()?.toDouble() ?: return
    repeat(num - 1) {
        val x = readLine()?.trim()?.toDouble() ?: return
        m = Math.max(m, x - hold)
        if (x < hold) {
            hold = x
        }
    }
    println(m.toInt())
}
