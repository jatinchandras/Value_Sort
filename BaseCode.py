#ValueSort 
def Value_Sort(x_input):
    x_input=x_input.split()
    y_list = [None] * len(x_input)
    for a in x_input:
        count_equal=0
        count_lessthan=0
        for b in x_input:
            if int(b)<int(a):
                count_lessthan+=1 
            elif int(b)==int(a):
                count_equal+=1 
        for r in range(count_equal):
            y_list[count_lessthan+r]=a
    return(y_list)


x_input = input("Enter a series of values: ")
print("The Sorted list: ", Value_Sort(x_input))

#space complexity = O(2n)
#time complexity = O(n^2)
