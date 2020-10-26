package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val rowNumber = readLine()?.trim()?.split(' ')?.map(String::toInt)
    if (rowNumber !is List<Int>) {
        return
    }
    val (n, m) = rowNumber

    val matrix = mutableListOf<List<Int>>()
    for (i in 1..n) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        matrix.add(input)
    }

    val vector = mutableListOf<Int>()
    for (i in 1..m) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        val (value) = input
        vector.add(value)
    }

    println(calc(matrix, vector).joinToString("\n"))
}

private fun calc(matrix: List<List<Int>>, vector: List<Int>): List<Int> {
    return matrix.map { it * vector }
}

private operator fun List<Int>.times(other: List<Int>): Int {
    return this.withIndex()
        .map { (idx, v) -> v * other[idx] }
        .sum()
}
