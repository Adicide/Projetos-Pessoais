# Determinador de números primos e compostos

while True:
    n = int(input('Digite um número: '))
    if n < 2:
        print(f'{n} não é primo.\n')
    else:
        primo = True
        divisor = 2
    
    while divisor < n:
        if n % divisor == 0:
            primo = False
        divisor += 1
        
    if primo:
        print(f'{n} é Primo.\n')
    else:
        print(f'{n} não é primo.\n')