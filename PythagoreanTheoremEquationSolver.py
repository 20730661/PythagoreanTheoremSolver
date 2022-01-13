import math
#Made By 20730661
print("------------------------------------------------------------")
print("Made By 20730661")
print("------------------------------------------------------------")
print("Solving for the hyp, leg A (vertical) or leg B (horizantal)?")
print("(Please input your response as shown above.)")
response= input(">>")

if response == "hyp":
    print("------------------------------------------------------------")
    print(".............Solving for the hypothnuse.............")
    print("------------------------------------------------------------")
    print("Please input the value of varible A")
    a=int(input(">>"))
    print("please input the value of varible B")
    b=int(input(">>"))

    x=a**2
    y=b**2

    c= x+y

    answer=math.sqrt(c)
    print("varible C is:")
    print(answer)
    print("------------------------------------------------------------")
else:
    if response == "leg B":
        print("------------------------------------------------------------")
        print(".............Solving for the leg B.............")
        print("------------------------------------------------------------")
        print ("please input the value of varible A")
        b2= int(input(">>"))

        print ("please input the value of varible C / hypothnuse.")
        c2= int(input(">>"))

        b3=b2**2
        c3=c2**2

        a2=c3-b3

        answer2= math.sqrt(a2)

        print(answer2)

        print("------------------------------------------------------------")

    else:
        if response == "leg A":
            print("------------------------------------------------------------")
            print(".............Solving for the leg A.............")
            print("------------------------------------------------------------")
            print ("please input the value of varible B")
            b4=int(input(">>"))

            print ("please input the value of varible C / hypothnuse.")
            c4= int(input(">>"))

            b5=b4**2
            c5=c4**2

            a3=c5-b5

            answer3= math.sqrt(a3)

            print(answer3)

            print("------------------------------------------------------------")
