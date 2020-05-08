fun main(args: Array<String>) {
    while (true) {
        val x = readLine()
        if (x == "0") break
        println(x!!.split("").filter(String::isNotEmpty).map(String::toInt).sum())
    }
}
