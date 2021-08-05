import random
def choose():
    #names=["dhinesh","kathir","jegan","aravinth","bharath","kaviprakash","iqbal","raaghav","anbumani","aathi"]
    names=["aarthy","mahesh","sanju","annamalai","unnamalai","alamu","visalachi"]
    word=random.choice(names)
    return word
def jumbled(word):
    jum="".join(random.sample(word,len(word)))
    return jum
def thank(p1,p2,pp1,pp2):
    print(p1,"your point is",pp1)
    print(p2,"your point is",pp2)
    print("thank you")
def play():
    p1=input("enter player1 name")
    p2=input("enter player2 name")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumbled(picked_word)
        print(qn)
        if(turn%2==0):
            print (p1,"your turn")
            ans=input("my guess is")
            if(ans==picked_word):
                pp1=pp1+1
                print("your score is",pp1)
            else:
                print("wrong answer.The rights answer is",picked_word)
            d=input("enter 1 to continue and 0 to exit")
            c=int(d)
            if(c==0):
                thank(p1,p2,pp1,pp2)
                break
        else:
            print (p2,"your turn")
            ans=input("my guess is")
            if(ans==picked_word):
                pp2=pp2+1
                print("your score is",pp2)
            else:
                print("wrong answer.The rights answer is",picked_word)
            d=input("enter 1 to continue and 0 to exit")
            c=int(d)
            if(c==0):
                thank(p1,p2,pp1,pp2)
                break
        turn=turn+1
play()
            
        
                
    
                