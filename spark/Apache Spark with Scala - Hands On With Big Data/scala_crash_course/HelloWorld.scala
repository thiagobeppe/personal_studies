

object HelloWorld extends App {
    // Values are immutables constants. Val != var
    val hello: String = "Hola!"
    var hello_var: String = "Hallo!"
    println(hello)
    println(hello_var)
    hello_var = hello
    println(hello_var)

    //Data types
    val numberOne: Int = 1
    val truth: Boolean = true
    val letterA: Char = 'a'
    val pi: Double = 3.14159
    val piSinglePrecision: Float = 3.14159f
    val bigNumber: Long = 31514241
    val smallNumber: Byte = 127

    //Format
    println("Here is a mess: " + numberOne + truth + letterA + pi + piSinglePrecision + bigNumber)
    println(f"Pi is about $piSinglePrecision%.3f")
    println(f"Zero padding on the left: $numberOne%05d")
    println(s"I can use the s prefix to use variable like $numberOne $truth $letterA")
    
    //RegEx
    val theUltimateAnswer: String = "To life, the universe, and everything is 42."
    val pattern = """.* ([\d]+).*""".r

    val pattern(answerString) = theUltimateAnswer

    println(answerString) 

}
