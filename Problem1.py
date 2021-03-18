# 1.Let us say your expense for every month are listed below,

# January - 2200

# February - 2350

# March - 2600

# April - 2130

# May - 2190

# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


expence = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]

def ExtraFeb():
    print("January Expence are - ",expence[0][1])
    print("February Expence Are - ",expence[1][1])
    result = expence[1][1] - expence[0][1]
    print("In Feb We Spend Extra Dollers is - ",result)


def QuarterExpence():
    total = 0
    print("First 3 Month Expence Are -")
    for i in range(3):
        print(expence[i][1])
        total = total + expence[i][1]
    print("All The first quarter Expence - ",total)



def findExact():
    for i in expence:
        if i[1] == 2000:
            print("Found The Expence is 2000")
            return i
     
    print("No Expence is 2000")

def addExpence():
    expence.insert(len(expence),['June',1980])
    print(expence)


def correction():
    print("Expence Before Corrections - ",expence)
    for i in range(len(expence)):
        if expence[i][0] == 'April':
            expence[i][1] = expence[i][1] - 200
            print(expence)
            
correction()