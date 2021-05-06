object Functions extends App {
    def squared(n:Int): Int = {
        n*n
    }

    println(squared(10))
    
    def cubeIt(n: Int): Int = n*n*n
    println(cubeIt(10))

    def transformInt( x: Int, f: Int => Int): Int = {
        f(x)
    }

    println(transformInt(10,squared))
    println(transformInt(10,cubeIt))

    println(transformInt(10, x=> ((x*x) + 5)))
}
