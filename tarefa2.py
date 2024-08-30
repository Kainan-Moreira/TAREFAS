def pertence_a_fibonacci(numero):
  
    a, b = 0, 1
    
    fibonacci = [a, b]

   
    while b < numero:
        a, b = b, a + b
        fibonacci.append(b)

   
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."
    
numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

print(pertence_a_fibonacci(numero_informado))

#Rode o código e insira o numéro que desejar no terminal