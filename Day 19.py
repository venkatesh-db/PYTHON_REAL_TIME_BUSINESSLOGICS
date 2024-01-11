
def outer():
    print("outer")
    def inner():
        print("inner")
    return inner

ret =outer()  # outer
ret()              # inner 


raul=lambda: "Hi " + "smile"
ret = raul()
print(ret)

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('don of pythons')

# Output: Hey there, Delilah


def outers():
    print("outers")
    return lambda: "Hi " + "smile"

rets= outers()
ret =rets()
print(ret)


def recursion( obj):
    print(" recrusion")
    if obj == 0:
        return
    recursion(obj-1)

recursion(5)


def coroutine(obj):
    print(" start cororutine")
    while True:
      name=(yield)
      print("received once ",name)
    print("end coroutine" )
 

holiday=coroutine("sankrathi holidays")
holiday.__next__()
holiday.send("1 holi ")
holiday.send("3 holi ")
    





