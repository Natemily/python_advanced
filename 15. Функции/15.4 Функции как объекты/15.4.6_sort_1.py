def sum_of_digits(number):
    return sum(int(digit) for digit in number)


numbers = input().split()
    
sorted_numbers = sorted(numbers, key=sum_of_digits)
    

print(" ".join(sorted_numbers))

