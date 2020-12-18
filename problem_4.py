def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    left = 0
    right = len(input_list) -1

   
    while index <= right: #with this condition we avoid messing with already sorted 2 numbers at right
      
        if input_list[index] == 2:   #check if the element is 2
                      
            input_list[index], input_list[right] = input_list[right], input_list[index] 
            right-=1 # increment right index, to put next number 2 found in the list
            #this condition will not increment the var index, to not left any number 2 behind
        
        elif input_list[index] == 0: #check if the element is 0
            input_list[index], input_list[left] = input_list[left], input_list[index] 
            left+=1 # increment the left index, to put next number 2 found in the list
            index+=1  # the array will be incremented, to avoid passing other number that is not 0 to the left
        else:
            index+=1 #when the element is 1, just increment the array
     
    return input_list 



def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0,1])
#[0, 1]
test_function([2,2,2,2,1,2,2,2,2])
#[1, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([])
#[]