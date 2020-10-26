import java.util.*

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val countCharMap = mutableMapOf<Char, Int>()
    while (scanner.hasNextLine()) {
        val line = scanner.nextLine()
        for (c in line) {
            countCharMap.merge(c.toLowerCase(), 1, Int::plus)
        }
    }
    ('a'..'z')
        .map { "$it : ${countCharMap.getOrDefault(it, 0)}" }
        .forEach { println(it) }
}
