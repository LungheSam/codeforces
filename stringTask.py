def filterFunction(txt):
    return txt not in ['a','e','i','o','u','y']
text=input().strip().lower()
text_list=list(text)
text_consonants=list(filter(filterFunction,text_list))
text_consonants=["."+txt for txt in text_consonants]
print("".join(text_consonants))

