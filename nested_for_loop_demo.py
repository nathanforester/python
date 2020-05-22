# xVal = [0, 1, 2]
# yVal = [0, 1, 2]
#
# for x in xVal:
#     for y in yVal:
#         print(x, y)


n1 = []
for x in range(1500, 2701):
     if(x%7==0) & (x%5==0):
         n1.append(str(x))

print(','.join(n1))
