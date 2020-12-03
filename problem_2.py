def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list)==0:
        return -1

    start_index = 0
    end_index = len(input_list)

    middle = (start_index + end_index)//2
     
    #check if the number in middle is number that you are looking for
    if number == input_list[middle]:
        return middle    

    #split the list in two
    ar1 = input_list[start_index: middle]
    ar2 = input_list[middle +1: ]
    selected_array = []

    #check if the number could be between array values 
    if number >=ar1[0] and number <=ar1[len(ar1)-1]:
        selected_array = ar1
    elif number >=ar2[0] and number <=ar2[len(ar2)-1]:
        selected_array = ar2

    start = 0
    end = len(selected_array) -1

    #search for the number
    while start <= end:

        mid = (start + end)//2

        if number == selected_array[mid]:
            if selected_array is ar2:
                return mid + middle +1 
            else:
                return mid

        if number < selected_array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    #if the number is not found return -1
    return -1

   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#"Pass"
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#"Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#"Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#"Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#"Pass"
test_function([[6, 7, 8, 1, 2, 3, 4], 5])
#"Pass"
test_function([[], 1])
#"Pass"