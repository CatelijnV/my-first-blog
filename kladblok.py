print("hello, Django girls")
if 3>2:
    print("it works")
    if 5>2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi(name):
    print('Hi ' + name + '!')

girls = ['monica','cat']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1,6):
    print(i)
for a in range(1,9):
    print(a)
    
