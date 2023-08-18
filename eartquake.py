while True :
    richter = input("Enter a magnitude on the Richter scale, else print 'exit': ")
    
    if richter.lower() == "exit":
        print("Exiting the program.")
        break
    
    richter = float(richter)
    if richter >= 8 :
        print("most structures fall")
    else: 
        if richter >= 7 :
            print("many buildings destroied")
        else:
            if richter >= 6 :
                print("many buildings are damaged, some destroied")
            else:
                if richter >= 4.5 :
                    print("Damage to poorly constructed buildings")
                else:
                    print("No destruction of buildings")
#you could use "elif" but pay attention to order (from higher to lower)
#                