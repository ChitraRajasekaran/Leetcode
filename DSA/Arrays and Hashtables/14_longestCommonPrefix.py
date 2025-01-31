strs = ["flow","flower","flight"]
# print(len(strs[0])) --> 4

# def com(strs):
#     for i,j in enumerate(strs):
#         for k in j:
#             for s in i+1[s]:
#                 if k == s:
#                 else:
#                     return False

def com(strs):
 res = ""
 for i in range(len(strs[0])):
    # print(strs[0][i]) --> flow
    for s in strs:
    #   print(s[i]) --> ffflllooiwwg
        if i == len(s) or s[i] != strs[0][i]:
           return res
    res = res + strs[0][i]
 return res
print(com(strs))

