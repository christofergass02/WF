# wf04.py
from sys import exit
import time
import random

# choices: [yes, no], [left, right, forward]


#(2) African Pavilion
def african_pav():
#    money = 0.50  
#    time = 45
    print("The Pavilion is made up of round huts\n that represent 24 nations of sub-Saharan Africa\n stands on a broad platform erected on stilts above water.")
    print("As you walk into the Pavilion you hear the sounds of chanting and drum beats.\nAs you walk in the open-air entertainment area\nyou see Watsui men from Rwanda perform a spirited dance\nand demonstrate their ability at high-jumping.\nBurundi drummers and West African dancers also perform.")
    print("Where would you like to go to now?")
    print("To the left is THE NEW JERSEY PAVILION and to the right is THE UNISPHERE.")
    afri1()
def afri1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        nj_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        unisphere_pav()
    else:
        print("I didn't understand that.\n")
        afri1()

#(3) Alaska Pavilion
#    time = 30 
def alaska_pav():
    print("While in the igloo shaped pavilion you observe\nthe 32-square-foot topographical model of Alaska.")
    print("Where would you like to go to next?")
    print("To the left is THE MISSOURI PAVILION\nand to the right is THE WISCONSIN PAVILION.")
    al1()
def al1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left": 
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE WISCONSIN PAVILION.")
        wisconsin_pav()
    else:
        print("I didn't understand that.\n")
        al1()

# Astral Fountain
def astral_pav(): 
#    time = 10 
    print("You enjoy the orchestration of the fountain and the atmosphere of the Fair.")   
    print("Where would you like to go from here?")
    print("To the left is THE WESTINGHOUSE PAVILION\nand to the right is THE NEW YORK STATE PAVILION.")
    ast1()
def ast1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE WESTINGHOUSE PAVILION   ")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysc_pav()
    else:
        print("I didn't understand that.\n")
        ast1()

#(8) American-Israel Pavilion
def americanisrael_pav():
#    money = 0.25  
#    time = 25
    print("Within the pavilion you enjoy scenes and artifacts portraying 4,000 years of Jewish history.\nAfter you walk around the Pavilion and to its top\nyou consider which Pavilion to head to next.")
    print("Do you head left to THE HALL OF FREE ENTERPRISE PAVILION\nor right to THE SWITZERLAND PAVILION")
    amer1()
def amer1():    
    choice = input("Which way do you go?\nleft or right?\n ")    
    if choice == "left":
        print("\nYOU ARE AT THE HALL OF FREE ENTERPRISE PAVILION")
        hall_pav()   
    elif choice == "right":
        print("\nYOU ARE AT THE SWITZERLAND PAVILION")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")
        amer1()

#(14) Belgium Pavilion
def belgium_pav():
#    money = 0.60 
#    time = 60
    print("As you walk through the pavilion you enjoy the sight of Gille Dancers.")
    print("Clowns with wooden shoes, ostrich-feather headdresses and bells\ndance through the streets to the sound of drums and brass instruments.")
    print("You learn that the Gilles hark back to 1540, when Belgium was ruled by Spain,\nand the conquistidors' triumph over Peruvian Indians was celebrated at Mardi Gras.")
    print("To your left you see THE LOUISIANNA PAVILION,\nand to the right is THE VATICAN PAVILION?")
    bel1()
def bel1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE LOUISIANNA PAVILION")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE VATICAN PAVILION")
        vatican_pav()
    else:
        print("I didn't understand that.\n")
        bel1()

#(24) Christian Science Pavilion
def christianscience_pav():
#    time = 30 
    print("The Pavilion is in a star-shape\nand their is descriptions of the faith\nwith displays and recorded testimponials.")
    print("After walking around the pavilion you decide on where to head to next.")
    print("To the left is THE HALL OF FREE ENTERPRISE PAVILION")
    print("and to the right is THE SWITZERLAND PAVILION.")
    chris1()
def chris1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE HALL OF FREE ENTERPRISE PAVILION.")
        hall_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SWITZERLAND PAVILION.")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")
        chris1()

#(26) Chrysler Pavilion
def chrysler_pav():
#    time = 60     
    print("")
    print("After walking around the pavilion you decide it is time to go on home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()    
#    print("To the left is THE HALL OF FREE ENTERPRISE PAVILION")
#    print("and to the right is THE SWITZERLAND PAVILION.")
#    choice = input("Which way do you go?\nleft or right?\n ") 
#    if choice == "left":
#        print("\nYOU ARE AT THE HALL OF FREE ENTERPRISE PAVILION.")
#        hall_pav()
#    elif choice == "right":
#        print("\nYOU ARE AT THE SWITZERLAND PAVILION.")
#        switzerland_pav()
#    else:
#        print("I didn't understand that.\n")

#(37) Eastman Kodak Pavilion
def eastman_pav():
#    time = 45 (30-90) 
    print("Atop this pavilion are five color photographs, each 30 by 36 feet in size.\nWhile you are walking around the pavilion\nyou notice a sad figure with shabby clothing and clown makeup.")
    east1()
def east1():    
    choice = input("Do you approach the figure?\nyes or no\n ")
    if choice == "yes":
        print("You find out the figure is none other than Emitt Kelly Jr,\nwhich is the Pavilion's mascot.\nAfter you do your best miming act with Emitt\nyou decide where to head to next.")
    elif choice == "no":
        print("\nOf course, as you please.")
    else:
        print("I didn't understand that.\n")
        east1()
    print("Where do you go to next?")
    print("To the left you see THE GARDEN OF MEDITATION\nand to the right is THE AMERICAN ISRAEL PAVILION.")
    east2()
def east2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GARDEN OF MEDITATION")
        garden_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AMERICAN-ISRAEL PAVILION")
        americanisrael_pav()
    else:       
        print("I didn't understand that.\n")
        east2()

#(40) First National City Bank Pavilion
def fncb_pav():
#    time = 10 
    print("Which you find out is the Fair's only bank with a branch.") 
    print("After contemplating what you would do with a few extra bucks\nyou consider which pavilion to head to next.")
    print("Do you go left to THE GARDEN OF MEDITATION,\nor right to THE CHRISTIAN SCIENCE PAVILION?")
    fncb1()
def fncb1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GARDEN OF MEDITATION.")
        garden_pav()   
    elif choice == "right":
        print("\nYOU ARE AT THE CHRISTIAN SCIENCE CENTER.")
        christianscience_pav()
    else:
        print("I didn't understand that.\n")
        fncb1()

#(45) Garden of Meditation
def garden_pav():
#    time = 20     
    print("As you continue to walk through the Garden\nyou notice the hum of the busy Fair become quieter and quieter.\nAll around you are trees, as well as laurel and azaleas.\nAlso in the Garden are Biblical references and a quotation from Sir Francis Bacon.")
    gar1() 
def gar1():
    choice = input("Would you like to read the quote or know more about one of the Biblical verses\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,4)
        if randint == 1: 
            print("Numbers 6:24-26 - 'The Lord bless you\n and keep you;\nthe Lord make his face shine on you\n and be gracious to you;\nthe Lord turn his face toward you\n and give you peace.'")
        elif randint == 2:
            print("Mica 6:8 - 'He has shown you, O mortal, what is good.\n And what does the Lord require of you?\nTo act justly and to love mercy\n and to walk humbly with your God.'")
        elif randint == 3:
            print("Romans 12:10 & 12 - 'Be devoted to one another in love. Honor one another above\nyourselves. Never be lacking in zeal, but keep your spiritual\n fervor, serving the Lord. Be joyful in hope, patient in affliction,\n faithful in prayer.'")
        elif randint == 4:
            print("God Almighty first planted a Garden.\nAnd indeed it is the purest of human pleasures.\nIt is the greatest refreshment to the spirits of man. -Francis Bacon")
            gar2()
    elif choice == "no":
        print("Of course, let's move on.\n")        
        gar2()
    else:
        print("I didn't understand that.\n")
        gar1()
    
def gar2():
    print("After you relax in the Garden,\nyou contemplate where to head to next.")
    print("Do you head left to THE BELGUIM PAVILION,\nor right to THE CHRISTIAN SCIENCE PAVILION?")
    
    gar3()
def gar3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE BELGIUM PAVILION.")
        belgium_pav()       
    elif choice == "right":
        print("\nYOU ARE AT THE CHRISTIAN SCIENCE PAVILION.")
        christianscience_pav()
    else:            
        print("I didn't understand that.\n")
        gar3()

#(48) General Motors
def gm_pav(): 
#    time = 40   
    print("YOU WALK ABOUT THE PAVILION . . . . ")   
    print("After you walk through the pavilion you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()
#    print("To the left is the . . . .  and to the right . . . ")
#    choice = input("Which way do you go?\nleft or right?\n ") 
#    if choice == "left":
#        print("\nYOU ARE AT THE    ")
#        international_pav()
#    elif choice == "right":
#        print("\nYOU ARE AT THE   PAVILION.")
#        sierra_pav()
#    else:
#        print("I didn't understand that.\n")

#(53) Hall of Free Enterprise Pavilion
def hall_pav():
#    time = 35    
    print("There is someone talking on an oval stage,\nbut you see a device called the Answer Machine that catches your eye.")
#    hall1() 
#def hall1():
#    choice = input("Do you play with the Answer Machine?\nyes or no\n ")
#    if choice == "yes":
#        randint = random.randint(0,5)
#        if randint == 1: 
#            print("") 
#        elif randint == 2:
#            print("") 
#        elif randint == 3:
#            print("") 
#        elif randint == 4:
#            print("") 
#        elif randint == 5:
#            print("") 
#    elif choice == "no":
#        print("Of course, let's move on.\n")
#        
#    else:
#        print("I didn't understand that.\n")
#        hall1()
    print("After walking through the pavilion you decide where to go next.")
    print("To the left is THE VATICAN PAVILION")
    print("and to the right is THE INTERNATIONAL PAVILION.")
    hall2()
def hall2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE VATICAN PAVILION.")
        vatican_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE INTERNATIONAL PAVILION.")
        international_pav()
    else:
        print("I didn't understand that.\n")
        hall2()

#(64) International Plaza
def international_pav():
#    time = 30     
    print("You enjoy displays such as U.N. postage stamps,\nworks of art and food specialties.")
    print("While walking about the pavilion you notice fairgoers eating a strange pastry.")
    int1()
def int1():    
    choice = input("Do you decide to buy a Belguim Waffle?\nyes or no\n ")
    if choice == "yes":
        print("'Mmmmmm, that is delicious', you say out loud.\n")
    elif choice == "no":
        print("Of course, as you please.")
        int2()
    else:
        print("I didn't understand that.\n")
        int1()

    int2()
def int2():
    print("After enjoying the sights and sounds of the Plaza\nyou consider your next destination.")
    print("To the left is THE NEW YORK STATE PAVILION")
    print("and to the right is THE SWEDEN PAVILION.")
    int3()
def int3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SWEDEN PAVILION.")
        sweden_pav()
    else:
        print("I didn't understand that.\n")
        int3()

#(76) Louisiana Pavilion
def louisiana_pav():    
#    money = 1 (for teen-age center)
#    time = 30      
    print("While in the pavilion you dance to jazz in the big Teen-Age Dance Center.\nAfter dancing you consider the next pavilion to go to.")
    print("Do you head left to THE WESTINGHOUSE PAVILION\nor right to THE NEW YORK STATE PAVILION.")
    lou1()
def lou1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE WESTINGHOUSE PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysc_pav()
    else:
        print("I didn't understand that.\n")
        lou1()

#(83) Malaysia Pavilion
def malaysia_pav():
#    time = 20    
    print("During your visit to this new country's pavilion,\nyou walk to the center of the building\nand enjoy the sight of orchids and ferns that surround a small lily pond.")
    print("Also within the pavilion are visual devices\nand taped commentaries on pickup phones.\nWhich aquaint visitors to the pavilion with Malaysia's\npeople, government, industry and arts.")
    print("Where would you like to go to now?")
    print("To the left is THE NEW JERSEY PAVILION and to the right is THE UNISPHERE.")
    mal1()
def mal1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")
        mal1()

#(83) Minnesota Pavilion
def minnesota_pav():
#    time = 25     
    print("While walking around the pavilion\nyou learn about Minnesota's instrustrial production.")
    print("Where would you like to go to now?")
    print("To the left is THE LOUISIANNA\nand to the right is THE NEW YORK STATE PAVILION.")
    minn1()
def minn1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE LOUISIANA PAVILION.")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    else:
        print("I didn't understand that.\n")
        minn1()

#(83) Missouri Pavilion
def missouri_pav():
#    time = 15 
    print("AS YOU WALK ABOUT THE PAVILION . . . .")
    print("Where do you decide to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE WISCONSIN PAVILION.")
    miss1()
def miss1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE WISCONSIN PAVILION.")
        wisconsin_pav()
    else:
        print("I didn't understand that.\n")
        miss1()

#(92) New Jersey
def nj_pav(): 
#    time = 30     
    print("While walking about the Pavilion you find out the state\nis celebrating its tercentenary this year.")   
    print("As you make your way towards the center of the Pavilion\nyou view local choral groups, bands, symphony orchastras and folk dances.")
    print("Where would you like to go to next?")
    print("To the left is THE NEW YORK CITY PAVILION\nand to the right THE UNISPHERE.")
    nj1()
def nj1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK CITY PAVILION.")
        unisphere_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        nyca_pav()
    else:
        print("I didn't understand that.\n")
        nj1()

#(94) New York City Pavilion and Ice Theater
def nyca_pav(): 
#    money = 0.10      
#    time = 60
    print("While in the pavilion you observe the incredibly\ndetailed model of the city, which is 180 by 100 feet\nand includes every one of New York's 835,000 buildings\nand all of its streets, ferries, docks, bridges and airports.")   
    print("After you find your neighborhood on the model\nyou decide where to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    nyca1()
def nyca1():   
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I didn't understand that.\n")
        nyca1()

#(94) New York City Pavilion and Ice Theater B
def nycb_pav(): 
#    money = 0.10    
    print("You enjoy a model of NYC as it is today\nand how it was in 1664. Additionaly, you look over an exhibit of art,\n sculpture, artifacts and photographs from 34 of the city's\nmost important museums, libraries, zoos and botanical gardens.")   
    print("After walking around the pavilion you decide where to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    nycb2()
def nycb2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I didn't understand that.\n")
        nycb2()

#(95) New York State Pavilion
def nysa_pav():
#    time = 30 
    print("You take the 'Sky-Streak', a speedy elevator capsule,\nup the side of the fair's tallest towers.")
    print("From atop the tower you are able to see the whole fairgrounds!")
    print("You can also see the NYC Skyline, New Jersey, Connecticut,\nThe Atlantic Ocean and most of Long Island.")
    print("After you take in all the sights and sounds of the Fair\nyou consider where to go to next?")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
    nysa1()
def nysa1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysa1()

#(95) New York State Pavilion B
def nysb_pav():
#    time = 30     
    print("While at the Pavilion you decide to check out the 'Tent of Tomorrow'.\nWhile you walk into the Tent you enjoy the sights above and below you.\nAbove you are wonderfully colored translucent fiberglass panels that creates a stained glass effect.\nBelow your feet is a humongous map of the state of New York.\nIn the distance you hear a school choir.")
    print("As you get closer you hear what they are singing, the song is titled 'Everything's Coming up Moses'.")

    nysb1()
def nysb1():    
    choice = input("Interested to know the lyrics to 'Everything's Coming up Moses'?\nyes or no\n ")
    if choice == "yes":
        print("\nYou'll be swell, You'll be great,")
        print("Gonna have the whole world on a plate.")
        print("Starting here, starting now")
        print("It's a small world after all")
        print("Honey, everything's coming up Moses!")
        print("")
        print("Clear the decks, Clear the tracks")
        print("You've got nothing to do but relax.")
        print("Blow a kiss, take a bow,")
        print("It's a small, small world")
        print("Honey, everything's coming up Moses!")
        print("")
        print("Now's our inning,")
        print("Stand the world on its ear!")
        print("Set it spinning,")
        print("It's a small world after all")
        print("That'll be just the beginning!")
        print("")
        print("Curtain up, light the lights")
        print("You got nothing to hit but the heights")
        print("You'll be swell, you'll be great")
        print("I can tell, Just you wait,")
        print("That lucky star I talk about is due..")
        print("Honey everything coming up Moses for me and for you!")
        print("After enjoying the song by a Long Island middle school choir\nyou decide where to head to next.")
    elif choice == "no":
        print("\nOf course, as you please. Let's move on to the next pavilion.")
    else:
        print("I didn't understand that.\n")
        nysb1()

    print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
    nysb2()
def nysb2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysb2()

#(95) New York State Pavilion 3
def nysc_pav():
#    time = 30     
    print("As you walk around the pavilion you enjoy the artwork on the outside of the theatre\nby Pop artists such as John Chamberlain, Robert Indiana, Roy Lichtenstein and James Rosenquist.")
    nysc1()
def nysc1():
    choice = input("Would you like to know more about one of the artworks?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,5)
        if randint == 1: 
            print("Roy") 
        elif randint == 2:
            print("Ben") 
        elif randint == 3:
            print("Paul") 
        elif randint == 4:
            print("Not Andy") 
        elif randint == 5:
            print("Andy") 
    elif choice == "no":
        print("Of course, let's move on.\n")
        nysc2()
    else:
        print("I didn't understand that.\n")
        nysc1()

    nysc2()
def nysc2():

    print("Where would you like to go to next?")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
    nysc3()
def nysc3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysc3()

#(98) Pakistan Pavilion
def pakistan_pav():
#    time = 30 
    print("While walking through the Pavilion you learn about the country's history\nthrough relics dating back thousands of years.")
    print("After taking your time to take in all the sights and sounds of the Pavilion\nyou consider your next destination.")
    print("To the left is . . . . and to the right is . . . . ")
    pak1()
def pak1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        nj_pav()
    else:
        print("I didn't understand that.\n")
        pak1()

#(102) Pepsi-Cola Pavilion
def pepsi_pav():
#    money = 0.60 (boat ride)
#    time = 25
    print("While in the pavilion you take a boat ride called 'It's a Small World'.\nYou see scenes such as the Eiffel Tower,\na Dutch Windmill and India's Taj Mahal\nwhile anmimated figures dance and sing 'It's a Small World'.")
    pep1()
def pep1():    
    choice = input("Interested to know the lyrics to 'It's a Small World'?\nyes or no\n ")
    if choice == "yes":
        print("\nIt's a world of laughter, a world of tears")
        print("It's a world of hopes and a world of fears")
        print("There's so much that we share, that it's time we're aware")
        print("It's a small world after all")
        print("")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small, small world")
        print("")
        print("There is just one moon and one golden sun")
        print("And a smile means friendship to everyone")
        print("Though the mountains divide, and the oceans are wide")
        print("It's a small world after all")
        print("")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small, small world\n")
    elif choice == "no":
        print("\nOf course, as you please.")
    else:
        print("I didn't understand that.\n")
        pep1()

    print("After enjoying the nine minute boat ride\nyou decide where to head to next.")
    print("To the left is THE FIRST NATIONAL CITY BANK.")
    print("and to the right is THE EASTMAN KODAK PAVILION.")
    pep2()
def pep2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE FIRST NATIONAL CITY BANK.")
        fncb_pav()
    elif choice == "right":
        print("\nYOU AT THE EASTMAN KODAK PAVILION.")
        eastman_pav()
    else:
        print("I didn't understand that.\n")
        pep2()

# Robert Moses


#(119) Sierra Leone Pavilion
def sierra_pav():
#    money = 0.10  
#    time = 30 
    print("Walking up to the pavilion you notice a raised stage with people dancing.")
    print("As you get closer you watch two troupes perform intricate dances.")
    print("Where would you like to go next?")
    print("To the left is THE MALAYSIA PAVILION\nand to the right is THE AFRICAN PAVILION")
    sier1()
def sier1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE MALAYSIA PAVILION.")
        malaysia_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AFRICAN PAVILION.")
        african_pav()
    else:
        print("I didn't understand that.\n")
        sier1()

#(121) Sinclair Pavilion
def sinclair_pav():
#    time = 10     
    print("After you check out the dinasours . . . you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()
#    print("To the left is THE UNITED STATES RUBBER PAVILION\nand to the right is THE SKF PAVILION.")
#    choice = input("Which way do you go?\nleft or right?\n ") 
#    if choice == "left":
#        print("\nYOU ARE AT THE UNITED STATES RUBBER PAVILION.")
#        westinghouse_pav()
#    elif choice == "right":
#        print("\nYOU ARE AT THE SKF PAVILION.")
#        minnesota_pav()
#    else:
#        print("I didn't understand that.\n")

#(123) SKF Industries Pavilion
def skf_pav():
#    time = 15     
    print("After you walk around the Pavilion you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()
#    print("Where would you like to go to now?")
#    print("To the left is THE CHRYSLER PAVILION and to the right is THE SINCLAIR PAVILION.")
#    choice = input("Which way do you go?\nleft or right?\n ") 
#    if choice == "left":
#        print("\nYOU ARE AT THE CHRYSLER PAVILION.")
#        chrysler_pav()
#    elif choice == "right":
#        print("\nYOU ARE AT THE SINCLAIR PAVILION.")
#        sinclair_pav()
#    else:
#        print("I didn't understand that.\n")

#(127) Sweden Pavilion
def sweden_pav():
#    time = 30     
    print("Within the pavilion you enjoy a number of exhibits\nshowing fascinating mechanical or electrical devices.")
    print("On display for the first time is a large model of Sweden's\nsupersecret new fighter plane, the 'Viggen', or Thunderbolt.")
    print("Where would you like to go to next?")
    print("To the left is THE NEW YORK STATE PAVILION\nand to the right is THE PAKISTAN PAVILION.")
    swed1()
def swed1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysc_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE PAKISTAN PAVILION.")
        pakistan_pav()
    else:
        print("I didn't understand that.\n")
        swed1()

#(129) Switzerland Pavilion
def switzerland_pav():
#    time = 45     
    print("While in the pavilion you check out the 'Time Center' near the entrance.\nAt the front of the exhibit are the dials and indicators of a large 'Master Clock'.")
    print("The 'Master Clock' is so accurate that it can measure irregularities in the earth's rotation.")
    print("After you take time to enjoy the rest of the exhibits you decide where to head to next.")
    print("To the left is THE INTERNATIONAL PAVILION\nand to the right is THE SIERRA LEONE PAVILION.")
    switz1()
def switz1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE INTERNATIONAL PLAZA")
        international_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SIERRA LEONE PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")
        switz1()

#(133) Transportation and Travel Pavilion
def tat_pav():
#    time = 60     
    print("")
    print("Where would you like to go to now?")
    print("To the left is THE SKF INDUSTRIES PAVILION\nand to the right is THE UNITED STATES RUBBER PAVILION.")
    tat1()
def tat1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SKF INDUSTRIES PAVILION.")
        skf_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNITED STATES RUBBER PAVILION.")
        usr_pav()
    else:
        print("I didn't understand that.\n")
        tat1()

#(138) United States Rubber
def usr_pav():
#    money = 0.25   
#    time = 10 
    print("After you enjoy the ride you decide where would you like to go to next.")
    print("To the left is THE SKF INDUSTRIES PAVILION\nand to the right is THE CHRYSLER PAVILION.")
    usr1()
def usr1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SKF INDUSTRIES PAVILION.")
        skf_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE CHRYSLER PAVILION.")
        chrysler_pav()
    else:
        print("I didn't understand that.\n")
        usr1()

#(140) Unisphere
def unisphere_pav():
#    time = 15     
    print("While you try to get a better look at the fair's symbol,\nyou are stopped from getting closer due to a protest.")
#    choice = input("Would you like to know more about the protest?\nyes or no\n")
#    if choice == "yes":
#        print("")
#        print("")
#    elif choice == "no":
#        print("Of course, as you please.")
#    else:
#        print("I didn't understand that.\n")
    uni1()
def uni1():
    print("Where do you decide to go to next?")
    print("To the left is THE WISCONSIN PAVILION\nand to the right is THE NEW YORK CITY PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE WISCONSIN PAVILION")
        international_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK CITY PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")
        uni1()

#(141) Vatican Pavilion
def vatican_pav():
#    time = 45     
    print("As you enter the Pavilion you walk along the Long Gallery.\nAfter you walk through the Gallery you are brisked away along a moving platform\nwhere you look in awe at the 'Pietà' by Michelangelo.")
    print("After you walk through various other parts of the Pavilion\nyou consider where to go to next?")
    print("To the left is THE MINNESOTA PAVILION\nand to the right is THE ASTRAL FOUNTAIN.")
    vat1()
def vat1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE MINNESOTA PAVILION.")
        minnesota_pav()
    elif choice == "right":
        print("YOU ENJOY THE ASTRAL FOUNTAIN.")
        astral_pav()
    else:   
        print("I didn't understand that.\n")
        vat1()

#(145) Westinghouse Pavilion
def westinghouse_pav():
#    time = 15    
    print("You enjoy the copies of articles buried in the Time Capsule from 1938.")
    west1()
def west1():    
    choice = input("Interested to know about some of the items from the Time Capsule?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,5)
        if randint == 1: 
            print("Alarm clock, can opener, nail file, tooth brush,\nset of alphabet blocks, baseball, deck of cards, and poker chips.") 
        elif randint == 2:
            print("Rubber fabrics, aluminum, carbon steel, copper, silicon,\nstainless steel, glass wool and raw rubber") 
        elif randint == 3:
            print("Money of the United States, a message from Albert Einstein\nand the Holy Bible.") 
        elif randint == 4:
            print("Microfilm of 'Guernica' by Pablo Picasso,\nphotograph of string quartet,\nand a typical poker scene.") 
        elif randint == 5:
            print("Newsreel of President Franklin D. Roosevelt\nspeaking at Gettysburg, Pennsylvania, July 3, 1938,\nJesse Owens winning 100 meter dash in 1936 Olympic games,\nand Collegiate football: Harvard-Yale, November 1936 at 'Yale Bowl,'\nNew Haven, Conn. Yale wins 14-13.") 
    elif choice == "no":
        print("Of course, let's move on.\n")
        west3()
    else:
        print("I didn't understand that.\n")
        west1()
 
    west3()
def west3():
    print("After you enjoy the Time Capsule you consider the next pavilion")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE NEW YORK STATE PAVILION.")
    west2()
def west2():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysa_pav()
    else:
        print("I didn't understand that.\n")
        west2()

#(147) Wisconsin Pavilion
#    time = 20
def wisconsin_pav(): 
    print("You walk into a modern teepee that is representative of the states Indian hertiage.\nOnce inside you enjoy displays of the state's\nfarms, industries and great outdoors.")   
    print("Before leaving the Pavilion you notice a large yellow block on a van.\nAs you get closer you find out it is actually a block of cheese\nwhich is said to be 17 tons and possibly the world's largest.")
    wisc1()
def wisc1():
    choice = input("Would you like to know more about the block of cheese?\nyes or no\n ")
    if choice == "yes":
        print("The cheese was made for the Wisconsin Cheese Foundation\nand took 43 1/2 hours to make.\nThe size of the cheese is 6 1/2 feet wide, 5 1/2 feet high and 14 1/2 feet long.\nThe approximate weight of the cheese is 17 1/4 tons or 34,591 pounds.") 
    elif choice == "no":
        print("Of course, let's move on.\n")
    else:
        print("I didn't understand that.\n")
        wisc1()
    print("On your way out, and a little more hungrier than before you entered the Pavilion,\nyou decide where you would like to head to next.")
    print("To the left is THE GENERAL MOTORS PAVILION and to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    wisc2()
def wisc2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I didn't understand that.\n")
        wisc2()

# First decision
def first():  
    choice = input("Which way do you want to go?\n You can go left, right or forward?\n ")    
    if choice == "left":
        print("\nYOU ARE AT THE FIRST NATIONAL CITY BANK PAVILION.")
        fncb_pav()
    elif choice == "forward":
        print("\nYOU ARE AT THE EASTMAN KODAK PAVILION")
        eastman_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE PEPSI-COLA PAVILION")
        pepsi_pav()
    else:
        print("I didn't understand that.\n")
        first()

# Second decision
def second():    
    choice = input("Would you like to know more about the areas of the fair before you proceed?\nyes or no\n ")
    if choice == "yes":
        print("\nThe areas of the fair are: Industrial, International,\nFederal and State, Transportation, Lake Amusement, and Flushing Bay.\n")
        print("The Industrial Area has 45 pavilions that showcases America's industry.\nThe International Area is represented by 80 nations in 37 pavilions.")
        print("The Federal and State Area represents 19 states.\nThe Transportation Area shows off the many forms of transportation.")
        print("The Lake Amusement Area is the smallest section, but with the most variety.\nThe Flushing Bay Area is a place for seafarers and sports fans.\n")            
        print("The site of people as well as strange and colorful buildings\nare in all directions near and as far as the eye can see.")
        print("What do you want to see first?")
        print("To your left you see THE FIRST NATIONAL CITY BANK.")
        print("Forward is THE EASTMAN KODAK PAVILION.")
        print("and to your right is THE PEPSI-COLA PAVILION.")  
    if choice == "no":    
        print("\nThe sight of thousands of people as well as dozens of strange and colorful buildings\nare in all directions near and as far as the eye can see.")
        print("What do you want to see first?")
        print("To your left you see THE FIRST NATIONAL CITY BANK.")
        print("Forward is THE EASTMAN KODAK PAVILION.")
        print("and to your right is THE PEPSI-COLA PAVILION.")   
    else: 
        print("I didn't understand that.") 
        second() 


# Start
def start():
    print("                                                  ,--, ")
    print("            .---.    ,---,.                     ,--.'| ")
    print("           /. ./|  ,'  .' |        ,---.     ,--,  | : ")
    print("       .--'.  ' ;,---.'   |       /     \ ,---.'|  : ' ")
    print("   .--'.  '   \' .:   :  :       .    ' /  |   | : _' | ")
    print(" /___/ \ |    ' ':   |  |-,    '    / ;   :   : |.'  | ")
    print(" ;   \  \;      :|   :  ;/|    |   :  \   |   ' '  ; : ")
    print("  \   ;  `      ||   |   .'    ;   |   ``.\   \  .'. | ")
    print("   .   \    .\  ;'   :  '      '   ;      \`---`:  | ' ")
    print("    \   \   ' \ ||   |  |      '   |  .\  |     '  ; | ")
    print("     :   '  |--' |   :  \      |   :  ';  :     |  : ; ")
    print("      \   \ ;    |   | ,'       \   \    /      '  ,/  ")
    print("       '---'     `----'          `---`--`       '--'   ")
    time.sleep(3)
    name()
def name():
    name = input("\nWhat is your name, fairgoer?\n ")
    print("")
    print("Hello, " + name + "!")
# how to store name to recall later?

    print("After riding your bike around your neighborhood")
    print("you decided to see what all the excitement was about at the park\nand now you find yourself at a fence near the fairgrounds.")
    print("It looks like you are able to jump over it.\n")
    intro()
def intro():
    choice = input("Do you decide to sneak into the 1964-1965 World's Fair?\nyes or no\n ")
    if choice == "yes":
        print("")
        print("     ----------------------------------------")
        print("      WELCOME TO THE 1964-1965 WORLD'S FAIR!!")
        print("     ----------------------------------------") 
        print("")       
        print("You are now within the fair at the Court of the Five Boroughs.\nTo the left is the International Area and to the right is the Industrial Area.")
        choice = input("Would you like to know more about the areas of the fair before you proceed?\nyes or no\n ")
        if choice == "yes":
            print("\nThe areas of the fair are: Industrial, International,\nFederal and State, Transportation, Lake Amusement, and Flushing Bay.\n")
            print("The Industrial Area has 45 pavilions that showcases America's industry.\nThe International Area is represented by 80 nations in 37 pavilions.")
            print("The Federal and State Area represents 19 states.\nThe Transportation Area shows off the many forms of transportation.")
            print("The Lake Amusement Area is the smallest section, but with the most variety.\nThe Flushing Bay Area is a place for seafarers and sports fans.\n")            
            print("The site of people as well as strange and colorful buildings\nare in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To your left you see THE FIRST NATIONAL CITY BANK.")
            print("Forward is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")  
        if choice == "no":    
            print("\nThe sight of thousands of people as well as dozens of strange and colorful buildings\nare in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To your left you see THE FIRST NATIONAL CITY BANK.")
            print("Forward is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")   
        else: 
            print("I didn't understand that.") 
            second() 
    elif choice == "no":
        print("\nLooks like you are not ready for this year's World's Fair. Goodbye.")
        time.sleep(5)
        exit()
    else: 
        print("I didn't understand that.")
        intro()


# First direction choice
    choice = input("Which way do you go?\nleft, right or forward?\n ")    
    if choice == "left":
        print("\nYOU ARE AT THE FIRST NATIONAL CITY BANK PAVILION.")
        fncb_pav()
    elif choice == "forward":
        print("\nYOU ARE AT THE EASTMAN KODAK PAVILION")
        eastman_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE PEPSI-COLA PAVILION")
        pepsi_pav()
    else:
        print("I didn't understand that.")
        first()

# The start of the game 
start()