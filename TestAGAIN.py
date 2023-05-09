import random

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
times = input("¿cuantos caracteres quieres?")
alltext = "error!"
error = False

if times.isnumeric() == False:
    print("error!")
    error = True

if error == False:
    if int(times) > 0:
        alltext = ""
    for i in range(int(times)):
        randomitem = random.choice(a)
        alltext = alltext + randomitem
    print(alltext)
