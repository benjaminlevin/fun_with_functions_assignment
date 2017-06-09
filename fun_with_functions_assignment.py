#odd/even
def odd_even():
    for z in range(1,2001):
        if (z%2) == 0:
            print ("Number is " + str(z) + '. This is an even number.')
        else:
            print ("Number is " + str(z) + '. This is an odd number.')
odd_even()

#multiply
a = [2,4,10,16]
def multiply(a,y):
    i = 0
    c = []
    while i < len(a):
        a[i]=(a[i]*y)
        i = i + 1
    return a
b = multiply(a,5)
print b

#hacker challenge
def layered_multiples(arr):
    new_array = []
    i = 0
    while i < len(arr):
        new_array.append([1]*arr[i])
        i = i + 1
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
