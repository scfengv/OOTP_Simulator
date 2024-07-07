import os
import shutil

class OOTPFile:

    """
    Workflow
    0. Loop through all the folders in saved_game
    1. Find "40320_xxxxx.lg" folder
    2. Check if game properly run
    -> Check if /40320_xxxxx.lg/dump/dump_2024_03/csv/games.csv lines == 2 (col. name and game stats)
    3. If Yes: 
        - Change csv name to 40320_xxxxx 
        - Move csv folder to designated folder to upload at once 
       else: 
        - print("Game 40320_xxxxx did not properly run")
    """

    def __init__(self, base_dir, organized_path, item) -> None:
        self.base_dir = base_dir
        self.organized_path = organized_path
        self.item = item
        self.lg_folder_name = None
        self.lg_folder_path = None
        self.csv_folder_path = None
        self.csv_file = None
        self.proper_run = False
    
    def find_lg_folder(self):
        """
        Step 0 ~ 1
        """
        item_path = os.path.join(self.base_dir, self.item)

        if self.item.endswith('.lg'):
            self.lg_folder_name = self.item[:-3]
            self.lg_folder_path = item_path
    
    def check_game(self):
        """
        Step 2
        """

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




# /path/to/saved_games
base_dir = '/Users/shenchingfeng/Library/Containers/com.ootpdevelopments.ootp25macqlm/Data/Application Support/Out of the Park Developments/OOTP Baseball 25/saved_games'

# The folder you wish all the csv to be
##### Create this folder beforehand #####
organized_path = '/Users/shenchingfeng/Downloads/organized_csv'

for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    
    if os.path.isdir(item_path) and item.endswith('.lg'):
        lg_folder_name = item[:-3]
        
        # /path/to/csv
        csv_folder_path = os.path.join(item_path, 'dump', 'dump_2024_03', 'csv')
        
        # Check if the csv folder exists
        if os.path.exists(csv_folder_path) and os.path.isdir(csv_folder_path):
            new_folder_path = os.path.join(item_path, 'dump', 'dump_2024_03', lg_folder_name)
            
            # Rename the csv folder
            os.rename(csv_folder_path, new_folder_path)

            # Move all the csv folder to a designated folder to upload at once
            destination_path = os.path.join(organized_path, lg_folder_name)
            shutil.move(new_folder_path, destination_path)

        else:
            print(f'csv folder not found in {item_path}')
