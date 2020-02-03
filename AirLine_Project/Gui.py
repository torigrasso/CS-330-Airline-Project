


class Airline:

    #   Class to get a seat assignment for Customer. Keeps track of satisfaction to use for calculations in the main
    #   file.


    def __init__(self):

        #   All the seats and the spots of Window Seats as well as Aile seats

        self.Windows = [0,5,6,11,12,17,18,23,24,29,30,35,36,41,42,47,48,53,54,59,60,65,66,71,72,77,78,83,84,89,90,95,96,101,102,107,108,113,114,119,120,125]
        self.aile = [2,3,8,9,14,15,20,21,26,27,32,33,38,39,44,45,50,51,56,57,62,63,68,69,74,75,80,81,86,87,92,93,98,99,104,105,110,111,116,117,122,123]
        self.Seats = [1,0,1,0,0,0,0,0,0,0,0,0,
                 0,0,0,1,0,0,0,0,0,0,0,0,
                 0,0,0,1,0,0,0,0,0,0,0,0,
                 0,0,0,1,0,0,0,0,0,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1,0,1,1,0,0,0,
                 0,0,0,1,0,1]


    def getSeats(self):
        return self.Seats

    def setBusinessA(self,a):

        #   Seats for Business people who want a Business Priority seat
        #   Find the first Seat available in first two rows of plane, if All seats are full find first free seat
        #   from the back of the plane forward

        count = 0
        while count < 11:
            if self.Seats[count] == 0:
                self.Seats[count] = 1
                if len(a) is not 0:
                    for i in a:
                        self.Seats[i] = 0
                return count
            count += 1
        count = self.setBusinessB([])

        #   All len(a) is not 0 expressions are to take into account if reassign was selected and first seats needs to
        #   be set to open again
        if len(a) is not 0:
            for i in a:
                self.Seats[i] = 0
        return count

    def setBusinessB(self,a):

        #   Gives a seat for Business Type with no seat preference
        #   Starts from the back of plane and works forward for first free spot

        count = 125
        while count > 11:
            if self.Seats[count] == 0:
                self.Seats[count] = 1
                if len(a) is not 0:
                    for i in a:
                        self.Seats[i] = 0
                return count
            count -= 1

    def setTourist(self,a):

        #   Checks for any pair window seats and returns them if open

        count = 11
        for i in range(21):
            if self.Seats[count] == 0 and self.Seats[count + 1] == 0:
                self.Seats[count] = 1
                self.Seats[count + 1] = 1
                if len(a) is not 0:
                    for t in a:
                        self.Seats[t] = 0

                return count + 1, count

            if self.Seats[count + 4] == 0 and self.Seats[count + 5] == 0:
                self.Seats[count + 4] = 1
                self.Seats[count + 5] = 1
                if len(a) is not 0:
                    for t in a:
                        self.Seats[t] = 0

                return count + 4, count + 5
            count += 6

        # using BusinessB for a quick seat assignment to find available seats on plane for passenger

        countA = self.setBusinessB([])
        countB = self.setBusinessB([])

        if len(a) is not 0:
            for i in a:
                self.Seats[i] = 0
        return countA, countB

    def setFamilyA(self,a):

        #   Find first three seats available and return spot for 3 seats. Ignore business select seats.
        count = 12
        middleRow = 16
        while count < 126:
            if count == middleRow:
                count += 2
                middleRow += 6
            if self.Seats[count] == 0 and self.Seats[count +1] == 0 and self.Seats[count +2] == 0:
                self.Seats[count] = 1
                self.Seats[count +1] = 1
                self.Seats[count +2] = 1
                if len(a) is not 0:
                    for i in a:
                        self.Seats[i] = 0

                return count, count +1, count +2
            #   all pairs of 3 have been checked and no seats are available if count is 123
            if count == 123:
                count += 100
            count += 1
        countA = self.setBusinessB([])
        countB = self.setBusinessB([])
        countC = self.setBusinessB([])
        if len(a) is not 0:
            for i in a:
                self.Seats[i] = 0
        return countA, countB, countC

    def setFamilyB(self,a):

        #   Find first four-pair of available seats and return spot of 4 seats.
        count = 12
        middleRow = 15
        while count < 126:
            if count == middleRow:
                count += 3
                middleRow += 6
            if self.Seats[count] == 0 and self.Seats[count +1] == 0 and self.Seats[count +2] == 0 and self.Seats[count +3] == 0:
                self.Seats[count] = 1
                self.Seats[count +1] = 1
                self.Seats[count +2] = 1
                self.Seats[count +3] = 1
                if len(a) is not 0:
                    #Resets all returned seats to available
                    for i in a:
                        self.Seats[i] = 0

                return count, count + 1, count + 2, count + 3
            if count == 122:
                count += 100
            count += 1
        countA = self.setBusinessB([])
        countB = self.setBusinessB([])
        countC = self.setBusinessB([])
        countD = self.setBusinessB([])

        if len(a) is not 0:
            for i in a:
                self.Seats[i] = 0
        return countA, countB, countC, countD

    def setFamilyC(self,a):

        #   Find first five-pair of seats available and returns spot of each seat
        count = 12
        middleRow = 14
        while count < 126:
            if count == middleRow:
                count += 4
                middleRow += 6
            if self.Seats[count] == 0 and self.Seats[count + 1] == 0 and self.Seats[count + 2] == 0 and self.Seats[
                        count + 3] == 0 and self.Seats[count + 4] == 0:
                self.Seats[count] = 1
                self.Seats[count + 1] = 1
                self.Seats[count + 2] = 1
                self.Seats[count + 3] = 1
                self.Seats[count + 4] = 1
                if len(a) is not 0:
                    for i in a:
                        self.Seats[i] = 0

                return count, count + 1, count + 2, count + 3, count + 4
            if count == 121:
                count += 100

            count += 1
        countA = self.setBusinessB([])
        countB = self.setBusinessB([])
        countC = self.setBusinessB([])
        countD = self.setBusinessB([])
        countE = self.setBusinessB([])

        if len(a) is not 0:
            for i in a:
                self.Seats[i] = 0

        return countA, countB, countC, countD, countE

    def assign(self, customer, a):

        #   Function is called if reassigning is done. Will simply call respective function, reOpen returned seat and
        #   Give one more seat option


        customerType = customer.Type()
        if customerType == 'BusinessA':
            return self.setBusinessB(a)
        elif customerType == 'BusinessB':
            return self.setBusinessA(a)
        elif customerType == 'Tourist':
            return self.setTourist(a)
        elif customerType == 'FamilyA':
            return self.setFamilyA(a)
        elif customerType == 'FamilyB':
            return self.setFamilyB(a)
        else:
            return self.setFamilyC(a)