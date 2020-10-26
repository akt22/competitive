package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val rc = readLine()?.trim()?.split(' ')?.map(String::toInt)
    if (rc !is List<Int>) {
        return
    }
    val (r, _) = rc

    val matrix = mutableListOf<MutableList<Int>>()
    for (i in 1..r) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is MutableList<Int>) {
            return
        }
        matrix.add(input)
    }
    resolve(matrix)
}

private fun resolve(matrix: MutableList<MutableList<Int>>) {
    matrix.forEach { it.add(it.sum()) }

    val l = mutableListOf<Int>()
    for (i in matrix[0].indices) {
        var s = 0
        for (j in (matrix.indices)) {
            s += matrix[j][i]
        }
        l.add(s)
    }
    matrix.add(l)

    println(matrix.joinToString("\n") { it.joinToString(" ") })
}
