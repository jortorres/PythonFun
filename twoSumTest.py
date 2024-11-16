def twoSum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return[i,j]
    return None

arr = [2,6,5,8,4]
target = 8

print(twoSum(arr,target))

print("\ndef twoSum(arr,target): \nfor i in range(len(arr)): \n for j in range(i+1, len(arr)): \nif arr[i] + arr[j] == target: \n return[i,j] \nreturn None")



            
    