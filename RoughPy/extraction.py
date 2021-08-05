# =============================================================================
# import re
# f=open(r"C:\Users\91962\Downloads\regex_sum_677367.txt","r")
# x=[]
# y=[]
# sum=0
# for line in f:
#     y=re.findall('[0-9]+',line)
#     for i in range(len(y)):
#         x.append(y[i])
# for i in range(len(x)):
#     sum += int(x[i])
# print(sum)
# 
# =============================================================================

import re
email="552001mahesh@gmail.com"
org=re.findall('@([^ ]+)',email)
print(org[0])