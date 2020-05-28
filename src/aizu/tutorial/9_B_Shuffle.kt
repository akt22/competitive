package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        var deck = readLine()?.trim() ?: return
        if (deck == "-") break
        val shuffleCount = readLine()?.trim()?.toInt() ?: return
        repeat(shuffleCount) {
            val num = readLine()?.trim()?.toInt() ?: return
            deck = shuffle(deck, num)
        }
        println(deck)
    }
}

private fun shuffle(deck: String, num: Int): String {
    val first = deck.substring(0 until num)
    val second = deck.substring(num until deck.length)
    return second + first
}
