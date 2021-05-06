object FlowControl extends App{
    if ( 1 > 3) println ("Impossible") else println("The world makes sense.")
    
    if ( 1 > 3) {
        println ("Impossible")
        } 
    
    else {
       println("The world makes sense.")
    }

    val number = 3
    number match {
        case 1 => println("one")
        case 2 => println("two")
        case _ => println("something else")
    }

    for (x <- 1 to 4) {
        val squared = x*x
        println(squared)
    }

    var x = 10
    while (x >= 0){
        println(x)
        x -= 1
    }

    
    def fib(n : Int): Int = {
        n match{
            case 0 | 1 => n
            case _ => fib(n-1) + (n-2)
        }
    }
    for (xy<- 0 to 10){
        println(fib(xy))
    }
}