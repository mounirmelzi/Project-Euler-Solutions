# func to check if n isn't dev by nums from 1 to 20
def func (n) :
    for i in range (11 , 21):
        if n % i != 0 : return True
    return False

x = 20 
while func (x) : x += 20
print(x)
