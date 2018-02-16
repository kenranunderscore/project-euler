-- Ideal solution using inductively proven formulas
difference :: Int -> Int
difference n = n^2 * (n+1)^2 `div` 4 - n * (n+1) * (2*n+1) `div` 6

problem6 :: Int
problem6 = difference 100

-- Solution without using known formulas
sumOfSquares :: Int -> Int
sumOfSquares n = sum [x^2 | x <- [1..n]]

squareOfSum :: Int -> Int
squareOfSum n = s^2
    where s = sum [1..n]

problem6' :: Int
problem6' = squareOfSum 100 - sumOfSquares 100