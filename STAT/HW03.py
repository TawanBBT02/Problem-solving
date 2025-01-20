import HW02
import math
data2 = [80,45,67,99,73,21,60]
ave =  HW02.average(data2)
sd = HW02.standard_deviation(data2)
sq = math.sqrt(len(data2))
t = (float(format(ave,'.2f')) - 50)/float(format(float(format(sd,'.2f'))/float(format(sq,'.2f')),'.2f'))
print(format(sd,'.2f'))
print(float(format(ave,'.2f')),float(format(sd,'.2f')),format(sq,'.2f'),t)
