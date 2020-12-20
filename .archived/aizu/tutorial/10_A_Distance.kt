package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val input = readLine()?.trim()?.split(' ')?.map(String::toDouble) ?: return
    println(resolve(input))
}

private fun resolve(input: List<Double>): Double {
    val (x1, y1, x2, y2) = input
    return Math.sqrt(Math.pow(x2 - x1, 2.0) + Math.pow(y2 - y1, 2.0))
}
