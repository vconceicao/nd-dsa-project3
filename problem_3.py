def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    

    if len(input_list) == 0:
        return [0,0]

  

    sorted_array = mergesort(input_list)


    # concat major numbers
    # check if the position is even or odd
    index = 0
    max_num1 = ''
    max_num2 = ''
    while index <len(sorted_array):
    # if it is even concat it to the first string
        if index%2==0:
            max_num1+=str(sorted_array[index])
        else:
            max_num2+=str(sorted_array[index])
        index+=1


    # else concat it in the second string 

    return [int(max_num1), int(max_num2)]

def mergesort(input_array):

    if len(input_array) <=1:
        return input_array

    start_index = 0
    end_index = len(input_array) 
    midpoint =  (start_index + end_index)//2

    left = input_array[:midpoint]
    right = input_array[midpoint:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    left_index = 0
    right_index = 0
    merged_array=[]

    while left_index < len(left) and right_index < len(right):

        if right[right_index] > left[left_index]:
            merged_array.append(right[right_index])
            right_index+=1
        else:
            merged_array.append(left[left_index])
            left_index+=1
    
    merged_array+=left[left_index:]
    merged_array+=right[right_index:]

    return merged_array

    
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[], [0,0]]
test_case4 = [[1,2], [2, 1]]
test_case5 = [[2,5,7,0], [72,50]]

test_function(test_case1)
#[542, 31]
test_function(test_case2)
#[964, 852]
test_function(test_case3)
#[0, 0]
test_function(test_case4)
#[2, 1]
test_function(test_case5)
#[72,50]
