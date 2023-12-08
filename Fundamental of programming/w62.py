def input_integers():
    input_string = input("Give integers separated by comma:\n")
    input_char = input_string.split(",")
    list_int = []
    for ch in input_char:
        list_int.append(int(ch))
    return  list_int

def sorted_list(nums: list):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if(nums[j]>nums[j+1]):
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                
    return nums

num = input_integers()
index = input("Give an integer:\n")
ans = sorted_list(num) 
if(int(index)<=int(len(num))):
    print(str(index)+"th smallest element is",ans[int(index)-int(1)])
else:
    print("Not suitable")