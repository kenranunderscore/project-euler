isPalindrome :: Int -> Bool
isPalindrome x = s == reverse s
    where s = show x

problem3 :: Int
problem3 = maximum [x * y | x <- [100 .. 999], y <- [100 .. 999], isPalindrome (x * y)]