with open("test.txt") as f:
    numbers = f.read().splitlines()

numbers = [int(x) for x in numbers]

print(numbers)

def get_sums(width, nums):
    
    for i in range(len(nums)):
        
        sum_array = nums[i-width:i]
        sums = []

        for j in range(len(sum_array)):

            second_sum = sum_array[j:]
            for k in range(len(second_sum)):
                
                s1 = sum_array[j]
                s2 = second_sum[k]
                s = s1 + s2
                if s1 != s2 and s not in sums:

                    sums.append(s)

        if i > width-1 and nums[i] not in sums:
            return nums[i]

n = get_sums(25, numbers)
print("Final Number")
print(n)