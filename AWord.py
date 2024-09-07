"""
A. Word
time limit per test2 seconds
memory limit per test256 megabytes
Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

Input
The first line contains a word s — it consists of uppercase and lowercase Latin letters and possesses the length from 1 to 100.

Output
Print the corrected word s. If the given word s has strictly more uppercase letters, make the word written in the uppercase register, otherwise - in the lowercase one.

Examples
InputCopy
HoUse
OutputCopy
house
InputCopy
ViP
OutputCopy
VIP
InputCopy
maTRIx
OutputCopy
matrix

"""
input_text=input().strip()
input_text_list=list(input_text)

uppercases=[uppercase for uppercase in input_text_list if uppercase.isupper()]
lowercases=[lowercase for lowercase in input_text_list if lowercase.islower()]
if len(uppercases)>len(lowercases):
    print(input_text.upper())

elif len(uppercases)<len(lowercases):
    print(input_text.lower())
else :
    print(input_text.lower())


