class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        word = ""

        for n in range(min(i,j)):
            word += word1[n]
            word += word2[n]

        if i<j:
            word += word2[n+1:]
        if j<i:
            word += word1[n+1:]

        return word


# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         i = len(word1)
#         j = len(word2)
#         word = []

#         for n in range(min(i,j)):
#             word.append(word1[n])
#             word.append(word2[n])

#         if i<j:
#             word.append(word2[n+1:])
#         if j<i:
#             word.append(word1[n+1:])
        
#         return "".join(word)