import pandas as pd
import os

FILENAME = "judo_data.csv"

# 1. LOAD DATA: Check if we have a saved file.
if os.path.exists(FILENAME):
    df = pd.read_csv(FILENAME)
    print(f"--- Loaded {len(df)} fights from history ---")
else:
    # Create empty table if no file exists
    df = pd.DataFrame(columns=["Result", "Technique", "Score"])
    print("--- Created a brand new fight log ---")

def add_fight():
    global df
    print("\n[ RECORDING NEW FIGHT ]")
    
    # Smart Result Input (Handles Win, Won, W, Loss, Lost, L)
    while True:
        res_input = input("Result (Win/Loss): ").lower().strip()
        if res_input.startswith('w'):
            result = "Win"
            break
        elif res_input.startswith('l'):
            result = "Loss"
            break
        else:
            print("(!) Please enter something starting with 'W' or 'L'.")

    technique = input("Technique used: ").strip().capitalize()
    score = input("Score (Ippon/Waza-ari/Shido): ").strip().capitalize()

    # Add to the table
    new_entry = pd.DataFrame([{"Result": result, "Technique": technique, "Score": score}])
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # SAVE IMMEDIATELY: So you don't lose data if the power goes out
    df.to_csv(FILENAME, index=False)
    print("✔ Fight saved to your permanent log!")

def show_stats():
    if df.empty:
        print("\n[!] No fights recorded yet. Go train!")
        return

    print("\n" + "="*30)
    print("       JUDO STATISTICS")
    print("="*30)
    print(df) # Shows the full table
    
    # V1 Math Features:
    total = len(df)
    wins = len(df[df['Result'] == 'Win'])
    win_rate = (wins / total) * 100
    
    print("-" * 30)
    print(f"Total Fights: {total}")
    print(f"Wins: {wins} | Losses: {total - wins}")
    print(f"Win Rate: {win_rate:.1f}%")
    
    # Most used technique logic
    if not df['Technique'].empty:
        top_move = df['Technique'].mode()[0]
        print(f"Signature Move: {top_move}")
    print("="*30)

# Main Menu
while True:
    print("\n[M]ain Menu: (A)dd Fight | (S)tats | (Q)uit")
    choice = input("Select an option: ").lower().strip()
    
    if choice == 'a':
        add_fight()
    elif choice == 's':
        show_stats()
    elif choice == 'q':
        print("Progress saved. See you at the Dojo!")
        break
