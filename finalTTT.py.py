from winner import winner


list1=[1,2,3,4,5,6,7,8,9]


def board():
    
    print(list1[0], " | " ,list1[1] ," | " ,list1[2])

    print(list1[3]," | " ,list1[4]," | " ,list1[5])

    print(list1[6]," | " ,list1[7]," | " ,list1[8])

w=True
p1=True

total=0
while(w):
        
        if(p1):
            print(board())
            try:
                
                print("player 1=")
                pos=int(input("enter the position"))
                if(0<pos<10):
                
                    if(list1[pos-1]=="x" or[pos-1]== "0"):
                        print("already occupied")
                        continue
                    else:
                        list1.insert(pos-1,"x")
                        list1.pop(pos)
                        board()
                        t=(winner(list1))
                        if(t=="player 1 winner"):
                            print(t)
                            w=False
                            continue
                        total=total+1
                        if(total==9):
                            print("Tie")
                            break

                        p1=False
  
                else:
                    print("choose valid option")

            except:
                print("enter valid input")

        else:
            p2=True
            if(p2):
                try:
                    print("player 2=")
                    pos=int(input("enter the position"))
                    if(0<pos<10):
                
                        if(list1[pos-1]=="0" or list1[pos-1]=="x"):
                            print("already occupied")
                            continue
                        else: 
                            list1.insert(pos-1,"0")
                            list1.pop(pos)
                            board()
                            t=(winner(list1))
                        
                            if(t=="player 2 winner"):
                                print(t)
                                w=False
                                continue
                            total=total+1
                            if(total==9):
                                print("Tie")
                                break
                        
                            p1=True
                            continue        
                    else:
                        print("enter valid input")
                        continue
                except:
                    print("enter valid input")
else:
    print("thankx for playing")
                
