package aizu.alds1

fun main(args: Array<String>) {
    val (x, y) = readLine()?.trim()?.split(" ")?.map(String::toInt) ?: return
    println(gcd(x, y))
}

private fun gcd(x: Int, y: Int): Int {
    if (x == 0 || y == 0) {
        return if (x >= y) x else y
    }
    return if (x >= y) {
        gcd(y, x % y)
    } else {
        gcd(x, y % x)
    }
}
