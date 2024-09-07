import statistics
def input_data():
    n=int(input())
    numbers_list=[]
    while (n != 0):
        numbers=input().strip()
        numbers=numbers.split(" ")
        numbers=list(map(int,numbers))
        numbers_list.append(numbers)
        n-=1
    return numbers_list
def Medium(numbers):
    output=[]
    for numbers_in in numbers:
        output.append(statistics.median(numbers_in))
    output=list(map(str,output))
    return "\n".join(output)

numbers_given=input_data()
print(Medium(numbers_given))