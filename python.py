from random import randint
    
heads = 0
tails = 1
   
flip = int(input("How many times do you want to flip a coin? : "))
    
#Keep track of the largest run    
maxHeads = 0
maxTails = 0

#Keep track of the current number of heads or tails in a run
headRunCounter = 0
tailRunCounter = 0

#Keep track of what the previous coin flip was using a 0 or a 1
previousFlip = 0

for i in range(flip):
    result = randint(0,1)
    if result == 0:
        print("Heads")
        heads += 1
        
        #Check to see if the previous flip was a Tails.
        if previousFlip == 1:
            #Check to see if the previous run of Tails set a new record
            if tailRunCounter > maxTails:
                maxTails = tailRunCounter
            #Reset the Tails run counter
            tailRunCounter = 0
        headRunCounter += 1
        #Track the previous coin flip
        previousFlip = 0
    else:
        print("Tails")
        tails += 1
        
        #Check to see if the previous flip was a Heads
        if previousFlip == 0:
        #Check to see if the previous run of Heads set a new record
            if headRunCounter > maxHeads:
                maxHeads = headRunCounter
                #Reset the Heads run counter
            headRunCounter = 0
        tailRunCounter += 1
        #Track the previous coin flip
        previousFlip = 1



if tailRunCounter > maxTails:
    maxTails = tailRunCounter
    
if headRunCounter > maxHeads:
    maxHeads = headRunCounter
  
print("Here is what happened:")
print("Heads", heads)
print("Tails", tails)

#Print out the max Heads and Tails that were in a run.
print("Number of 'Heads' in a row:", maxHeads)
print("Number of 'Tails' in a row:", maxTails)
