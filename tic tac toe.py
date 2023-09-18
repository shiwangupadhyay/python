
def display(n1,n2,n3):
    print(n1)
    print(n2)
    print(n3)

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
display(row1,row2,row3)


def user_choice():
    x = input("enter your symbol X/O :")
    if(x == "X"):
        y = "O"
    else:
        y = "X"
    i=1
    while i<10 :
        n = int(input("enter the place you want to put your symbol: "))
        if i==1 or i == 3 or i ==5 or i==7  or i == 9:
            if n==1 :
                row1[0] = x
            elif n == 2:
                row1[1] = x
            elif n==3:
                row1[2] = x
            elif n==4 :
                row2[0] = x
            elif n == 5:
                row2[1] = x
            elif n==6:
                row2[2] = x
            elif n==7 :
                row3[0] = x
            elif n == 8:
                row3[1] = x
            elif n==9:
                row3[2] = x
        elif i == 2 or i==4 or i == 6 or i==8 :
            if n==1 :
                row1[0] = y
            elif n == 2:
                row1[1] = y
            elif n==3:
                row1[2] = y
            elif n==4 :
                row2[0] = y
            elif n == 5:
                row2[1] = y
            elif n==6:
                row2[2] = y
            elif n==7 :
                row3[0] = y
            elif n == 8:
                row3[1] = y
            elif n==9:
                row3[2] = y
        i+=1
        display(row1,row2,row3)
        if(row1[1]==row2[1]==row3[1] == x or row1[1]==row2[1]==row3[1] == y ):
            print(row1[1],"win")
            break
        elif(row1[2]==row2[2]==row3[2] == x or row1[2]==row2[2]==row3[2] == y):
            print(row1[2],"win")
            break
        elif(row1[0]==row2[0]==row3[0] == x or row1[0]==row2[0]==row3[0] == y):
            print(row1[0],"win")
            break
        elif(row1[0]==row1[1]==row1[2] == x or row1[0]==row1[1]==row1[2] == y):
            print(row1[1],"win")
            break
        elif(row2[0]==row2[1]==row2[2] == x or row2[0]==row2[1]==row2[2] == y):
            print(row2[1],"win")
            break
        elif(row3[0]==row3[1]==row3[2] == x or row3[0]==row3[1]==row3[2] == y):
            print(row3[1],"win")
            break
        elif(row1[0]==row2[1]==row3[2] == x or row1[0]==row2[1]==row3[2] == y):
            print(row2[1],"win")
            break
        elif(row1[2]==row2[1]==row3[0] == x or row1[2]==row2[1]==row3[0] == y):
            print(row2[1],"win")
            break
user_choice()