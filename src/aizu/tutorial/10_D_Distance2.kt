package aizu.tutorial

fun main(args: Array<String>?): Unit {
    readLine() ?: return
    val x = readLine()?.trim()?.split(' ')?.map(String::toDouble) ?: return
    val y = readLine()?.trim()?.split(' ')?.map(String::toDouble) ?: return
    resolve(x, y)
}

private fun resolve(x: List<Double>, y: List<Double>) {
    println(minkowski(x, y, 1.0))
    println(minkowski(x, y, 2.0))
    println(minkowski(x, y, 3.0))
    println(chebyshev(x, y))
}

private fun minkowski(x: List<Double>, y: List<Double>, p: Double): Double {
    return Math.pow(
        x.zip(y)
            .map { (_x, _y) -> Math.pow(Math.abs(_x - _y), p) }
            .sum(),
        1 / p)
}

private fun chebyshev(x: List<Double>, y: List<Double>): Double {
    return x.zip(y).map { (_x, _y) -> Math.abs(_x - _y) }.max() ?: 0.0
}
