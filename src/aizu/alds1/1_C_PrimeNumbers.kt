package aizu.alds1

fun main(args: Array<String>) {
    val num = readLine()?.trim()?.toInt() ?: return
    var count = 0
    repeat(num) {
        val x = readLine()?.trim()?.toInt() ?: return
        if (isPrime(x)) {
            count++
        }
    }
    println(count)
}

private fun isPrime(x: Int): Boolean {
    if (x == 0 || x == 1) {
        return false
    }
    val a = Math.round(Math.sqrt(x.toDouble())).toInt()
    for (i in 2..a) {
        if (x % i == 0) return false
    }
    return true
}
