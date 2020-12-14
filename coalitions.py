# Created by David Shuster
# Last updated on 8 October, 2020

# Generates a list of non-empty coalitions
# TODO: Look into using an unordered data structure instead of lists.

def combine(lst1, lst2):
    combined_list = list(frozenset(lst1).union(frozenset(lst2)))
    return combined_list

# take in a list S, and return a list containing all non-empty lists that can be made from the elements in S
def list_of_lists(S):
    if len(S)==1:
        return [S]
    big_list=[]
    pivot = S.pop()
    big_list.append([pivot])
    list_sans_pivot = list_of_lists(S)
    for i in list_sans_pivot:
        big_list.append(combine([pivot],i))
        big_list.append(i)
    return(big_list)

def main(): # main simply contains a small example of coalitions.py's capabilities
    S = ["Libertarian", "Green", "American Solidarity"]
    LoL=list_of_lists(S)
    print(LoL)
    print(len(LoL), "coalitions")

if __name__ == '__main__':
    main()