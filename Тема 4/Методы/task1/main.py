def get_list_number_divisors(number):
      # TODO найти список делителей числа number
    list_ = []
    for division in range(1, number+1):
        if number % division == 0:
            list_.append(division)

    return list_

print(get_list_number_divisors(17))
print(get_list_number_divisors(2 ** 16))
