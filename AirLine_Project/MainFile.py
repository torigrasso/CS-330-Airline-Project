#   Made By Tori Grasso & Reynaldo Garcia
#   March 28, 2019
#   CS-330

from Gui import*
from Customer import*
from button import*
from random import*

def _WelcomeScreen():

    #   Creates the Welcome screen to be called on whenever with the basic buttons and greetings
    #   Returns The window and each button to be tested if clicked in main function

    WelcomeWin = GraphWin('Welcome!', 400, 200)
    WelcomeWin.setBackground('LightBlue')
    setUp = Text(Point(200, 75), "Already Have an Account")
    SetUp = Text(Point(200, 125), "Create Account")
    WelcomeText = Text(Point(200, 25), "Welcome To Our Airline!")
    WelcomeText.setSize(15)
    setUp.draw(WelcomeWin)
    SetUp.draw(WelcomeWin)
    WelcomeText.draw(WelcomeWin)
    TopButton = Button(WelcomeWin, Point(50, 75), 25, 25, '')
    BottomButton = Button(WelcomeWin, Point(50, 125), 25, 25, '')
    TopButton.activate()
    BottomButton.activate()
    return WelcomeWin, TopButton, BottomButton

def _findCustomer(customers,userName):
    #   Helper Function to find the customer that is trying to log in based on userName
    #   Goes through each customer in array and compares their Username to given userName
    num = 0
    for i in customers:
        if i.getuser() == userName:
            return num
        else:
            num += 1
    return num

def _satisfaction(customers):
    #   Function to Find the percent average Satisfaction of flight
    #   Since its average, If less then 10 people are on the plane the len of people used to calc satisfaction
    #   report is not 10
    a = []
    if len(customers) is 0:
        return 0.0
    total = 0
    if len(customers) > 10:
        temp = 10
    else:
        temp = len(customers)
    for i in range(temp):
        b = randrange(0,len(customers))
        a.append(b)
    spot = 0
    for i in range(len(customers)):
        if spot == a[i]:
            num = customers[spot].getSatisfaction()
            total += num
        spot += 1
    return total

def main():

    #   ManagerArray for Manager Credentials and Customer array to hold all customers that fly on AERO AirLine
    ManagerArray = []
    customers = []
    #   Since its event driven I need to know when everything is done. When end is changed to something that
    #   Isn't 0, Seat Assignments will stop
    end = 0

    airline = Airline()
    #   Leaving my hard coding in here b/c why not?
    #'''Fake customer Account'''
    #z = Customer('r','','','',0)
    #x = Customer('e','','e','e',0)
    #y = Customer('y','','y','y',0)
    #w = Customer('n','','n','n',0)
    #v = Customer('a','','a','a',0)
    #u = Customer('l','','l','l',0)
    #customers.append(z),customers.append(y),customers.append(x),customers.append(w),customers.append(v),customers.append(u)

    while end != 1:
        WelcomeWin, TopButton, BottomButton = _WelcomeScreen()
        #   If bottom button is clicked you'll need to create an account and the use that new account to log into
        #   the program
        if BottomButton.clicked(WelcomeWin.getMouse()) is True:
            WelcomeWin.close()
            CreateAccount = GraphWin('Create Account',400,200)
            CreateAccount.setBackground('LightBlue')
            name = Text(Point(100,100),'First Name: ')
            uName = Text(Point(100,125), 'Username:')
            pWord = Text(Point(100,150),'Password:')
            cText = Text(Point(200,25),'Create an Account')
            cText.setSize(15)
            cText.draw(CreateAccount)
            name.draw(CreateAccount)
            uName.draw(CreateAccount)
            pWord.draw(CreateAccount)
            nameEntry = Entry(Point(250,100), 10)
            nameEntry.setFill('white')
            uNameEntry = Entry(Point(250, 125), 10)
            uNameEntry.setFill('white')
            pWordEntry = Entry(Point(250,150), 10)
            pWordEntry.setFill('white')
            finish = Button(CreateAccount, Point(350, 150), 40, 25, 'Done')
            finish.activate()
            nameEntry.draw(CreateAccount), uNameEntry.draw(CreateAccount), pWordEntry.draw(CreateAccount)
            temp = CreateAccount.getMouse()
            while finish.clicked(temp) is False:
                temp = CreateAccount.getMouse()
            fName = nameEntry.getText()
            userName = uNameEntry.getText()
            password = pWordEntry.getText()
            customer = Customer(fName,'',userName,password,0)
            customers.append(customer)
            CreateAccount.close()
        #   Need to clarify if you're the manager so you have manager commands or if your
        #   another nobody trying to get from point A to point B
        else:
            WelcomeWin.close()
            VerifyWindow = GraphWin('Type',400,200)
            VerifyWindow.setBackground('lightBlue')
            Passenger = Button(VerifyWindow,Point(100,150),25,25,'')
            Manager2 = Button(VerifyWindow,Point(300,150),25,25,'')
            pText = Text(Point(100,100),'Passenger')
            mText = Text(Point(300,100),'Manager')
            mainText = Text(Point(200,50),'Are you a Passenger or Manager?')
            mainText.setSize(15)
            mainText.draw(VerifyWindow)
            pText.draw(VerifyWindow)
            mText.draw(VerifyWindow)
            Passenger.activate()
            Manager2.activate()
            #   Since you have an account at this point we need to verify its actually you. This will now check to make
            #   sure your username and password match up
            if Passenger.clicked(VerifyWindow.getMouse()):
                VerifyWindow.close()
                Login = GraphWin('Login',400,200)
                Login.setBackground('LightBlue')
                username = Text(Point(50,100),'UserName:')
                password = Text(Point(50,150),'Password:')
                username.draw(Login)
                password.draw(Login)
                userButton = Entry(Point(200,100),10)
                passButton = Entry(Point(200,150),10)
                loginText = Text(Point(200,50),'Please, Login')
                loginText.setSize(15)
                loginText.draw(Login)
                userButton.setFill('white')
                passButton.setFill('white')
                userButton.draw(Login)
                passButton.draw(Login)
                error = Text(Point(175,175),'')
                error.setFill('red')
                error.draw(Login)
                finish = Button(Login, Point(350, 150), 40, 25, 'Done')
                finish.activate()
                temp = Login.getMouse()
                done = 0
                total = 0
                #   Checking UserName and Password
                while done is 0:
                    while finish.clicked(temp) is False:
                        temp = Login.getMouse()
                    userName = userButton.getText()
                    Password = passButton.getText()
                    num = _findCustomer(customers, userName)
                    total += 1
                    #   Tells you if you have messed up your username or password so you don't freak out thinking we
                    #   messed up when really its just you for not typing correctly
                    ErrorNum = str(total)
                    #   Went through entire list and you're not on there with the given username
                    if num == len(customers):
                        error.setText('UserName or Password is incorrect.' + ErrorNum)
                        temp = Login.getMouse()
                    else:
                        #   Verifies password
                        testPass = customers[num].Verify(userName,Password)
                        if testPass == 2:
                            error.setText('UserName or Password is incorrect.' + ErrorNum)
                            temp = Login.getMouse()
                        else:
                            #   Everything matches up and we can move on. WOO!
                            done = 1
                            currentCustomer = customers[num]

                Login.close()
                #   Section to finally choose your seat. You have all the options as well as the option to
                #   Choose any box as many times as you want (Just being able to watch each box turn on and off is
                #   pretty cool. Don't know how we did it)
                select = GraphWin('Selection',400,200)
                select.setBackground('LightBlue')
                Command = Text(Point(200,25),'Select Type + Number of Seats')
                Command.setSize(20)
                BusinessText = Text(Point(250,75),'Business')
                TouristText = Text(Point(150,75),'Tourist')
                FamilyText = Text(Point(50,75),'Family')
                BusinessA = Button(select,Point(230,100),25,25,'')
                BusinessB = Button(select,Point(230,130),25,25,'')
                BAText = Text(Point(300,130),'Business Seat')
                BBText = Text(Point(300,100),'Regular Seat')
                TText = Text(Point(170,100),'2')
                FAText = Text(Point(70,100),'3')
                FBText = Text(Point(70,130),'4')
                FCText = Text(Point(70,160),'5')
                Command.draw(select)
                Tourist = Button(select,Point(140,100),25,25,'')
                FamilyA = Button(select,Point(40,100),25,25,'')
                FamilyB = Button(select,Point(40,130),25,25,'')
                FamilyC = Button(select,Point(40,160),25,25,'')
                finish = Button(select, Point(350, 175), 40, 25, 'Done')
                finish.activate()
                BAText.draw(select),BBText.draw(select),TText.draw(select),FAText.draw(select)
                FBText.draw(select),FCText.draw(select)
                BusinessText.draw(select),TouristText.draw(select),FamilyText.draw(select)
                BusinessA.activate(),BusinessB.activate(),Tourist.activate()
                FamilyA.activate(),FamilyB.activate(),FamilyC.activate()
                temp = Point(1,1)
                a = FamilyA
                #   This is what allows you to reclick any of them. Each one is turned off if you click another box
                #   and type of customer is saved as well to be added to the specific customer
                while finish.clicked(temp) is False:
                    temp = select.getMouse()
                    a.unMark()
                    if FamilyA.clicked(temp):
                        FamilyA.mark()
                        a = FamilyA
                        b = 'FamilyA'
                    elif FamilyB.clicked(temp):
                        FamilyB.mark()
                        a = FamilyB
                        b = 'FamilyB'
                    elif FamilyC.clicked(temp):
                        FamilyC.mark()
                        a = FamilyC
                        b = 'FamilyC'
                    elif Tourist.clicked(temp):
                        Tourist.mark()
                        a = Tourist
                        b = 'Tourist'
                    elif BusinessA.clicked(temp):
                        BusinessA.mark()
                        a = BusinessA
                        b = 'BusinessA'
                    elif BusinessB.clicked(temp):
                        BusinessB.mark()
                        a = BusinessB
                        b = 'BusinessB'

                currentCustomer.setCustomerType(b)
                select.close()

                #   Save all seats for ease of access working with seating graphics and the same for text so
                #   that the seats can be displayed and saved for later use on the ticket
                allSeats = []
                allText = []
                Seats = GraphWin('Seats', 600, 800)
                Seats.setBackground('LightBlue')
                Accept = Button(Seats,Point(500,25),75,30,'Accept')
                ReAssign = Button(Seats,Point(500,75),75,60,'ReAssign')
                seats = Text(Point(475,200),'')
                seats.draw(Seats)
                Accept.activate()
                ReAssign.activate()
                X = 30
                Y = 25
                x = 75
                y = 50
                row = 0
                spot = 0
                a = 65
                letter = chr(a)
                #   This right here is making all the ovals. Probably could have hard coded in every oval and would
                #   have gotten the task done faster but this is more impressive and makes the code seem more geeked
                #   out so we decided to go with this
                for i in range(126):
                    if row < 6:
                        row += 1
                    else:
                        row = 1
                    if spot > 6:
                        spot = 1
                        a += 1
                        letter = chr(a)
                    if spot == 6:
                        X = 30
                        Y += 30
                        x = 75
                        y += 30
                    if spot == 3:
                        X += 50
                        x += 50
                    rec = Oval(Point(X, Y), Point(x, y))
                    text = Text(Point(X + 20, Y + 15), str(row) + letter)
                    word = text.getText()
                    allText.append(word)
                    spot += 1
                    z = airline.getSeats()
                    if z[i] is 0:
                        rec.setFill('lightgreen')
                    else:
                        rec.setFill('Red')
                    rec.draw(Seats)
                    text.draw(Seats)
                    allSeats.append(rec)
                    X += 50
                    x += 50

                #   Finally time to assign seating. Pretty strait forward on this side of things. Check to make sure
                #   The customers type is the one we need and just calls the Seating class. Also had to assign all
                #   The seats text to 'Order' so that it could just be printed out on the ticket and for display on
                #   The seating GUI
                if b == 'FamilyA':
                    Seat1, Seat2, Seat3 = airline.setFamilyA([])
                    allSeats[Seat1].setFill('yellow')
                    allSeats[Seat2].setFill('yellow')
                    allSeats[Seat3].setFill('yellow')
                    order = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3]
                    a = [Seat1,Seat2,Seat3]
                    seats.setText(allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3])
                elif b == 'FamilyB':
                    Seat1,Seat2,Seat3,Seat4 = airline.setFamilyB([])
                    allSeats[Seat1].setFill('yellow')
                    allSeats[Seat2].setFill('yellow')
                    allSeats[Seat3].setFill('yellow')
                    allSeats[Seat4].setFill('yellow')
                    order = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4]
                    a = [Seat1,Seat2,Seat3,Seat4]
                    seats.setText(allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4])
                elif b == 'FamilyC':
                    Seat1,Seat2,Seat3,Seat4,Seat5 = airline.setFamilyC([])
                    allSeats[Seat1].setFill('yellow')
                    allSeats[Seat2].setFill('yellow')
                    allSeats[Seat3].setFill('yellow')
                    allSeats[Seat4].setFill('yellow')
                    allSeats[Seat5].setFill('yellow')
                    order = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4] + ',' + allText[Seat5]
                    a = [Seat1,Seat2,Seat3,Seat4,Seat5]
                    seats.setText(allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4] +
                                  ',' + allText[Seat5])
                elif b == 'Tourist':
                    Seat1,Seat2 = airline.setTourist([])
                    allSeats[Seat1].setFill('yellow')
                    allSeats[Seat2].setFill('yellow')
                    order = allText[Seat1] + ',' + allText[Seat2]
                    a = [Seat1,Seat2]
                    seats.setText(allText[Seat1] + ',' + allText[Seat2])
                elif b == 'BusinessA':
                    Seat1 = airline.setBusinessB([])
                    allSeats[Seat1].setFill('yellow')
                    order = allText[Seat1]
                    a = [Seat1]
                    seats.setText(allText[Seat1])
                else:
                    Seat1 = airline.setBusinessA([])
                    allSeats[Seat1].setFill('yellow')
                    order = allText[Seat1]
                    a = [Seat1]
                    seats.setText(allText[Seat1])
                temp = Point(1,1)
                #   This is the reassign area. If they want to Reassign it'll just call the assign function
                #   in the seating class to undo the previous assignment and assign new seats
                while Accept.clicked(temp) is False:
                    if ReAssign.clicked(temp):
                        for i in a:
                            allSeats[i].setFill('lightGreen')
                        if len(a) == 1:
                            Seat1 = airline.assign(currentCustomer,a)
                            a = [Seat1]
                            c = allText[Seat1]
                            seats.setText(c)
                        elif len(a) == 2:
                            Seat1, Seat2 = airline.assign(currentCustomer,a)
                            a = [Seat1,Seat2]
                            c = allText[Seat1] + ',' + allText[Seat2]
                            seats.setText(c)
                        elif len(a) == 3:
                            Seat1, Seat2, Seat3 = airline.assign(currentCustomer,a)
                            a = [Seat1,Seat2,Seat3]
                            c = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3]
                            seats.setText(c)
                        elif len(a) == 4:
                            Seat1, Seat2, Seat3, Seat4 = airline.assign(currentCustomer,a)
                            a = [Seat1,Seat2,Seat3,Seat4]
                            c = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4]
                            seats.setText(c)
                        else:
                            Seat1, Seat2, Seat3, Seat4, Seat5 = airline.assign(currentCustomer,a)
                            a = [Seat1,Seat2,Seat3,Seat4,Seat5]
                            c = allText[Seat1] + ',' + allText[Seat2] + ',' + allText[Seat3] + ',' + allText[Seat4] +',' + allText[Seat5]
                            seats.setText(c)

                        for i in a:
                            allSeats[i].setFill('yellow')
                    temp = Seats.getMouse()


                Seats.close()
                done = 0
                while done != 1:
                    SatWindow = GraphWin('Satisfied?',400,200)
                    SatWindow.setBackground('LightBlue')
                    doneButton = Button(SatWindow,Point(350,150),40,25,'Done')
                    satisfactionText = Entry(Point(200,100),20)
                    text = Text(Point(100,50),'How Satisfied Are you?')
                    text.draw(SatWindow)
                    doneButton.activate()
                    satisfactionText.draw(SatWindow)
                    temp = SatWindow.getMouse()
                    if doneButton.clicked(temp):
                        done = 1
                        Sat = satisfactionText.getText()
                        Sat = int(Sat)
                        currentCustomer.setSatisfaction(Sat)
                        SatWindow.close()

                #   Prints out the ticket with all their information for their trip
                ticket = GraphWin('Thank You',400,200)
                ticket.setBackground('LightBlue')
                Name = currentCustomer.GetName()
                Type = currentCustomer.Type()
                asSeats = Text(Point(75,100), order)
                ThankYou = Text(Point(200,150),'THANK YOU AND HAVE A NICE FLIGHT!')
                ThankYou.setOutline('Red')
                ThankYou.draw(ticket)
                flightText = Text(Point(50,50),'AirLine')
                TText = Text(Point(300,100), Type)
                Title = Text(Point(300,50), Name)
                flightText.setSize(15)
                Title.setSize(15)
                asSeats.draw(ticket)
                flightText.draw(ticket)
                Title.draw(ticket)
                TText.draw(ticket)
                temp = Point(1,1)
                FinishButton = Button(ticket,Point(375,175),40,25,'End')
                FinishButton.activate()
                while FinishButton.clicked(temp) is False:
                    temp = ticket.getMouse()
                ticket.close()
            #   This goes all the way back to the beginning if the manager clicked his section. Here he can end the
            #   flight program or get a satisfaction report
            else:
                VerifyWindow.close()
                #   If no Manager Account exsist, The manager will ened to create a Manager account before anything
                #   else can get done
                if len(ManagerArray) is 0:
                    CreateAccount = GraphWin('Create Account', 400, 200)
                    CreateAccount.setBackground('LightBlue')
                    name = Text(Point(100, 100), 'First Name: ')
                    uName = Text(Point(100, 125), 'Username:')
                    pWord = Text(Point(100, 150), 'Password:')
                    cText = Text(Point(200, 25), 'Create an Account')
                    cText.setSize(15)
                    cText.draw(CreateAccount)
                    name.draw(CreateAccount)
                    uName.draw(CreateAccount)
                    pWord.draw(CreateAccount)
                    nameEntry = Entry(Point(250, 100), 10)
                    nameEntry.setFill('white')
                    uNameEntry = Entry(Point(250, 125), 10)
                    uNameEntry.setFill('white')
                    pWordEntry = Entry(Point(250, 150), 10)
                    pWordEntry.setFill('white')
                    finish = Button(CreateAccount, Point(350, 150), 40, 25, 'Done')
                    finish.activate()
                    nameEntry.draw(CreateAccount), uNameEntry.draw(CreateAccount), pWordEntry.draw(CreateAccount)
                    temp = CreateAccount.getMouse()
                    while finish.clicked(temp) is False:
                        temp = CreateAccount.getMouse()
                    fName = nameEntry.getText()
                    userName = uNameEntry.getText()
                    password = pWordEntry.getText()
                    Manager = Customer(fName, 'Manager', userName, password, 0)
                    ManagerArray.append(Manager)
                    CreateAccount.close()
                #   The manager can log in now and do his special manager things
                Login = GraphWin('Login', 400, 200)
                Login.setBackground('LightBlue')
                username = Text(Point(50, 100), 'UserName:')
                password = Text(Point(50, 150), 'Password:')
                username.draw(Login)
                password.draw(Login)
                userButton = Entry(Point(200, 100), 10)
                passButton = Entry(Point(200, 150), 10)
                loginText = Text(Point(200, 50), 'Please, Login')
                loginText.setSize(15)
                loginText.draw(Login)
                userButton.setFill('white')
                passButton.setFill('white')
                userButton.draw(Login)
                passButton.draw(Login)
                error = Text(Point(175, 175), '')
                error.setFill('red')
                error.draw(Login)
                finish = Button(Login, Point(350, 150), 40, 25, 'Done')
                finish.activate()
                temp = Point(1,1)
                done = 0
                total = 0
                #   Checking to make sure the manager knows his username and password
                while done is 0:
                    temp = Login.getMouse()
                    userName = userButton.getText()
                    Password = passButton.getText()
                    if ManagerArray[0].Verify(userName,Password) == 2:
                        error.setText('Incorrect username or password.'+ str(total))
                        total += 1
                    else:
                        done = 1
                    while finish.clicked(temp) is False:
                        temp = Login.getMouse()
                #   Manager is now signed in and can either get a satisfaction report or end the entire flight
                Login.close()
                WelcomeWin.close()
                VerifyWindow = GraphWin('', 400, 200)
                VerifyWindow.setBackground('lightBlue')
                sat = Button(VerifyWindow, Point(100, 150), 25, 25, '')
                finish = Button(VerifyWindow, Point(300, 150), 25, 25, '')
                pText = Text(Point(100, 100), 'Sat. Report')
                mText = Text(Point(300, 100), 'End Flight')
                mainText = Text(Point(200, 50), 'How can I help?')
                mainText.setSize(15)
                mainText.draw(VerifyWindow)
                pText.draw(VerifyWindow)
                mText.draw(VerifyWindow)
                close = Button(VerifyWindow,Point(200,175),40,25,'Close')
                close.activate()
                sat.activate()
                finish.activate()
                done = 0
                while done is 0:
                    temp = VerifyWindow.getMouse()
                    if sat.clicked(temp) is True:
                        done = 1
                    elif finish.clicked(temp) is True:
                        done = 1
                    elif close.clicked(temp) is True:
                        done = 1
                    else:
                        pass
                done = 0

                while done is 0:
                    #Gives satisfaction report
                    if sat.clicked(temp):
                        stats = GraphWin('Satisfaction',400,200)
                        text = Text(Point(200,100),'')
                        total = _satisfaction(customers)
                        text.setText('Satisfaction percent = ' + str(total))
                        stats.setBackground('LightBlue')
                        text.draw(stats)
                        closed = Button(stats,Point(200,150),45,25,'Close')
                        closed.activate()
                        temp = Point(1,1)
                        while closed.clicked(temp) is not True:
                            temp = stats.getMouse()
                        stats.close()
                    #   Ends the flight :)
                    elif finish.clicked(temp):
                        end = 1
                        done = 1
                    #   Closes Manager tabs and takes you back to the welcome screen for next customer to
                    #   get his seats
                    elif close.clicked(temp):
                        done = 1
                    else:
                        pass
                    if done is 0:
                        temp = VerifyWindow.getMouse()
                VerifyWindow.close()
    #Closing out the program on a good Note
    GoodBye = GraphWin('Thank You',400,200)
    GoodBye.setBackground('LightBlue')
    text = Text(Point(200,100),'Thank you for flying'
                               ' AERO AirLine')
    text.setSize(15)
    text.setStyle('bold')
    text.setTextColor('Red')
    text.draw(GoodBye)
    GoodBye.getMouse()






if __name__ == '__main__':
    main()


