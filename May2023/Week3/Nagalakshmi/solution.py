
num_cases = int(input())

# Iterate through each test case
for _ in range(num_cases):
    try:
        # Read the two values
        a, b = input().split()
        
        # Perform integer division
        result = int(a) // int(b)
        
        # Print the result
        print(result)
    
    except ZeroDivisionError as e:
        # Print the error code for ZeroDivisionError
        print("Error Code:", e)
    
    except ValueError as e:
        # Print the error code for ValueError
        print("Error Code:", e)
