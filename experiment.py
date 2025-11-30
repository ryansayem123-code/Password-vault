import numpy as np

ages = np.array([[21,33,18,19,20,21,33,28,43],
                 [30,15,17,17,18,19,21,37,41]])

teenagers = ages[ages < 18]
adults = ages[(ages < 18) | (ages >= 40)]
evens = ages[(ages % 2 != 0)]
nigga = np.where(ages > 18,ages, np.nan)  
print(nigga)
