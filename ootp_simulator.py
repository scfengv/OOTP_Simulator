import gc
import pandas as pd
from utils import *
from ootp_file import ootp_file

def main():
    division_path = "/Users/shenchingfeng/Downloads/ootp/40320_part9.csv"
    col_name = [
        "file", "FirstBatter", "SecondBatter", "ThridBatter", "ForthBatter", "FifthBatter", "SixthBatter", "SeventhBatter", "EighthBatter", "NinthBatter"
    ]
    df = pd.read_csv(division_path, names = col_name, header = None)
    df.set_index("file", inplace = True)
    batter_col = df.columns
    First_game = True  # Start w/ the START SCREEN
    start_game = 900

    while True:
        for file_index in df.index[start_game:start_game + 1]:
            print(f"===== Game {file_index[6:]} =====")
            if First_game:
                FirstGame_specialized_start(file_index)
                First_game = False

            else:
                create_new_game_in_TEAMInterface_and_type_in_name(file_index)
            
            alter_starting_lineup()

            # Algorithm to auto lineup
            batter_sequence = []
            for b in batter_col:
                batter = df.loc[file_index, b].split(' ', 1)
                batter_sequence.append(int(batter[0]))
                
            # A dictionary to track the current positions of each player
            current_positions = {i: i for i in range(1, 10)}

            for i in range(len(batter_sequence)):
                target_player = batter_sequence[i]
                current_pos = current_positions[target_player]
                desired_pos = i + 1

                if current_pos != desired_pos:

                    # Find which player is currently at the desired position
                    player_at_desired_pos = next(player for player, pos in current_positions.items() if pos == desired_pos)

                    MovePlayer(target_player, player_left, current_pos, desired_pos)
                    current_positions[target_player] = desired_pos
                    current_positions[player_at_desired_pos] = current_pos

            press_play()
            gc.collect()
            start_game += 1

            if start_game % 100 == 0:
                ootp_file()
                print(f"Move and Delete Game files before {start_game}")
                print("")

if __name__ == "__main__":
    main()