def sum_of_digits(number):
    return sum(int(digit) for digit in number)

def sort_key(number):
    return (sum_of_digits(number), int(number))


numbers = input().split()

sorted_numbers = sorted(numbers, key=sort_key)
    

print(" ".join(sorted_numbers))
