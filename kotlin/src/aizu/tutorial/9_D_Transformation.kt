package aizu.tutorial

fun main(args: Array<String>?): Unit {
    var word = readLine()?.trim() ?: return
    val count = readLine()?.trim()?.toInt() ?: return

    repeat(count) {
        val line = readLine()?.trim()?.split(" ") ?: return
        when (line[0]) {
            "print" -> word = print(word, line[1].toInt(), line[2].toInt())
            "reverse" -> word = reverse(word, line[1].toInt(), line[2].toInt())
            "replace" -> word = replace(word, line[1].toInt(), line[2].toInt(), line[3])
        }
    }
}

private fun print(word: String, a: Int, b: Int): String {
    println(word.substring(a..b))
    return word
}

private fun reverse(word: String, a: Int, b: Int): String {
    return word.substring(0 until a) + word.substring(a..b).reversed() + word.substring(b + 1 until word.length)
}

private fun replace(word: String, a: Int, b: Int, replacement: String): String {
    return word.substring(0 until a) + replacement + word.substring(b + 1 until word.length)
}
