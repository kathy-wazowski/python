#for loop
nums = [1,2,3,4,5.3,5,4,5]
for num in nums:
    print(num)

#break
for num in nums:
    if num==5.3:
        break; #jump out of the whole loop
    print(num)

#continue
for num in nums:
    if num==5.3:
        continue; #jump out of the current loop
    print(num)

#nest loops
nums = [10,9,8,7,6,5]
word = "abc"
for num in nums:
    for letter in word:
        print(num, letter)

#range()
for i in range(10):
    print(i) # print 0 - 9

for i in range(1, 11):
    print(i) # print 1-10

# while loop
num = 0
while num < 10:
    if(num == 5):
        break
    print('while ', num)
    num += 1