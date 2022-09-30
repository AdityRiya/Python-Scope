x = 50
def func():
    global x
    x = 1000
    

print(x)
# use of global variable in a function
func()
print(x)