def twoSum(arry, target):
    for i in range(len(arry)):
        for k in range(i + 1,len(arry)):
            if target == arry[i] + arry[k]:
               return (i,k)
    return None

def sort(arrySort):
   
   n = len(arrySort)
   
   for i in range(n):
       for j in range(0,n-i-1):
        if arrySort[j] > arrySort[j+1]:
            #swap if the array is greater then the next element
            arrySort[j], arrySort[j+1] = arrySort[j+1], arrySort[j]
       print(f'Array after pass {i + 1}: {arrySort}')
   return arrySort # return array
    
    
    




num = [6528,1,5,100,5,6102,7]
tar = 8
print('Hello')
print(twoSum(num,tar))
print('After funciton')

print(sort(num))

