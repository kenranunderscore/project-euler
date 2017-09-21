module Main where

import Numeric (showIntAtBase)
import Data.Char (intToDigit)

toBinaryString :: Integer -> String
toBinaryString n = showIntAtBase 2 intToDigit n ""

isPalindromic :: String -> Bool
isPalindromic s = s == reverse s

doublePalindromeSum :: Integer -> Integer
doublePalindromeSum n = sum [x | x <- [1,3..n], isPalindromic $ show x, isPalindromic $ toBinaryString x]

main = print $ doublePalindromeSum 1000000