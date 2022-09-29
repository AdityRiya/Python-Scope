x = 25 
def my_func():
    x = 30 
    return x
#the function is not called that's why X's value is not updated
print(x)
#function is called , can you guess the output?

my_func()
print(x)
#and now.....check the output again....
print(my_func())