-- Ideal solution using inductively proven formulas
difference :: Int -> Int
difference n = n^2 * (n+1)^2 `div` 4 - n * (n+1) * (2*n+1) `div` 6

problem6 :: Int
problem6 = difference 100