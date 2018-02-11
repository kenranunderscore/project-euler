fibonacci :: [Integer]
fibonacci = 1 : 1 : zipWith (+) fibonacci (tail fibonacci)

problem2 :: Integer
problem2 = sum [x | x <- takeWhile (<= 4000000) fibonacci, even x]