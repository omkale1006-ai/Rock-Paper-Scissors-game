import random

def check_win(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'R' and computer == 'S') or \
         (player == 'P' and computer == 'R') or \
         (player == 'S' and computer == 'P'):
        return "player"
    else:
        return "computer"

def main():
    print("🎮 Welcome to the Rock, Paper, Scissors Game!")
    print("🤖 Instructions: Choose R for Rock, P for Paper, or S for Scissors.")
    
    player = input("👉 Enter your choice (R/P/S): ").upper()

    if player not in ['R', 'P', 'S']:
        print("⚠️ Please select a valid option (R, P, or S).")
        return

    computer = random.choice(['R', 'P', 'S'])

    print(f"\n🧑 You chose: {player}")
    print(f"💻 Computer chose: {computer}")

    winner = check_win(player, computer)

    if winner == 'tie':
        print("🤝 It's a tie!")
    elif winner == 'player':
        print("🎉 You win! Great job!")
    else:
        print("😢 Computer wins! Better luck next time.")

# Start the game
main()
