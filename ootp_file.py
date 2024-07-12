import os
import shutil

class OOTPFile:
    """
    What this code will do
    - Check if OOTP games were properly run during the simulation
    - Change csv folders name to 40320_xxxxx
    - Move all the csv folders to organized_path (let you upload them at once)

    Workflow
    0. Loop through all the folders in saved_game
    1. Find "40320_xxxxx.lg" folder
    2. Check if game properly run
    -> Check if /40320_xxxxx.lg/dump/dump_2024_03/csv/games.csv lines == 2 (col. name & game stats)
    3. If Yes:
        - Change csv folder name to 40320_xxxxx 
        - Move csv folder to designated folder
       else: 
        - print("Game 40320_xxxxx did not properly run")

    All you have to do
    1. Change base_dir @ main()
    2. Create organized_path @ your computer (Wherever you like)
    3. Change organized_path @ main()

    Explanation
    - base_dir = /path/to/saved_games
    - organized_path = /path/to/where you wish to organize all the csv file
    """
    def __init__(self, base_dir, organized_path, item) -> None:
        self.base_dir = base_dir
        self.organized_path = organized_path
        self.item = item
        self.lg_folder_name = None
        self.lg_folder_path = None
        self.csv_folder_path = None
        self.if_lg_folder = False
        self.proper_run = False
    
    def find_lg_folder(self):
        """
        Step 0 ~ 1
        """
        item_path = os.path.join(self.base_dir, self.item)

        if self.item.endswith('.lg'):
            self.if_lg_folder = True
            self.lg_folder_name = self.item[:-3]
            self.lg_folder_path = item_path
    
    def check_game(self):
        """
        Step 2
        """

        # To avoid those .dat or other files
        if self.if_lg_folder:
            self.csv_folder_path = os.path.join(self.lg_folder_path, 'dump', 'dump_2024_03', 'csv')

            # Check if the csv directory exists (To avoid those games that have been moved)
            if os.path.isdir(self.csv_folder_path):
                games_csv_path = os.path.join(self.csv_folder_path, 'games.csv')

                if os.path.isfile(games_csv_path):
                    with open(games_csv_path, 'r') as file:
                        lines = file.readlines()
                        if len(lines) != 2:
                            print(f"Game {self.lg_folder_name} did not properly run")

                        else:
                            self.proper_run = True
    
    def move_game(self):
        """
        Step 3
        """

        if self.proper_run:
            new_folder_path = os.path.join(self.lg_folder_path, 'dump', 'dump_2024_03', self.lg_folder_name)

            # Rename
            os.rename(self.csv_folder_path, new_folder_path)

            # Move
            destination_path = os.path.join(self.organized_path, self.lg_folder_name)
            shutil.move(new_folder_path, destination_path)
            print(f"Move Folder {self.lg_folder_name}")

    def remove_lg_folders(self):
        """
        Remove all ".lg" folders in base_dir
        """
        for item in os.listdir(self.base_dir):
            item_path = os.path.join(self.base_dir, item)
            if item.endswith('.lg') and os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed folder: {item}")

def ootp_file():
    base_dir = '/Users/shenchingfeng/Library/Containers/com.ootpdevelopments.ootp25macqlm/Data/Application Support/Out of the Park Developments/OOTP Baseball 25/saved_games'
    organized_path = '/Users/shenchingfeng/Downloads/organized_csv'
    
    for item in os.listdir(base_dir):
        file_operator = OOTPFile(base_dir, organized_path, item)
        file_operator.find_lg_folder()
        file_operator.check_game()
        file_operator.move_game()

    # file_operator.remove_lg_folders()
    
if __name__ == "__main__":
    ootp_file()
