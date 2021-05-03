
// Values are immutables constants. Val != var
object HelloWorld extends App {
    val hello: String = "Hola!"
    var hello_var: String = "Hallo!"

    println(hello)
    println(hello_var)
    hello_var = hello
    println(hello_var)
}
