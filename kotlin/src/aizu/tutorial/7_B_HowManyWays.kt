package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input)
    }
}

private fun resolve(input: List<Int>) {
    val (n, x) = input
    if (n == 0 && x == 0) return
    val set = mutableSetOf<Set<Int>>()
    for (i in 1..n) {
        for (j in 1..n) {
            if (j == i) continue
            for (k in 1..n) {
                if (i == k || j == k) continue
                if ((i + j + k) == x) {
                    set.add(setOf(i, j, k))
                }
            }
        }
    }
    println(set.size)
}
