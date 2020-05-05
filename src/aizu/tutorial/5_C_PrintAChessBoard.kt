package aizu.tutorial


fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        resolve(input)
    }
}

private fun resolve(inputs: List<Int>): Unit {
    val (h, w) = inputs
    if (h == 0 || w == 0) return
    (0 until h).forEach { idx ->
        (0 until w).forEach { idx2 ->
            print(charChooser(idx2, idx))
        }
        println()
    }
    println()
}

private fun charChooser(col: Int, row: Int): Char {
    return if ((col % 2 xor row % 2) == 0) '#' else '.'
}
