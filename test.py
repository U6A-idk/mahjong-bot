Dictionary_Suits={1:"bamboo",2:"dots",3:"characters",4:"honors",5:"bonus"}

Eyes = []
Pengs = []
Chis = []   
Kons = []
Possible=[]

# removing eyes from hand, so easier
def eye(hand):
    hand.sort()
    Eyes = []
    Temp_hand = hand.copy()
    for tile in hand:
        count = Temp_hand.count(tile)
        if count >= 2 and tile not in Eyes:
            Eyes.append(tile)
            for i in range(2):
                Temp_hand.remove(tile)
    return Eyes


def Sets(hand, pengs, chis, kons, eyes):

    #hand empty, append to global, return to get next possibility
    if not hand:
        Possible.append({"pengs": pengs[:],"chis": chis[:],"kons": kons[:],"eyes": eyes})
        return

    #take first
    first = hand[0]

    #Kon, append into kon, recursive call

    if hand.count(first) >= 4:
        Temp = hand.copy()
        for i in range(4):
            Temp.remove(first)
        Sets(Temp, pengs, chis, kons + [first], eyes)

        
    #Peng, append into peng, and recursive call
    if hand.count(first) >= 3:
            Temp = hand.copy()
            for i in range(3):
                Temp.remove(first)
            Sets(Temp, pengs + [first], chis, kons, eyes)



    #Chi, test for same suit, append into chi, and recursive call
    if first + 1 in hand and first + 2 in hand:
            Temp = hand.copy()
            suit = Dictionary_Suits[(first-1)//9 +1]
            if suit in ["bamboo", "dots", "characters"]:
                rank = (first-1)%9 +1
                if rank < 8:
                    Temp.remove(first)
                    Temp.remove(first+1)
                    Temp.remove(first+2)
                    Sets(Temp, pengs, chis + [first], kons, eyes)

    #if left with tiles, but no sets, return to get next possibility            
    return False







N_hand = [4,4,4,5,5,5,6,6,6,12,12,12,23,23]

Pengs.clear()
Chis.clear()
Eyes.clear()
Kons.clear()
Possible.clear()

pairs = eye(N_hand)


for pair in pairs:

#eye testing
    Temp = N_hand.copy()
    Temp.remove(pair)
    Temp.remove(pair)
#run possible sets with the eye tested, append
    Sets(Temp, [], [], [], pair)

#numbering solutions
for i, j in enumerate(Possible, 1):
    print("Solution", i)
    print("Pengs:", j["pengs"])
    print("Chis:", j["chis"])
    print("Kons:", j["kons"])
    print("Eyes:", j["eyes"])
    print("------------------------------------------------------------")



