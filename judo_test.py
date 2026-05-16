import pandas as pd

# 1. Create a list to store fight data
fights = []

print("--- JUDO PERFORMANCE TRACKER v1 ---")

# 2. A simple loop to let you enter multiple fights.
while True:
    result = input("Result (Win/Loss) or type 'exit' to finish: ").capitalize()
    if result == 'Exit':
        break
    
    technique = input("Technique used: ")
    score = input("Score (Ippon/Waza-ari/Shido): ")
    
    # Store the entry as a dictionary
    fights.append({"Result": result, "Technique": technique, "Score": score})
    print("Fight recorded!\n")

# 3. Use Pandas to turn the list into a Table (DataFrame)
if fights:
    df = pd.DataFrame(fights)
    
    print("\n--- YOUR FIGHT LOG ---")
    print(df)
    
    # 4. Math Logic: Calculate Win Rate
    total_fights = len(df)
    wins = len(df[df['Result'] == 'Win'])
    win_rate = (wins / total_fights) * 100
    
    print(f"\nStatistics:")
    print(f"Total Fights: {total_fights}")
    print(f"Win Rate: {win_rate}%")
    print(f"Most used technique: {df['Technique'].mode()[0]}")
else:
    print("No data entered.")
