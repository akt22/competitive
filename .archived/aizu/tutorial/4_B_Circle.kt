package aizu.tutorial


fun main(args: Array<String>?): Unit {
    while (true) {
        val input = readLine()?.trim()?.split(' ')?.map(String::toDouble)
        if (input !is List<Double>) {
            return
        }
        resolve(input).let { if (it.isNotEmpty()) println(it) }
    }
}

private fun resolve(inputs: List<Double>): String {
    val (r) = inputs
    val pi = 3.141592653589793
    val area = r * r * pi
    val long = 2 * r * pi
    return "%.5f %.5f".format(area, long)
}
