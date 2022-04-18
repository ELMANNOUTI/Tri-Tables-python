# def tri_bulles(T):
#     n=len(T)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if T[j] > T[j+1]:
#                 temp = T[j]
#                 T[j] = T[j+1]
#                 T[j+1] = temp
#
# T=[5,89,0,-5,8,2,6,1]
#
# tri_bulles(T)
# print(T)


#
# def tri_insrction(T):
#     for i in range(1,len(T)):
#         var = T[i]
#         j=i-1
#         while j>=0 and var<T[j]:
#             T[j+1]=T[j]
#             j-=1
#             T[j+1]=var

#
# def tri_selection(T):
#    for i in range(0,len(T)-1):
#       min = T[i]
#       posmin = i
#       for j in range(i+1,len(T)):
#           if T[j]< min:
#              min = T[j]
#              posmin= j
#
#       temp=T[i]
#       T[i] =T[posmin]
#       T[posmin] = temp
#
# T=[5,8,9,1,2,4,0,98,-1,5,-98,45,4,8,5,4,9,25,3,-4,78,0,8,0,96,45,78,12,9,8]
#
# tri_selection(T)
# print(T)