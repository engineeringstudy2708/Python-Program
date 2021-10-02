import dis

def tuple():
    tuple1=(1,12,30,2.3)
    print(tuple1)
def list():
    list1=[1,12,30,2.3]
    print(list1)
print("This is for tuple:")
print(dis.dis(tuple))

print("This is for list:")
print(dis.dis(list))

tuple()

list()
