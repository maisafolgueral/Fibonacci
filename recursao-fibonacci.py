'''Os números de Fibonacci correspondem à seguinte sequência de números naturais:
 1 1 2 3 5 8 13 ...
A regra de formação desta sequência é muito simples: exceto para os dois números iniciais (0 e 1), todos os outros números são a soma dos números imediatamente anteriores na sequencia.

(a) Proponha uma regra recursiva para definir o n-ésimo número de Fibonacci.'''
# Regra: fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n - 2)

'''(b) Implemente uma função recursiva que calcule o n-ésimo número de Fibonacci e a teste dentro do programa.'''

def fibonacci(n):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

n = int(input('Digite um número: '))
print(fibonacci(n))

'''(c) Faça um diagrama de execução das chamadas recursivas de sua implementação para calcular o 5-ésimo número de Fibonacci.'''
#fibonacci(5) --> 5
#                fibonacci(4) --> 3         +         fibonacci(3) --> 2
#       fibonacci(3) + fibonacci(2) --> 2+1 + fibonacci(2) + fibonacci(1)
#           fibonacci(2) + fibonacci(1)   +      1       +      1
#               1        +     1
    

