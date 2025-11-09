#s is the array nums
#n is the target
def find(s, n):
    rounds = len(s) - 1
    first_index = 0
    second_index = 1
    for i in range(rounds): #0, 1, 2
        for j in range(1+i,len(s)): #1,2,3
            sum = s[i] + s[j]
            if sum == n:
                first_index = i
                second_index = j
                break
    return [first_index, second_index]        

nums = [2,7,11,15]
target = 9 
print(find(nums,target))
    

