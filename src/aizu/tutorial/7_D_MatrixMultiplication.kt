package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val rowNumber = readLine()?.trim()?.split(' ')?.map(String::toInt)
    if (rowNumber !is List<Int>) {
        return
    }
    val (n, m, l) = rowNumber

    val matrix1 = mutableListOf<List<Long>>()
    for (i in 1..n) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toLong)
        if (input !is List<Long>) {
            return
        }
        matrix1.add(input)
    }

    val matrix2 = mutableListOf<MutableList<Long>>()
    repeat(l) {
        matrix2.add(mutableListOf())
    }
    for (i in 1..m) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toLong)
        if (input !is List<Long>) {
            return
        }
        for ((idx, v) in input.withIndex()) {
            matrix2[idx].add(v)
        }
    }
    println(calc(matrix1, matrix2).joinToString("\n") { it.joinToString(" ") })
}

private fun calc(m1: List<List<Long>>, m2: List<List<Long>>): List<List<Long>> {
    val res = mutableListOf<List<Long>>()
    for (r in m1) {
        res.add(m2.map { r * it })
    }
    return res
}

private operator fun List<Long>.times(other: List<Long>): Long {
    return this.withIndex()
        .map { (idx, v) -> v * other[idx] }
        .sum()
}
