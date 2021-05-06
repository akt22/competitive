const val N = 3
const val ANSWER = 7

fun main(args: Array<String>) {
    val (a, b, c, d) = readLine()!!.trim().toCharArray().map { it -> Integer.parseInt(it.toString()) }

    solve(a, b, c, d)
}

private fun solve(a: Int, b: Int, c: Int, d: Int) {
    val remain = listOf(b, c, d)
    for (bit in 0 until 1.shl(N)) {
        var tmp = a
        var tmpString = a.toString()
        for (i in 0 until N) {
            val elem = remain[i]
            if (1.shl(i) and bit != 0) {
                tmp += elem
                tmpString += "+%d".format(elem)
            } else {
                tmp -= elem
                tmpString += "-%d".format(elem)
            }
        }
        if (tmp == ANSWER) {
            println("%s=7".format(tmpString))
            return
        }
    }
}
