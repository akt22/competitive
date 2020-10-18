package atcoder

var S = ""

fun main(args: Array<String>) {
    S = readLine()!!

    solve()
}

private fun solve() {
    val n = S.length
    var ans = 0
    for (bit in 0 until 1.shl(n-1)) {
        var tmp = 0
        for (i in 0 until n-1) {
            tmp = tmp*10 + S[i].toInt()
            if (bit shr i and 1 == 1) {
                ans += tmp
                tmp = 0
            }
        }
        tmp = tmp*10 + S[S.lastIndex].toInt()
        ans += tmp
    }
    println(ans)
}
