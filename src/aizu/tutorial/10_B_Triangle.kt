package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val input = readLine()?.trim()?.split(' ')?.map(String::toDouble) ?: return
    resolve(input)
}

private fun resolve(input: List<Double>) {
    val (a, b, c) = input
    val s = 0.5 * a * b * Math.sin(Math.toRadians(c))
    val l = a + b + Math.sqrt(Math.pow(a, 2.0) + Math.pow(b, 2.0) - 2 * a * b * Math.cos(Math.toRadians(c)))
    val h = b * Math.sin(Math.toRadians(c))
    println("$s\n$l\n$h")
}
