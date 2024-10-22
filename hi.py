nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
length = len(nums[0])
l = []
l1 = []
score = 0
for i in range(len(nums[0])):
    for j in range(len(nums)):
        k = max(nums[j])
        l.append(k)
        nums[j].remove(k)
    score += max(l)
    l = []
print()




    