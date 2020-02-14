import Global_Par as Gp
import random
pro = 95
# 距离约接近最大范围 概率越小， 最低概率为90%
def ratio(dis):
   y = (pro-100)/(Gp.com_dis/2)*dis + 100 + (100-pro)
   a = random.uniform(1,100)
   if a <= y:
       return 1
   else:
       return 0
   # return

