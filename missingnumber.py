import array

def missingnumber(given_list):

    start = given_list[0]
    end = given_list[len(given_list)-1]

    actual_list = list(range(start,end+1))
    actual_sum = sum(actual_list)
    given_sum = sum(given_list)
    return actual_sum-given_sum

arr = array.array('b',[1,2,3,5,6,7,8,9,10])    
print("Missing Number: ",missingnumber(arr))