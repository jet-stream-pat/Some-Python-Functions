def compute_bill(bill): # the function 'compute_bill' is defined and takes one parameter/argument called 'bill'
    total = 20 + bill # inside the funtion 'bill', 'total = 20 + bill' creates a new variable called 'total'. 'Total' adds together '20' with the 'bill' parameter
    return total # return total means that the function 'compute_bill' is exited and will return the value of 'total' back to where the function was called
total_bill = compute_bill(3.20) # 'total_bill = compute_bill(3.20)' calls the compute_bill function w/ 3.20 as the argument. This passes 3.20 into the bill parameter of function
print(total_bill) # returns 23.2 into console
