package aizu.alds1

fun main(args: Array<String>) {
    val count = readLine()?.trim()?.toInt() ?: return
    val array = readLine()?.trim()?.split(" ")?.map(String::toInt)?.toMutableList() ?: return
    gcd(array, count)
}

private fun gcd(a: MutableList<Int>, n: Int) {
    println(a.joinToString(" "))
    for (i in 1 until n) {
        val v = a[i]
        var j = i - 1
        while (j >= 0 && a[j] > v) {
            a[j + 1] = a[j]
            j--
        }
        a[j + 1] = v
        println(a.joinToString(" "))
    }
}
