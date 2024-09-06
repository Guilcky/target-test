def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1 
    
    while len(fibonacci_series) < n:
        fibonacci_series.append(a)
        a, b = b, a + b
        
    return fibonacci_series

try:
    n = int(input("Digite um número para calcular a série de Fibonacci: "))
    if n <= 0:
        print("Por favor, digite um número positivo.")
    else:
        result = fibonacci(n)
        print(f"Série de Fibonacci até o {n}-ésimo termo: {result}")
        
    verificar_numero = int(input("Digite um número para verificar se está na série de Fibonacci: "))
        
    if verificar_numero in result:
            print(f"O número {verificar_numero} está na série de Fibonacci.")
    else:
     print(f"O número {verificar_numero} não está na série de Fibonacci.")      
except ValueError:
    print("Por favor, digite um número válido.")
   