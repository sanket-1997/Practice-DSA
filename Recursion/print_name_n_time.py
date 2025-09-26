def print_name(name: str, number: int):
    if number ==0:
        return
    print(name)

    print_name(name, number-1)



print_name("Sanket", 1)


#TimeComplexity = O(N)
#SpaceComplexity = O(N) computer's internal stack is used.
