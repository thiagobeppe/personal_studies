package section_one

object ScalaBasics extends App {
    //Aula 1 Types, Var , Val
    //val são imutáveis, e o compilador pode inferir o tipo
    val x: Int = 42
    val y = 42
    println(x,y)

    //var são mutáveis mas desencorajadas por possuirem "side effects"
    var variable: Int = 5
    println(variable)
    variable = 10
    println(variable)
    //Aula 2 Expressions

    val x_plus: Int = 1+2

    println(2+3*5) //+ - * / & | << >> >>>
    println( 1 == x_plus) // == != >= <= > <
    println(!(1 == x_plus)) //Negação (! && ||)

    variable *= 4 //+= -+ /= *=
    println(variable)

    val aCondition: Boolean = true
    val aConditionedValue: Int =  if(aCondition) 5 else 3
    println(aConditionedValue)

    val aCodeBlock:String = {
        val y =2
        val z = y + 3
        if (z >2) "hello" else "good bye"
    }
    println(aCodeBlock)

    //Aula 3 Functions

    def aFunction(a: Int, b: Double ): Double = {
        a+b
    }
    println(aFunction(10,0.0))

    def aRepeatedFunction(aString: String, n: Int): String = {
        if (n == 1) aString
        else aString + aRepeatedFunction(aString, n-1)
        
    }
    println(aRepeatedFunction("a",3))

    def greetingFunction(name: String, age: Int): String = {
        s"Hello, my name is $name, and I have $age years old"
    }
    println(greetingFunction("Thiago", 26))

    def factorialNumber(number: Int): Int = {
        if (number <= 1) 1
        else number * factorialNumber(number - 1)
    }
    println(factorialNumber(10))

    def fibFunc(number: Int): Int = {
        if (number <= 1) 1
        else fibFunc(number - 1) + fibFunc(number - 2) 
    }
    println(fibFunc(15))

    def isPrime(number: Int): Boolean = {
        def isPrimeUntil(t: Int): Boolean = {
            if (t <= 1) true
            else number % t != 0 && isPrimeUntil(t-1)
        }
        isPrimeUntil((number/2).toInt)
    }
    println(isPrime(4))
}