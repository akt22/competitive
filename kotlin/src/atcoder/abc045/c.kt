var S = ""

fun main(args: Array<String>) {
    S = readLine()!!

    solve()
}

private fun solve() {
    val n = S.length
    var ans: Long = 0
    for (bit in 0 until 1.shl(n - 1)) {
        var tmp = ""
        for (i in 0 until n) {
            tmp += S[i]
            if (1.shl(i) and bit == 0) {
                ans += tmp.toLong()
                tmp = ""
            }
        }
        if (tmp.isNotBlank()) {
            ans += tmp.toInt()
        }
    }
    println(ans)
}
