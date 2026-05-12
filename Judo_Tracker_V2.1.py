import pandas as pd
import os

FILENAME = "judo_data.csv"

# 1. LOAD & CLEAN DATA (The "Self-Healing" logic)
if os.path.exists(FILENAME):
    df = pd.read_csv(FILENAME)
    df['Technique'] = df['Technique'].astype(str).str.strip().str.title()
    df['Result'] = df['Result'].astype(str).str.strip().str.title()
    df.to_csv(FILENAME, index=False)
    print(f"--- Loaded {len(df)} fights ---")
else:
    df = pd.DataFrame(columns=["Result", "Technique", "Score"])
    print("--- Created a brand new fight log ---")

def add_fight():
    global df
    print("\n[ RECORDING NEW FIGHT ]")
    print("(Type 'exit' at any prompt to cancel)")
    
    # --- Input Result ---
    while True:
        res_input = input("Result (Win/Loss): ").lower().strip()
        if res_input == 'exit' or res_input == 'e':
            print(">> Cancellation confirmed. Returning to menu.")
            return # This stops the function immediately
        
        if res_input.startswith('w'):
            result = "Win"
            break
        elif res_input.startswith('l'):
            result = "Loss"
            break
        else:
            print("(!) Enter W, L, or 'exit'.")

    # --- Input Technique ---
    tech_input = input("Technique: ").strip()
    if tech_input.lower() == 'exit':
        print(">> Cancellation confirmed.")
        return
    technique = tech_input.title()

    # --- Input Score ---
    score_input = input("Score (Ippon/Waza-ari/Shido): ").strip()
    if score_input.lower() == 'exit':
        print(">> Cancellation confirmed.")
        return
    score = score_input.title()

    # --- Final Save ---
    new_entry = pd.DataFrame([{"Result": result, "Technique": technique, "Score": score}])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(FILENAME, index=False)
    print("✔ Fight successfully saved to permanent log!")

def delete_fight():
    global df
    if df.empty:
        print("\n[!] Log is empty.")
        return

    print("\n" + "-"*10 + " CURRENT LOG " + "-"*10)
    print(df.rename(index=lambda x: x + 1)) 
    
    try:
        val = input("\nEnter the number to DELETE (or 'exit' to cancel): ").strip().lower()
        if val == 'exit' or val == 'e':
            return
        
        idx = int(val) - 1
        df = df.drop(df.index[idx]).reset_index(drop=True)
        df.to_csv(FILENAME, index=False)
        print(f"✔ Deleted entry {val}.")
    except:
        print("(!) Invalid input. No changes made.")

def show_stats():
    if df.empty:
        print("\n[!] No fights found.")
        return

    print("\n" + "█"*10 + " JUDO DASHBOARD v2.1 " + "█"*10)
    print(df.rename(index=lambda x: x + 1)) 
    
    total = len(df)
    wins = len(df[df['Result'] == 'Win'])
    
    print("-" * 35)
    print(f"Total: {total} | Wins: {wins} | Losses: {total - wins}")
    if total > 0:
        print(f"Win Rate: {(wins / total) * 100:.1f}%")
    
    winning_fights = df[df['Result'] == 'Win']
    if not winning_fights.empty:
        top_move = winning_fights['Technique'].mode()[0]
        print(f"Signature Move (Wins): {top_move}")
    print("█"*41)

# Main Menu
while True:
    print("\nMENU: [A]dd | [S]tats | [D]elete | [Q]uit")
    choice = input("Select: ").lower().strip()
    
    if choice == 'a':
        add_fight()
    elif choice == 's':
        show_stats()
    elif choice == 'd':
        delete_fight()
    elif choice == 'q':
        print("Progress saved. See you at the Dojo!")
        break