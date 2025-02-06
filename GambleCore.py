import random
import time
print('How much money do you want to deposit?')
moolah = int(input(' '))
print('What gambling game do you want to play')
Gameplaying = input('We have Slot Machine')
def SlotMachine(money):
    jackpotcounter = 0
    extreameJACKPOT = {'money': 1000000, 'jackpotcounter': 3} #☆*: .｡. o(≧▽≦)o .｡.:*☆
    jACKPOT = {'money': 2500, 'jackpotcounter': 0.75} # 🥇, 🍸
    miniJACKPOT = {'money': 1000, 'jackpotcounter': 0.5} # 💎
    smallwin = {'money': 150, 'jackpotcounter': 0.25} # ♥️, ♠️
    MajorJACKPOT = {'money': 10000, 'jackpotcounter': 1} # 7️⃣
    rarity = {"7️⃣ ": 4000, "🥇 ": 5000,"🍸 ": 5000,"💎 ": 7000,"♠️ ": 8000,"♥️ ": 8000, "☆*: .｡. o(≧▽≦)o .｡.:*☆ ": 300}
    # 7️⃣: $1000 4|  🥇: $2500 5|  🍸: $2500 5|  💎: $1000 7|  ♠️: $150 8|  ♥️: $150 8
    gamble = []
    for symbol, rority in rarity.items():
        gamble.extend([symbol] * rority)
    while int(money) >= 25 and jackpotcounter < 3:
        print('you have $' + str(money) + ' Do you wish to gamble? ')
        gamblecore = input(" ")
        if gamblecore.lower not in ['y' or 'yes']:
            print("Too bad you're addicted. You're gonna gamble anyway.")
        A1 = random.randint(0,len(gamble) - 1)
        if gamble[A1] == "7️⃣ ":
            rarity.update({"7️⃣ ": 3000})
        if gamble[A1] == "🥇 ":
            rarity.update({"🥇 ": 3750})
        if gamble[A1] == "🍸 ":
            rarity.update({"🍸 ": 3750})
        if gamble[A1] == "💎 ":
            rarity.update({"💎 ": 5250})
        if gamble[A1] == "♠️ ":
            rarity.update({"♠️ ": 6000})
        if gamble[A1] == "♥️ ":
            rarity.update({"♥️ ": 6000})
        if gamble[A1] == "☆*: .｡. o(≧▽≦)o .｡.:*☆ ":
            rarity.update({"☆*: .｡. o(≧▽≦)o .｡.:*☆ ": 225})
        print(rarity)
        B1 = random.randint(0,len(gamble) - 1)
        if gamble[B1] == "7️⃣ " and gamble[A1] == gamble[B1]:
            rarity.update({"7️⃣ ": 1500})
        if gamble[B1] == "🥇 " and gamble[A1] == gamble[B1]:
            rarity.update({"🥇 ": 1875})
        if gamble[B1] == "🍸 " and gamble[A1] == gamble[B1]:
            rarity.update({"🍸 ": 1875})
        if gamble[B1] == "💎 " and gamble[A1] == gamble[B1]:
            rarity.update({"💎 ": 2625})
        if gamble[B1] == "♠️ " and gamble[A1] == gamble[B1]:
            rarity.update({"♠️ ": 3000})
        if gamble[B1] == "♥️ " and gamble[A1] == gamble[B1]:
            rarity.update({"♥️ ": 3000})
        if gamble[B1] == "☆*: .｡. o(≧▽≦)o .｡.:*☆ ":
            rarity.update({"☆*: .｡. o(≧▽≦)o .｡.:*☆ ": 200})
        print(rarity)
        C1 = random.randint(0,len(gamble) - 1)
        rarity = {"7️⃣ ": 4000, "🥇 ": 5000,"🍸 ": 5000,"💎 ": 7000,"♠️ ": 8000,"♥️ ": 8000, "☆*: .｡. o(≧▽≦)o .｡.:*☆ ": 300}
        print(gamble[A1] + gamble[B1] + gamble[C1])
        money = money - 25
        if gamble[A1] == gamble[B1] and gamble[A1] == gamble[C1]:
            Damble = gamble[A1]
            if Damble == "7️⃣ ":
                print("MAJOR JACKPOT!!!!")
                jackpotcounter += MajorJACKPOT['jackpotcounter']
                #money += 10000
                money += MajorJACKPOT['money']
                print('you now have $' + str(money))
            if Damble == "🥇 ":
                print('JACKPOT')
                jackpotcounter += jACKPOT['jackpotcounter']
                #money += 2500
                money += jACKPOT['money']
                print('you now have $' + str(money))
            if Damble == "🍸 ":
                print('JACKPOT')
                jackpotcounter += jACKPOT['jackpotcounter']
                #money += 2500
                money += jACKPOT['money']
                print('you now have $' + str(money))
            if Damble == "💎 ":
                print('mini JACKPOT')
                jackpotcounter += miniJACKPOT['jackpotcounter']
            #money += 1000
                money += miniJACKPOT['money']
                print('you now have $' + str(money))
            if Damble == "♥️ ":
                print('small win')
                jackpotcounter += smallwin['jackpotcounter']
                #money += 150
                money += smallwin['money']
                print('you now have $' + str(money))
            if Damble == "♠️ ":
                print('small win')
                jackpotcounter += smallwin['jackpotcounter']
                #money += 150
                money += smallwin['money']
                print('you now have $' + str(money))
            if Damble == "☆*: .｡. o(≧▽≦)o .｡.:*☆ ":
                print('EXTREAME JACKPOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                jackpotcounter += extreameJACKPOT['jackpotcounter']
                money += extreameJACKPOT['money']
                print('you now have $' + str(money))
        if gamblecore.lower == 'withdraw':
            print('Succesfully withdrawing your money')
            time.sleep(1.4)
            print("watch out though I'm Indian")
            time.sleep(2.34)
            print('SYSTEMATIC ERROR')
            time.sleep(1.4)
            print("money permenantly left in code")
            break
        if gamblecore.lower == 'counter':
            print(jackpotcounter)
        if gamblecore.lower == 'changegame':
            break
        if gamblecore.lower == 'inst':
            break
        
    if jackpotcounter >= 3:
        print('You are too lucky for this site, also ur now not allowed to withdraw any money.')
    if money <= 0:
        print("I'm so sorry you're broke or don't have enough money to play again, feel free to break the keyboard in front of you, or you could always gimme more money")
if Gameplaying.upper == 'SM' or 'SLOTMACHINE':
    SlotMachine(moolah)
else:
    SlotMachine(moolah)