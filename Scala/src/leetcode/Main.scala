package leetcode

import scala.io.StdIn
import leetcode.leet118

object Main {
  def main(args: Array[String]): Unit = {
    // start
    println(">>> Welcome to Scala!")
    print("Enter here: ")

    val str = StdIn.readLine()
    val result = Solution.letterCombinations(str)

    println(result)

    // end
    println(">>> Bye. Good Luck!")
  }
}
