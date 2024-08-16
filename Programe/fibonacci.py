def fibonacci(n):
    fib_sequence=[0,1]
    for i in range(2,n):
        fib_sequence.append(fib_sequence[-1]+ fib_sequence[-2])
        return fib_sequence

    num_terms=int(input("Enter the number of terms: "))
    fib_sequence=fibonacci(num_terms)
    print("Fibonacci sequense up to",num_terms,"terms:",fib_sequence)