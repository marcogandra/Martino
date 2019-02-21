def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def decor1(func):
    def wrap1():
        print("**************")
        func()
        print("**************")
    return wrap1
    
@decor
@decor1 
def print_text():
    print("Hello world!")

print_text()
'''
what happens line by line
start - hope be correct. sorry about the english.
#line 20 calls the function 'print_text()' on line 15, like 'print_text = decor(print_text)' on exercise before.
20 - program stars on line 20
#'@decor' == 'print_text = decor(print_text)'
15 - calls @decor, which means start function decor with the function below 'def print_text()'
# the function decor have another function called 'wrap'. what happens? func 'wrap' just start to run when 'return wrap' is called.
# so, the function is there first, just to be called on local space, not global. so just use memory if realy necessary.
6 - return for function wrap. looks like a loop.
2 - start function wrap
3 - print
# after print, will start a function. now, at this time occour something like yield on the function wrap. because the function wrap stops there and will return later.
4 - start function func()
1 - decor(func) = decor(print_test)
# than, what funcion will start? the function described on line 1 'func'.  what 'func' calls? 'func' call the function below @decor, witch is 'def print_text'.
15 - like yield, function 'decor' yield here and go to next line of program
# @decor1 starts the same procedure of @decor, but using function 'def decor1(func)'
16 - calls @decor1, which means start function decor1
13 - return for function wrap1, like a loop.
9 - start function wrap1
10 - print
11 - start function func()
16 - like yield, function 'decor1' yield here and go to next line of program
# so, finnaly, after starts @decor and @decor1, whill start function 'print_text()'
17 - start function print_text()
18 - print
# than will continue de functions @decor and @decor1. remember, the functions use 'return', but works like 'yield'
15 - return to continue the function @decor
5 - print
# this is the 'real last line' of this functions @decor and @decor1
15 - close function and pass to the next line
16 - @decor1 will do the same as @decor
12 - print
# nothing more to do. after closing @decor1, the program finish.
16 - close function @decor1.
stop
'''