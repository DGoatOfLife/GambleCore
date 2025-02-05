import random
import time
print('How much money do you want to deposit?')
money = int(input(' '))
jackpotcounter = 0
gavble = ["7️⃣ ","🥇 ","🍸 ","💎 ","♠️ ","♥️ "]
rarity = {"7️⃣ ": 4, "🥇 ": 5,"🍸 ": 5,"💎 ": 7,"♠️ ": 8,"♥️ ": 8}
# 7️⃣: $1000 4|  🥇: $2500 5|  🍸: $2500 5|  💎: $1000 7|  ♠️: $150 8|  ♥️: $150 8
gamble = []
for symbol, rority in rarity.items():
    gamble.extend([symbol] * rority)
while int(money) > 0 and jackpotcounter < 3:
    print('you have $' + str(money) + ' Do you wish to gamble? ')
    gamblecore = input(" ")
    if gamblecore.lower not in ['y' or 'yes']:
        print("Too bad you're addicted. You're gonna gamble anyway.")
    gamble1 = random.randint(0,len(gamble) - 1)
    gamble2 = random.randint(0,len(gamble) - 1)
    gamble3 = random.randint(0,len(gamble) - 1)
    print(gamble[gamble1] + gamble[gamble2] + gamble[gamble3])
    money = money - 25
    if gamble[gamble1] == gamble[gamble2] and gamble[gamble1] == gamble[gamble3]:
        Damble = gamble[gamble1]
        if Damble == "7️⃣ ":
            print("MAJOR JACKPOT!!!!")
            jackpotcounter += 1
            money = money + 10000
            print('you now have $' + str(money))
        if Damble == "🥇 ":
            print('small JACKPOT')
            jackpotcounter += 0.75
            money = money + 2500
            print('you now have $' + str(money))
        if Damble == "🍸 ":
            print('small JACKPOT')
            jackpotcounter += 0.75
            money = money + 2500
            print('you now have $' + str(money))
        if Damble == "💎 ":
            print('mini JACKPOT')
            jackpotcounter += 0.5
            money = money + 1000
            print('you now have $' + str(money))
        if Damble == "♥️ ":
            print('small win')
            jackpotcounter += 0.25
            money = money + 150
            print('you now have $' + str(money))
        if Damble == "♠️ ":
            print('small win')
            jackpotcounter += 0.25
            money = money + 150
            print('you now have $' + str(money))
    if gamblecore == 'withdraw':
        print('you have successfully withdrawn your money ')
        time.sleep(1.4)
        print("watch out though I'm Indian")
        time.sleep(6.3214)
        print('SYSTEMATIC ERROR')
        time.sleep(1.4)
        print("money permenantly left in code")
        break
        
        
if jackpotcounter == 3:
    print('You are too lucky for this site, also ur now not allowed to withdraw any money.')
if money <= 0:
    print("I'm so sorry you're broke, feel free to break the keyboard in front of you, or you could always gimme more money")
