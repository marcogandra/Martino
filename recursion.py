def factorial(x):
  	if x == 1:
    	return 1
  	else: 
    	return x * factorial(x-1) 

print(factorial(5))
'''
start
Line - Description
7 - start the function called on function print
1 - cath function 'factorial' and the arg '5'
# 2 - if 5 == 1: 
# 3 - return 1
# 4 - else:
5 - return 5 * function 'factorial' with arg '5-1'
# two thinks happens above:
# 1 - first, like other function independently, 'fatorial(x-1)' will be return just 5-1, thats 4.
# 2 - than function 'def factorial(x)' it returns 5 * 4, that its 20 and will be storage in local memory.
# this recursive function is working like while loop 
# and the return statement its working like yield(just to understand why dont stop when 'return')
1 - goes to line 1 again, but now the arg of function 'factorial' is '20'
# the 'x' of line 2 makes reference from function 'factorial(x-1)'
# so, just be called, when this function gets 1 as return
5 - return 20 * function 'factorial' with arg '4-1'
# first, function 'factorial(x-1)' return 3.
# than the function 'def factorial(x)' will return 20 * 3, that its 60.
1 - goes to line 1 again, but now the arg of function 'factorial' is '60'
5 - return 60 * function 'factorial' with art '3-1'
# first, function 'factorial(x-1)' return 2.
# now the function 'def factorial(x)' will return 60 * 2, thats 120.
1 - goes to line 1 again, but now the arg of function 'factorial' is '120'
5 - return 120 * function 'factorial' with art '2-1'
# first, function 'factorial(x-1)' return 1.
# if u remember, the 'x' on line 2 references to arg on function 'factorial(x-1) being the result of 'x-1', thats 1 now
# so, now, because the function 'factorial(x-1) returns 1, this makes the function 'def factorial(x)' return to line 2
2 - confirm the 'if' statement
3 - return 1 
# now the function 'def factorial(x)' will return 120 * 1, thats 120.
# both functions @factorial(x-1) and @factorial(x) will end after that
7 - finish printing the factorial of 5
Output:
120	
stop
'''