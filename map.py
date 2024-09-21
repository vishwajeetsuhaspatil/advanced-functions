n= [1,2,3]
n2= [4,5,6]
result= map(lambda x,y: x + y, n,n2)
print(list(result))

a= [1,2,3,4]
def sq(a):
    return a*a
square= list(map(sq,a))
print(square)