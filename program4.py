def count_multiples(numbers, given_set):
    count_dict = {num:0 for num in given_set }

    for num in numbers:
        for divisor in given_set:
            if num % divisor == 0:
                count_dict[divisor] +=1

    return count_dict
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
given_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

counts = count_multiples(numbers, given_set)
print("Output:", counts)