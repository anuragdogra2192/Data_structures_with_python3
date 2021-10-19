#Advancing through an array.
def can_reach_end(L):
    furthest_reach_so_far, last_index = 0, len(L) - 1
    i = 0
    jumps = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        print(i)
        print(furthest_reach_so_far, end=" ")
        print(L[i]+i)
        furthest_reach_so_far = max(furthest_reach_so_far, L[i] + i)
        jumps = i
        i += 1
    return furthest_reach_so_far >= last_index

print("Provide the array of ints to advance: \n")
L = [int(x) for x in input().split()]
print("Did we advance the till the end: ", can_reach_end(L))
