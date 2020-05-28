package aizu.tutorial

fun main(args: Array<String>?): Unit {
    val target = readLine()?.trim() ?: return
    val sentence = mutableListOf<String>()
    while (true) {
        val line = readLine()?.trim()?.split(" ") ?: return
        if (line[0] == "END_OF_TEXT") break
        line.forEach { sentence.add(it.toLowerCase()) }
    }
    resolve(target, sentence)
}

private fun resolve(target: String, sentence: List<String>) {
    var count = 0
    sentence.forEach { if (target == it) count += 1 }
    println(count)
}
