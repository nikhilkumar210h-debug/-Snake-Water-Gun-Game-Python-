# snake water and gun game
import random
mapping = {
    0: "Snake 🐍",
    1: "Gun ",
    2: "Water 💧"
}
s = [2 , 1 , 0]
user_score = 0
comp_score = 0
rounds = 0

print("Welcome To Snake🐍. Water💧 ,Gun🔫 Game")
while True:
    rounds += 1
    try:
     i = int(input("\nChoose one of them\n'0' for snake '2' for water '1' for gun \npress '3' for quit: "))
     if i == 3:
         print("Have a nice day")
         break
     if i not in [0, 1, 2]:
         print("Invalid Input ❌")
         continue
     c = random.choice(s)
     r = (i - c)%3
     if r== 1 :
        print("\n\tYou Win😎\n")

        print(f"Computer: {mapping[c]}\nYou: {mapping[i]}")
        user_score += 1

     elif r == 2:
        print("\n\tYou Lose🤦‍♂️\n")

        print(f"Computer: {mapping[c]}\nYou: {mapping[i]}")
        comp_score += 1

     elif r == 0:
        print("\n\tDraw🤷‍♂️\n")
        print(f"Computer: {mapping[c]}\nYou: {mapping[i]}")

     print("\nFinal Score:")
     print("You:", user_score)
     print("Computer:", comp_score)
     if user_score > comp_score:
         print("🏆 You won the match!")
     elif comp_score > user_score:
         print("💻 Computer won the match!")
     else:
         print("🤝 Match Draw!")

    except ValueError:
       print("\nPlease Enter Number Not String❌.")


