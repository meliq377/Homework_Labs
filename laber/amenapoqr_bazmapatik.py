def amenapoqr_bazmapatik(x, y):

   if x > y:
       mecy = x
   else:
       mecy = y

   while(True):
       if((mecy % x == 0) and (mecy % y == 0)):
           res = mecy
           break
       greater += 1

   return res