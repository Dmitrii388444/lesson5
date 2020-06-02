# проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);

def is_prime(n):
    a = 2
    while n > a:
        if n % a == 0:
            break
        a += 1
    return a == n
print(is_prime(769))

# выводит список всех делителей числа;
def all_dividers(n):
    result = []
    a = 2
    while a * a <= n:
        if n % a == 0:
            n //= a
            result.append(a)
        else:
            a += 1
    if  n > 1:
        result.append(n)
    return result
print(all_dividers(64676476))

# выводит самый большой простой делитель числа.
def greatest_pr_div(n):
    prime_num = all_dividers(n)
    max_num = 0
    for a in prime_num:
        if a > max_num:
            max_num = a
    return(max_num)
print(greatest_pr_div(4971049704))