sum_of_mults_of_3_or_5 = sum [x | x <- [1..999], mod x 3 == 0 || mod x 5 == 0] 