import kotlin.math.max

fun main(args: Array<String>) {
    val N = readLine()!!.toInt()
    val meats = mutableListOf<Int>()
    repeat(N) {
        meats.add(readLine()!!.toInt())
    }

    solve(meats)
}

private fun solve(meats: List<Int>) {
    var plate1 = 0
    var plate2 = 0
    for (meat in meats.sortedDescending()) {
        if (plate1 > plate2) {
            plate2 += meat
        } else {
            plate1 += meat
        }
    }
    println(max(plate1, plate2))
}
