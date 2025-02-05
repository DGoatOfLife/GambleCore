import random
import time
print('How much money do you want to deposit?')
money = int(input(' '))
jackpotcounter = 0
extreameJACKPOT = {'money': 1000000, 'jackpotcounter': 30000} #☆*: .｡. o(≧▽≦)o .｡.:*☆
jACKPOT = {'money': 2500, 'jackpotcounter': 0.75} # 🥇, 🍸
miniJACKPOT = {'money': 1000, 'jackpotcounter': 0.5} # 💎
smallwin = {'money': 150, 'jackpotcounter': 0.25} # ♥️, ♠️
MajorJACKPOT = {'money': 10000, 'jackpotcounter': 1} # 7️⃣
gavble = ["7️⃣ ","🥇 ","🍸 ","💎 ","♠️ ","♥️ ", '☆*: .｡. o(≧▽≦)o .｡.:*☆']
rarity = {"7️⃣ ": 40, "🥇 ": 50,"🍸 ": 50,"💎 ": 70,"♠️ ": 80,"♥️ ": 80, '☆*: .｡. o(≧▽≦)o .｡.:*☆': 3}
# 7️⃣: $1000 4|  🥇: $2500 5|  🍸: $2500 5|  💎: $1000 7|  ♠️: $150 8|  ♥️: $150 8
gamble = []
for symbol, rority in rarity.items():
    gamble.extend([symbol] * rority)
while int(money) >= 25 and jackpotcounter < 30000:
    print('you have $' + str(money) + ' Do you wish to gamble? ')
    gamblecore = input(" ")
    if gamblecore.lower not in ['y' or 'yes']:
        print("Too bad you're addicted. You're gonna gamble anyway.")
    A1 = random.randint(0,len(gamble) - 1)
    B1 = random.randint(0,len(gamble) - 1)
    C1 = random.randint(0,len(gamble) - 1)
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
        if Damble == "☆*: .｡. o(≧▽≦)o .｡.:*☆":
            print('EXTREAME JACKPOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            jackpotcounter += extreameJACKPOT['jackpotcounter']
            money += extreameJACKPOT['money']
    if gamblecore == 'withdraw':
        print('Succesfully withdrawing your money')
        time.sleep(1.4)
        print("watch out though I'm Indian")
        time.sleep(6.3214)
        print('SYSTEMATIC ERROR')
        time.sleep(1.4)
        print("money permenantly left in code")
        break
    if gamblecore == 'counter':
        print(jackpotcounter)
        
if jackpotcounter >= 3:
    print('You are too lucky for this site, also ur now not allowed to withdraw any money.')
if money <= 0:
    print("I'm so sorry you're broke or don't have enough money to play again, feel free to break the keyboard in front of you, or you could always gimme more money")
