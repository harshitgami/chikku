def winner(list1):
    if(list1[0]=="x"  and list1[1]== "x"  and list1[2]=="x"):
        return("player 1 winner")
        
    elif(list1[3]=="x" and list1[4]=="x" and list1[5]=="x"):
        return("player 1 winner")
        
    elif(list1[6]=="x" and list1[7]=="x" and list1[8]=="x"):
        return("player 1 winner")
       
    elif(list1[0]=="x" and list1[3]=="x" and list1[6]=="x"):
        return("player 1 winner")
        
    elif(list1[1]=="x" and list1[4]=="x" and list1[7]=="x"):
        return("player 1 winner")
        
    elif(list1[2]=="x" and list1[5]=="x" and list1[8]=="x"):
        return("player 1 winner")
       
    elif(list1[0]=="x" and list1[4]=="x" and list1[8]=="x"):
        return("player 1 winner")
        
    elif(list1[2]=="x" and list1[4]=="x" and list1[6]=="x"):
        return("player 1 winner")
    
    elif(list1[0]=="0"  and list1[1]== "0" and list1[2]=="0"):
        return("player 2 winner")
    
    elif(list1[3]=="0" and list1[4]=="0" and list1[5]=="0"):
        return("playr 2 winner")
    
    elif(list1[6]=="0" and list1[7]=="0" and list1[8]=="0"):
        return("player 2 winner")
    
    elif(list1[0]=="0" and list1[3]=="0" and list1[6]=="0"):
        return("player 2 winner")
    
    elif(list1[1]=="0" and list1[4]=="0" and list1[7]=="0"):
        return("player 2 winner")
    
    elif(list1[2]=="0" and list1[5]=="0" and list1[8]=="0"):
        return("player 2 winner")

    elif(list1[0]=="0" and list1[4]=="0" and list1[8]=="0"):
        return("player 2 winner")
        
    elif(list1[2]=="0" and list1[4]=="0" and list1[6]=="0"):
        return("player 2 winner")
    
    
    else:
        return ("keep going")
