import random

num = random.randrange(1,5)
compNum = num



name = input ("What's your name?\n")

print ("Welcome" + " " + name + " " + "we'll see if you mean us harm or help")

def tottet():

    pickNum = int(input ("Choose a number from 1 to 5\n"))



    if pickNum == 1:
        print('Hope your geography is good')

        def question():

            ques1 = input (" On which continent is Zambia? Africa, Asia, America or Europe\n").upper()

            if ques1 == 'AFRICA':
                print ("Great, you're onto the next stage")

                print ("next stage allows 3 tries, think hard")

                for turn in range(3):
                    userNum = int(input ("choose a number from 1 to 5 and cross your fingers\n"))

                    
                    if userNum > 0 and userNum < 6:

                            
                            if userNum == compNum:
                                print ("yay you have helped us")
                                break

                            else:
                                if userNum < compNum:
                                    print (" Oopss, take it up a notch or two")
                                    
                                    
                                elif userNum > compNum:
                                    print ("Oopss, bring it down a notch or two")
                                    

                                if turn == 2:
                                    print ("You've run out of luck" + " " + name)

                                print ("Trial", turn + 1)
                    else:
                        print ("invalid choice,")
                        
                    
            elif ques1 == 'ASIA' or ques1 == 'AMERICA' or ques1 == 'EUROPE':
                print ("Wrong answer, Game over")

            else:
                print ("answer not among the options, try again")
                question()
        question()
            
    elif pickNum == 2:
        print ('Hope you are good at old movies')

        def question():

            ques2 = input ("What was the name of Dorothy's Dog in Wizard of Oz? Snoopy, Toto or Pluto?\n").upper()

            if ques2== 'TOTO':
                print (" Yep, that was right. Next stage")

                print ("next stage allows 3 tries, think hard")

                for turn in range(3):
                    userNum = int(input ("choose a number from 1 to 5 and cross your fingers\n"))

                    
                    if userNum > 0 and userNum < 6:

                            
                            if userNum == compNum:
                                print ("yay you have helped us")
                                break

                            else:
                                if userNum < compNum:
                                    print (" Oopss, take it up a notch or two")
                                    
                                    
                                elif userNum > compNum:
                                    print ("Oopss, bring it down a notch or two")
                                    

                                if turn == 2:
                                    print ("You've run out of luck" + " " + name)

                                print ("Trial", turn + 1)
                    else:
                        print ("invalid choice,")
                        
                    
            elif ques2 == 'SNOOPY' or ques1 == 'PLUTO':
                print ("Wrong answer, you have failed us too soon earthling")

            else:
                print ("answer not among the options, try again")
                question()
        question()

        

    elif pickNum == 3:
        print ("Hope you're good at science fiction")

        def question():
            ques3 = input ("Which naughty-thieving species does Captain Picard and crew encounter numerous times? Ferengi, Klingons or Acamarian?\n").upper()

            if ques3== 'FERENGI':
                print (" Yep, that was right. Next stage")

                print ("You have 3 attempts on next stage, think long and hard")
                
                for turn in range(3):
                    userNum = int(input ("choose a number from 1 to 5 and cross your fingers\n"))

                    if userNum > 0 and userNum < 6:

                
                        if userNum == compNum:
                            print ("yay you have helped us")
                            break

                        else:
                            if userNum < compNum:
                                print (" Oopss, take it up a notch or two")

                            elif userNum > compNum:
                                print ("Oopss, bring it down a notch or two")
                                print (compNum)

                            else:
                                print ("Game over")

                            if turn == 2:
                                print ("You've run out of luck" + " " + name)
                                print ("Game over")

                            print ("Trial", turn + 1)

                    else:
                        print ("invalid number, try again")
                        
            elif ques3 == 'KLINGONS' or ques3 == 'ACAMARIAN':
                print ("Nope, it was the Ferengi...Game over")
                    
            else:
                print("answer not among options, try again")
                question()
        question()


    elif pickNum == 4:
            print ("Hope you're good at literature")

            def question():
                ques4 = input ("Who is the author of Big Friendly Giant? Is it Dr.Seuss, Dahl or Rowling?\n").upper()

                if ques4== 'DAHL':
                    print (" Great job. Next stage")

                    print ("You have 3 chances on next stage, think long and hard")
                    
                    for turn in range(3):
                        userNum = int(input ("choose a number from 1 to 5 and hope for the best\n"))

                        if userNum > 0 and userNum < 6:

                    
                            if userNum == compNum:
                                print ("yay you have helped us")
                                break

                            else:
                                if userNum < compNum:
                                    print (" Oopss, take it up a notch or two")

                                elif userNum > compNum:
                                    print ("Oopss, bring it down a notch or two")
                                    print (compNum)

                                else:
                                    print ("Game over")

                                if turn == 2:
                                    print ("You've run out of luck" + " " + name)
                                    print ("Game over")

                                print ("Trial", turn + 1)

                        else:
                            print ("invalid number, try again")
                            
                elif ques4 == 'Dr.SEUSS' or ques4 == 'ROWLING':
                    print ("Nope, it was the Dahl...Game over")
                        
                else:
                    print("answer not among options, try again")
                    question()
            question()
    elif PickNum == 5
        print ("Hope you're good at anagrams\n")
        
        def question():
            ques5 = input ("Using all the letters make an animal from Balm\n").upper()
            
            if ques5 == "LAMB"
            print ("Baa baa good job!\n  Cross your fingers for the next stage")
            
            for turn in range(3):
                UserNum = int(input("Choose a number from 1 to 5 and hope for the best\n"))
                
                if UserNum > 0 and UserNum < 6:
                    
                    
                    if UserNum==CompNum:
                        print("Yay you've saved us" + name + "We owe you")
                        
                        
                    else:
                        if UserNum<CompNum:
                            print("Too high, try a smaller number")
                            
                        if UserNum>CompNum:
                            print("Too low, try a bigger number")
                            
                        else:
                            print("Game over")
                        
                     
                              
                              
                
              
        
    else:
        print("invalid number" + " " + name + " " + ", try again" )
        tottet()
tottet()
        
    
          
#else:
#    input ('Pick a valid number')
# add anagrams
# add a timer
# reduce code or edit it to become more iterative.
    
        
    

