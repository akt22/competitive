package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim() ?: return
        resolve(input)
    }
}

private fun resolve(input: String) {
    input.toCharArray().forEach {
        print(
            when {
                (it in 'a'..'z') -> it.toUpperCase()
                (it in 'A'..'Z') -> it.toLowerCase()
                else -> it
            }
        )
    }
    println()
}
