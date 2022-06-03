
def search(p,d,x=0,y=0):
    while p != 1:
        p = p//2
        x+=1
    while d != 1:
        d = d//2
        y+=1
    return x+y

p = int(input(f'Pick-up value as P: '))
d = int(input(f'Destination value as D: '))
print(search(p,d))

