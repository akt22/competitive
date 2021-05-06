import kotlin.math.min

fun main(args: Array<String>) {
    val (D, G) = readLine()!!.trim().split(" ").map { Integer.parseInt(it) }
    val problem = mutableListOf<Int>()
    val bonus = mutableListOf<Int>()
    repeat(D) {
        val (p, c) = readLine()!!.trim().split(" ").map { Integer.parseInt(it) }
        problem.add(p)
        bonus.add(c)
    }

    solve(D, G, problem, bonus)
}

private fun solve(D: Int, G: Int, problem: List<Int>, bonus: List<Int>) {
    var minCnt = 100000
    for (bit in 0 until 1.shl(D)) {
        var score = 0
        var solved = 0
        var restMaxIndex = -1
        for (i in 0 until D) {
            if (1.shl(i) and bit != 0) {
                score += (i + 1) * 100 * problem[i] + bonus[i]
                solved += problem[i]
            } else {
                restMaxIndex = i
            }
        }

        if (score < G) {
            val base = (1 + restMaxIndex) * 100
            val need = ((G - score - 1) / base) + 1
            if (problem[restMaxIndex] <= need) {
                continue
            }
            solved += need
        }
        minCnt = min(minCnt, solved)
    }
    println(minCnt)
}
