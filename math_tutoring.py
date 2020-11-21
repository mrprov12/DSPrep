'''
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
'''
Homework exercise: 
Write a Python progam that generates all alphanumeric passwords of length three 
and stores them in a data structure of your choosing. As a sanity check, make sure 
the number of passwords that are generated matches our answer to the previous exercise. 

Why does this suggest that three character alphanumeric passwords are insecure? 
Paste your code here.
'''
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
'''

##########################################################################################
##########################################################################################
##########################################################################################

#11/18/2020
#Practice Set 1
'''
1. Multiplication Principle (Password Strength)
(a) Write a Python program that generates all alphanumeric passwords of length three
and stores them in a data structure of your choosing. 

(b) As a sanity check, make sure the number of passwords that are generated is what you’d expect based on the multiplication principle.

(c) Why does this suggest that three character alphanumeric passwords are insecure?
'''
#a
def array_of_alphnum_passwords(length_of_pass):
    alph_numer = "abcedfghijklmnopqrstuvwxyz1234567890"

    passwords = []

    for c1 in alph_numer:
        for c2 in alph_numer:
            for c3 in alph_numer:
                passwords.append(c1+c2+c3)
    
    return passwords

#b
print(f'Sanity Check: {len(array_of_alphnum_passwords(3))} equals 46,656')

#c because it takes very little for a computer to test all of the password options


'''2. Factorials
(a) Write a recursive Python function that calculates factorials.

(b) Write an iterative Python function that calculates factorials.

(c) Print the values of 0! through 10! using each function. The values should be the same. (There are more scalable ways to compare values, but it’s instructive to actually inspect the first ten values yourself, to get a sense of how fast the factorial function grows.)

(d) For each of your factorial implementations, find a positive integer input that breaks it. One of the implementations can handle more inputs than the other. Why?
'''

#a: recursive function
#question: defination of recursive? A recursive function is a function that calls itself during its execution.
def rec_factorial(n, prod):
    if n < 0:
        return "Must be a positive number"
    elif n == 0:
        return prod
    else:
        return rec_factorial(n-1, prod*n)

#b: iterative function
def iter_factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

#c: print vals
#print("recursive factorial:")
#for num in range(1,10):
#    print(rec_factorial(num, 1))

#print("iterative factorial:")
#for num in range(11):
#    print(iter_factorial(num))

#d
#print("break: recursive factorial:")
#for num in range(1,1000):
#    print(rec_factorial(num, 1))

#print("break: iterative factorial:")
#for num in range(1001):
#    print(iter_factorial(num))

#recursive breaks first but not sure why


'''3. Permutations
(a) Develop a Python function that computes permutations using one of your factorial implementations from the previous exercise (whichever you think is better).

(b) Develop a Python function that computes permutations using falling powers.

(c) Find an input that breaks the factorial implementation but not the falling power implementation.
'''
#a
#define permutation function - factorials
def fact_permutation(n, k):
    return int(iter_factorial(n) / iter_factorial(n-k))

#b
#define permutation function - falling power
def fall_permutation(n, k):
    prod = 1
    for num in range(n, n-k, -1):
        prod *= num
    return prod

#c
#print(f"break: fact perm: {fact_permutation(500, 444)}")

#print(f"break: fp perm: {fall_permutation(500, 444)}")

#factorial permutation based on iteration factorials breaks, but falling power permutatin does not




'''4. Binomial Coefficients
We call x+y a binomial because it involves two terms. You might recognize binomials from elementary algebra, where we commonly square binomials to get (x+y)^2 = (x+y)(x+y) = x^2 + 2xy + y^2. Notice that the sequence of coefficients in the expanded form is 1, 2, 1. Powers of binomials come up in a lot of places, and it will be instructive to explore them along with their coefficients.

(a) Expand (x+y)^n by hand for n = 0, 1, 2, 3, and 4.

(b) Computing (x+y)^n becomes quite tedious as n grows. So, we’d like to have a general formula for the end result. Can you find a formula for the coefficients? 

Hint: In the expansion of (x+y)^3, if a coefficient equals three, that tells us we have three copies of a particular term. Each of those copies is the result of a different choice when performing the multiplication (x+y)(x+y)(x+y). So, we can reduce the problem of finding coefficients to a problem of counting choices. I think this is a pretty cool observation, since it allows us to use combinatorics to help us with algebra. Neat!

(c) Why might combinations also be referred to as binomial coefficients?

(d) What do you think is the expansion of (x+y)^n? This is an important result called the binomial theorem.
'''




'''5. Combinations
In this problem, we’ll use a bit of programming to help us discover a property of the binomial coefficients. This property provides a useful shortcut for evaluating powers of binomials.
(a) Develop a Python function that computes combinations. You can decide how you want to implement it.

(b) Use your function to print the coefficients of (x+y)^n for n = 0, 1, 2, 3, …10, using one new line for each value of n.

(c) Try to find a pattern in the coefficients computed by your program, and use it to quickly expand (x+y)^11 by hand.

Hint: It may help if you center each line (a.k.a. row) of coefficients so that they form a triangle. This is called Pascal’s triangle. You could do this on paper if you don’t want to bother formatting the output in Python.

(d) State the property you’ve discovered as a general conjecture, and then prove it.
'''
