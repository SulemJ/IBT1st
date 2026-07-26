
# ◆ Easy 
# Write a function fizzbuzz(n) that prints every integer from 1 to n. Print "Fizz" for multiples of 3, 
# "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the number itself otherwise. 
# Example: fizzbuzz(15) should print 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, 
# FizzBuzz. 
# ■ Hint: Check the combined condition (divisible by both 3 and 5) first, before the individual checks

# def fizzbuzz(n):
#     for i in range(1,n+1):
#         if i%3==0:
#             print("Fizz")
#         elif i%5 ==0:
#             print("Buzz")
#         elif i%3==0 and i%5 ==0:
#             print("FizzBuzz")
#         else:
#             print(i)


# fizzbuzz(15)


# count vowels

# def count_vowels(s):
#     vowels= set("A","O","U","I","E", "a", "o", "u", "i", "e")

#     print(sum(1 for i in s if i in vowels))
    # for i in s:
    #     if i in vowels:
    #         summ+=1
    # print(summ)

# count_vowels("PYTHON")


# palindrome

# def check_pali(s):
#     s= s.replace(" ", "")
#     s= s.lower()
#     print(s)
#     print(s==s[::-1])

# check_pali("SA S")




# 04 Find Duplicates
# ◆ Easy–Medium
# Write a function find_duplicates(lst) that takes a list of integers and returns a list of all values that
# appear more than once. The returned list should not itself contain duplicates, and order does not
# matter. Examples: find_duplicates([1, 2, 3, 2, 4, 3, 5]) -> [2, 3] find_duplicates([1, 2, 3]) -> []
# find_duplicates([5, 5, 5]) -> [5]

# from collections import Counter

# def find_duplicates(lst):
#     coun=Counter(lst)
#     print(coun)
#     ans=[]
#     for i,x in coun.items():
#         if x >=2:
#             ans.append(i)

#     print(ans)
#     # {1:1, 2:2, 3:2}

# find_duplicates([1, 2, 3, 2, 4, 3, 5]) 


# Write a function group_anagrams(words) that takes a list of strings and groups words that are
# anagrams of each other (same letters, different order). Return a list of groups (each group is a
# list). Order within groups and order of groups does not matter. Example: group_anagrams(["eat",
# "tea", "tan", "ate", "nat", "bat"]) -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


# def group_anagrams(words):
#     check=[]
#     for i in words:
#         i= "".join(sorted(i))
#         if i not in check:
#             check.append(i)

#     print(check)
#     ans=[]
#     for i in check:
#         temp=[]
#         for j in words:
#             h="".join(sorted(j))
#             if h == i:
#                 temp.append(j)
#         ans.append(temp)
#     print(ans)
        
# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])




# Write a function is_valid(s) that takes a string containing only the characters (, ), {, }, [, ] and
# returns True if the brackets are correctly matched and nested, False otherwise. Examples:
# is_valid("()") -> True is_valid("()[]{}") -> True is_valid("(]") -> False is_valid("([)]") -> False
# is_valid("{[]}") -> True
# ■ Hint: Use a stack. Push opening brackets; when you see a closing bracket, pop the stack and check if it
# matches.

# def is_valid(s):
#     stack=[]

#     for i in s:
#         if i == "(" or i == "{" or i == "[":
#             stack.append(i)
#         elif i == ")" and stack[-1] =="(":
#             stack.pop()

#         elif i == "}" and stack[-1] =="{":
#             stack.pop()

#         elif i == "]" and stack[-1] =="[":
#             stack.pop()


#     print(stack)
#     print(len(stack)==0)

# is_valid("()[]{}")




# Write a function two_sum(nums, target) that takes a list of integers and a target integer, and
# returns the indices [i, j] of the two numbers that add up to the target. You may assume exactly one
# solution exists and you cannot use the same element twice. Examples: two_sum([2, 7, 11, 15], 9)
# -> [0, 1] (2 + 7 = 9) two_sum([3, 2, 4], 6) -> [1, 2] (2 + 4 = 6) two_sum([3, 3], 6) -> [0, 1]
# ■ Hint: A brute-force nested loop is O(n²). Can you solve it in one pass using a dictionary to store numbers you
# have already seen?

def two_sum(nums, target):

    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            print([i, nums.index(target-nums[i])])

two_sum([3, 2, 4], 6)




