"""
A. Way Too Long Words
time limit per test1 second
memory limit per test256 megabytes
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

Output
Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

Examples
InputCopy
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
OutputCopy
word
l10n
i18n
p43s
"""

def input_data():
    n=int(input())
    words=[]
    while (n != 0):
        word_1=input()
        words.append(word_1)
        n-=1
    return words
def abbreviate(word):
    if len(word)>10:
        return f"{word[0]+str(len(word)-2)+word[len(word)-1]}"
    else:
        return word
def return_abbr():
    words=input_data()
    abbreviations=[]
    for i in range(len(words)):
        abbreviations.append(abbreviate(words[i]))
    return "\n".join(abbreviations)

print(return_abbr())