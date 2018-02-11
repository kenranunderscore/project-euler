problem4 :: Int
problem4 = maximum [z | x <- [100 .. 999], y <- [x .. 999], let z = x * y, isPalindrome z]
    where isPalindrome a = let s = show a in s == reverse s