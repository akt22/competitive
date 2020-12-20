package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val input = readLine()?.trim()?.split(" ")?.map(String::toDouble) ?: return
    resolve(input)
}

private fun resolve(input: List<Double>) {
    val (a, b) = input.map { it.toBigDecimal() }
    val d = a.multiply(b)
    println(d.toBigInteger())
}
