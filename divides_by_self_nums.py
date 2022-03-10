limit = int(input())


for num in range(1, limit+1):
    num_copy = num
    while True:
        last_digit = num % 10
        
        if last_digit == 0 or num % last_digit != 0:
            break
        
        if num_copy == num:
            print(num, end=" ")
        
        num = num // 10
