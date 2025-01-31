# nums = [1,2,1]

# def concatNum(num):
#     # cnum = num*2
#     # return cnum
#     ans = []
#     for i in range(2):
#         for i in num:
#             ans.append(i)
#     return ans

# print(concatNum(nums))

# nums = [1,2,3,1]
# h_num = {}
# count = 1
# def dup(num):
#     for i in num:
#         if i in h_num:
#             return True
#         else:
#             h_num[i] = count
#     return False

# print(dup(nums))


# s = "anagram"
# t = "nagaram"

# def anagram(s,t):
#     if len(s) != len(t):
#         return False
    
#     s_hash,t_hash = {},{}

#     for i in range(len(s)):
#         s_hash[s[i]] = 1 + s_hash.get(s[i],0)
#     return


# print(anagram(s,t))