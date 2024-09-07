
# n_k=input().strip().split()
# n_k=list(map(int,n_k))
# sequence_odd=[n for n in range(1,n_k[0]+1,2) ]
# sequence_even=[n for n in range(2,n_k[0]+1,2) ]
# sequence=sequence_odd+sequence_even
# print(sequence[n_k[1]-1])
def find_kth_number(n, k):
    odd_count = (n + 1) // 2  # Number of odd numbers in the sequence
    
    if k <= odd_count:
        # k-th number is among the odd numbers
        return 2 * k - 1
    else:
        # k-th number is among the even numbers
        return 2 * (k - odd_count)

# Read input
n, k = map(int, input().split())

# Print the k-th number in the sequence
print(find_kth_number(n, k))


