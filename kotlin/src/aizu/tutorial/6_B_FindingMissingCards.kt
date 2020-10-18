package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val rowNumber = readLine()?.trim()?.split(' ')?.map(String::toInt)
    if (rowNumber !is List<Int>) {
        return
    }
    val (n) = rowNumber

    var deck = createDeck()
    for (i in 1..n) {
        val input = readLine()?.trim()?.split(' ') ?: return
        deck = check(deck, input)
    }
    resolve(deck)
}

private fun createDeck(): MutableMap<String, Boolean> {
    val deck: MutableMap<String, Boolean> = mutableMapOf()
    for (m in listOf("S", "H", "C", "D")) {
        for (n in (1..13)) {
            deck["$m $n"] = false
        }
    }
    return deck
}

private fun check(
    deck: MutableMap<String, Boolean>,
    inputs: List<String>
): MutableMap<String, Boolean> {
    val (mark, number) = inputs
    deck["$mark $number"] = true
    return deck
}

private fun resolve(deck: MutableMap<String, Boolean>) {
    deck.entries.filter { (_, v) -> !v }.forEach { (k, _) -> println(k) }
}
