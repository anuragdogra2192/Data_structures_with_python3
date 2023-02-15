#Remove the duplicates in the sorted array and return the number of the valid entries.

def delete_duplicates(L):
    if not L:
        return 0
    
    write_index = 1
    for i in range(1, len(L)):
        if L[write_index - 1] != L[i]:
            L[write_index] = L[i]
            write_index += 1
    
    print(" The array after deleting occurrences: ", L)
    return write_index

print("Provide the sorted array with multiple occurrences \n")
print("For example: 1 1 2 3 3 4 4 4 4 5 9 9 9")
L = [int(x) for x in input().split()]

  
num_of_valid_entries = delete_duplicates(L)

print("Number of valid entries: ", num_of_valid_entries)