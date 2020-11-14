# Session 1 - Nov. 13th 2020

# #define factorial function
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

#define permutation function - factorials
def fact_permutation1(n, k):
    return int(factorial(n) / factorial(n-k))

#second definition from Tovio (prep class) - don't totally understand
def fact_permutation2(n,k):
    perm = 1
    for i in range(n,  n-k, -1):
        perm *= i
    return perm

#define permutation function - falling power
def fall_permutation(n, k):
    prod = 1
    for num in range(n-k+1, n+1):
        prod *= num
    return prod
#the above definition makes more sense now

#define combination fucntion with factorials
def fact_combination(n, k):
    return int( factorial(n) / (factorial(k) * factorial(n-k)))

#define combination function with falling power
def fall_combination(n, k):
    numer = 1
    denom = 1

    for num in range(n, n-k, -1): #I see now that doing it this way makes it noninclusive for n-k
        numer *= num

    for num in range(1, k+1):
        denom *= num

    return int(numer / denom)

#testing

print(f'factorial 5 (120): {factorial(5)}')


print(f'50P3 fact_permutation1 (117600): {fact_permutation1(50, 3)}')
print(f'50P3 fact_permutation2 (117600): {fact_permutation2(50, 3)}')
print(f'50P3 fall_permutation (117600): {fall_permutation(50, 3)}')

print(f'50C3 fact_combination (19600): {fact_combination(50, 3)}')
print(f'50C3 fall_combination (19600): {fall_combination(50, 3)}')


'''
Homework exercise: 
Write a Python progam that generates all alphanumeric passwords of length three 
and stores them in a data structure of your choosing. As a sanity check, make sure 
the number of passwords that are generated matches our answer to the previous exercise. 

Why does this suggest that three character alphanumeric passwords are insecure? 
Paste your code here.
'''
#with dupes, ie. with replacement
def array_of_alphnum_passwords(length_of_pass):
    alph_numer = "abcedfghijklmnopqrstuvwxyz1234567890"

    passwords = []

    for c1 in alph_numer:
        for c2 in alph_numer:
            for c3 in alph_numer:
                passwords.append(c1+c2+c3)
    
    return passwords
    

print(f'Sanity Check: {len(array_of_alphnum_passwords(3))} equals 46,656')
#print(array_of_alphnum_passwords(3))