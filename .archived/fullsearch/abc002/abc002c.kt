import kotlin.math.max

fun main(args: Array<String>) {
    val (n, m) = readLine()!!.trim().split(" ").map { Integer.parseInt(it) }
    val relation = mutableMapOf<Int, List<Int>>()
    repeat(m) {
        val (x, y) = readLine()!!.trim().split(" ").map { Integer.parseInt(it) }
        val l = relation.getOrDefault(x, mutableListOf())
        val l2 = l.toMutableList()
        l2.add(y)
        relation[x] = l2
    }

    solve(n, relation)
}

private fun solve(n: Int, relation: Map<Int, List<Int>>) {
    var ans = 0
    for (bit in 0 until 1.shl(n)) {
        val tmp = mutableListOf<Int>()
        var flg = true
        for (i in 0 until n) {
            if (1.shl(i) and bit == 0) {
                continue
            }
            for (c in tmp) {
                val cs = relation[c]
                if (cs == null || !cs.contains(i + 1)) {
                    flg = false
                    break
                }
            }
            tmp.add(i + 1)
        }
        if (flg) {
            ans = max(ans, tmp.size)
        }
    }
    println(ans)
}
