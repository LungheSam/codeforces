"""
A. Petya and Strings
time limit per test2 seconds
memory limit per test256 megabytes
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

Examples
InputCopy
aaaa
aaaA
OutputCopy
0
InputCopy
abs
Abz
OutputCopy
-1
InputCopy
abcdefg
AbCdEfF
OutputCopy
1
"""
# words=[]
# for i in range(2):
#     input_word=input()
#     words.append(input_word)
# def find_output(words):
#     if words[0].lower()==words[1].lower():
#          return '0'
#     # for i in range(len(words[0])):
#     #     if words[0][i].lower()==words[1][i].lower():
#     #         continue
#     #     else:
#     #         if ord(words[0][i].lower())>ord(words[1][i].lower()):
#     #             return '-1'
#     #         else:
#     #             return '1'
#     if words[0].lower()>words[1].lower():
#         return '-1'
#     if words[0].lower()<words[1].lower():
#         return '1'


# print(find_output(words))
# Read input strings
string1 = input().strip()
string2 = input().strip()

# Convert both strings to lowercase
string1 = string1.lower()
string2 = string2.lower()

# Compare the strings lexicographically
if string1 < string2:
    print("-1")
elif string2 < string1:
    print("1")
else:
    print("0")

            
            
        
