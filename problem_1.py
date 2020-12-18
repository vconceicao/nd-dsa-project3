def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0 :
        return None

    if number == 0 or number ==1:
        return number

    start = 0
    end = number
    while start<=end:
        mid = (start + end)//2
        sqr_mid = mid*mid
        sqr_next = (mid+1)*(mid+1)
        if between(number, sqr_mid, sqr_next):
            return mid
        if number < sqr_mid:
            end = mid -1
        else:
            start = mid+1

def between(number, sqr_mid, sqr_next):
    return number >= sqr_mid and number < sqr_next


print ("Pass" if  (3 == sqrt(9)) else "Fail") 
#3
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#0
print ("Pass" if  (4 == sqrt(16)) else "Fail")
#4
print ("Pass" if  (1 == sqrt(1)) else "Fail")
#1
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#5
print ("Pass" if  (16 == sqrt(256)) else "Fail")
#16
print ("Pass" if  (None is sqrt(None)) else "Fail")
#None