lowestCommonMultiple :: [Int] -> Int
lowestCommonMultiple = foldr1 lcm

problem5 :: Int
problem5 = lowestCommonMultiple [1..20]