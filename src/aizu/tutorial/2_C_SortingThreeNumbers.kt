package aizu.tutorial

fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toInt)
        if (input !is List<Int>) {
            return
        }
        println(resolve(input))
    }
}

private fun resolve(inputs: List<Int>): String {
      return inputs.sorted().joinToString(" ")
}
