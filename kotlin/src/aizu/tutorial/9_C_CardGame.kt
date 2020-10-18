package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val turn = readLine()?.trim()?.toInt() ?: return
    var taro = 0
    var hanako = 0
    repeat(turn) {
        val input = readLine()?.trim()?.split(" ") ?: return
        val (t, h) = judge(input)
        taro += t
        hanako += h
    }
    println("$taro $hanako")
}

private fun judge(input: List<String>): Pair<Int, Int> {
    val (t, h) = input
    return when {
        t < h -> 0 to 3
        t > h -> 3 to 0
        else -> 1 to 1
    }
}
