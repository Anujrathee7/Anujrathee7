import random
def game():
    random.seed(42)
    while True:
        shape = input("Rock, Paper, Scissors (type 'Exit' to quit):\n")
        choice =  ["Rock", "Paper", "Scissors"]
        computer = choice[random.randint(0,2)]
        if(computer == shape):
            print("It was a tie!")
        
        elif(computer == "Rock" and shape == "Scissors") or (computer == "Paper" and shape == "Rock") or (computer == "Scissors" and shape == "Paper"):
            print(f"You lost! {shape} loses to {computer}")
        elif(shape == "Rock" and computer == "Scissors") or (shape == "Paper" and computer == "Rock") or (shape == "Scissors" and computer == "Paper"):
            print(f"You won! {shape} triumphs {computer}")
        elif(shape == "Exit"):
            break
        else:
            print("That's not a valid play. Check your spelling!")


game()