from random import randint


##########################
def fair_coin():
    t = int(raw_input("How many times do you want to flip the coin? "))
    my_list = []
    for i in range(1, t+1):
        my_list.append(coin_flip_fair_coin())
    return my_list        

############################

def coin_flip_fair_coin():
    
    y = randint(1, 2)
    if (y == 1):
       return 'H'
    else:
       return 'T'
##############################




def ask_for_prob():
    global q
    q = int(raw_input("What is the probabilty of getting heads in percents (%) ? "))
    #This means the user enters something in %s
    


def coinflipping():
    x = raw_input("Enter n: ")
    if x == 'n':
        y = randint(1, 100)
        if (y <= q):
           return 'H'
        if (not (y <= q)):
           return 'T'
    else:
        return "I told you to press n "
        coinflipping()

if __name__ == "__main__":
    #ask_for_prob()
    #coinflipping()
    print fair_coin()
