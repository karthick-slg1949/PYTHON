def test_list(lst):
    test_list = [34, 56, 78, 98]
    print("The original list is:", lst(test_list))
    
    res = []
    
    for ele in test_list:
        summation = 0
        for digit in str(ele):
            summation += int(digit)
        res.append(summation)
            
    print("List integer summation:",res)

test_list(str)