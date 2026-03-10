from collections import Counter
Dictionary_Suits={1:"bamboo",2:"dots",3:"characters",4:"honors",5:"bonus"}
Dictionary_Ranks={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"dragon",11:"flower",12:"season"}
Pengs=[]
Chis=[]
Mirrors=[]
Kons=[]

#Peng: three identical tiles, append one into Pengs
#M_Sort to place into Pengs and Chis, then remove from hand

def Peng(hand): 
    hand.sort()
    first = hand[0]
    count = hand.count(first)
    if count >= 3:
        Pengs.append(first)
        for i in range(3):
            hand.remove(first)

#Chi: Increasing 3 tiles, append first into Chis

def Chi(hand):
    hand.sort()
    first = hand[0]
    suit = Dictionary_Suits[(first-1)//9 +1]
    if suit in ["bamboo", "dots", "characters"]:
        rank = (first-1)%9 +1
        if rank < 8:
            second = first + 1
            third = first + 2
            if second in hand and third in hand:
                Chis.append(first)
                hand.remove(first)
                hand.remove(second)
                hand.remove(third)

#Mirror: 2 identical tiles, append into Mirrors

def Mirror(hand):
    hand.sort()
    first = hand[0]
    count = hand.count(first)
    if count >= 2:
        Mirrors.append(first)
        for i in range(2):
            hand.remove(first)         

# Kon: 4 Identical tiles, append into Kons

def Kon(hand):
    hand.sort()
    first = hand[0]
    count = hand.count(first)
    if count >= 4:
        Kons.append(first)
        for i in range(4):
            hand.remove(first)

#sorting hand into Suits, and number of each
def count_suits(hand):
    suit_counts=Counter()
    for tile in hand:
        suit=Dictionary_Suits[(tile-1)//9+1]
        suit_counts[suit]+=1
    return suit_counts 






New_hand=[1,1,1,2,3,4,4,4,5,5,5,5]
Test_hand= New_hand.copy()


print(Test_hand)
print("Pengs:", Pengs)
print("Chis:", Chis)
print("Mirrors:", Mirrors)
print("Kons:", Kons)
