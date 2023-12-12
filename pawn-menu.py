'''
Start
Display a nemu option related to shopping cart 
Implement While loop to keep the menu running (after user has selected options)
Provide the user with the option to end the program (Break out the while)

End
'''


print ("Welcome to my shop\n")
while True :
    menu = input ("Select one of the following:\n\
                1. Add item \n\
                2. Remove Item \n\
                3. Update Item \n\
                4. Exit cart\n\
                    :\t")
    if menu == "1":
        print ("Added Item")
    elif menu == "2":
        print ("Item removed")
    elif menu == "3":
        print ("Item updated")
    elif menu == "4":
        print ("Have a good day!.")
        break
    else:
        print ("invalid option")
        
    
    


