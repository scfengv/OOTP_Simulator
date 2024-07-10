import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab

# Sleep after every operation for the game to react
# Make sure to click random place every time before next step to make sure the game work properly
random_place = (17, 172)

class module:
    def __init__(self, position, region, word) -> None:
        self.position = position
        self.region = region
        self.word = word

## 1-1 Start First game at the main screen
FirstGame_new_game = module(
    position = (181, 532),
    region = (147, 757, 416, 784), ## Get NEW QUICKSTART GAME -> which means FirstGame_new_game had successfully click
    word = "NEW QUICKSTART GAME"
)

FirstGame_start_new_quickstart_game = module(
    position = (177, 773),
    region = (600, 203, 877, 226),
    word = "LOAD QUICKSTART GAME"
)

## 1-2 Start the new game when you are in the game
file_button = module(
    position = (319, 87),
    region = (263, 141, 383, 157),
    word = "OOTP Start Screen"
)

quickstart_games = module(
    position = (310, 234),
    region = (485, 245, 651, 261),
    word = "Start New Quickstart Game"
)

start_new_quickstart_game = module(
    position = (531, 250),
    region = (600, 203, 877, 226),
    word = "LOAD QUICKSTART GAME"
)

## 1
select_template = (571, 296)
enter_name_for_the_game = (777, 443) ## MAKE SURE TO DOUBLE CLICK

create_game = module(
    position = (877, 779),
    region = (608, 148, 861, 178),
    word = "SET UP YOUR MANAGER"
)

select_MIN_TWINS = (304, 325)
select_team_OK = (1186, 832)

## Before adjust the lineup
team_button = module(
    position = (812, 86),
    region = (714, 162, 839, 179),
    word = "Team Home Screen"
)

lineup = module(
    position = (762, 255),
    region = (30, 294, 126, 319),
    word = "OVERVIEW"
)

## Position of each player at the switching lineup
player_left = {
    2: (70, 760),
    3: (70, 782),
    4: (70, 806),
    5: (70, 830),
    6: (70, 853),
    7: (70, 877),
    8: (70, 898),
    9: (70, 920),
}

## Play workflow
play_button = module(
    position = (901, 85),
    region = (834, 142, 919, 160),
    word = "Finish Today!"
)

sim_till_next_month_attention1 = module(
    position = (872, 347),
    region = (678, 407, 791, 433),
    word = "Attention!"
)

first_attention_ok = module(
    position = (915, 573),
    region = (678, 407, 791, 433), # Same with sim_till_next_month_attention1
    word = "Attention!"
)

sim_till_next_month_attention2 = module(
    position = (872, 347),
    region = (680, 433, 791, 456),
    word = "Attention!"
)

personal_message_ok = module(
    position = (886, 551), # Second attention
    region = (680, 433, 791, 456), # Same with sim_till_next_month_attention2
    word = "Attention!"
)

sim_till_next_month_congrat = module(
    position = (872, 347),
    region  = (622, 284, 846, 306),
    word = "CONGRATULATIONS!"
)

congrat_nice = module(
    position = (979, 696),
    region = (622, 284, 846, 306),
    word = "CONGRATULATIONS!"
)

congrat_ok = module(
    position = (888, 560),
    region = (679, 425, 792, 449),
    word = "Attention!"
)

sim_till_next_month_manager_of_the_year = module(
    position = (872, 347),
    region = (619, 284, 844, 309),
    word = "CONGRATULATIONS!"
)

manager_of_the_year_nice = module(
    position = (972, 699),
    region = (619, 284, 844, 309),
    word = "CONGRATULATIONS!"
)

def customized_sleep():
    time.sleep(1)
    
class Click:
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

    def __init__(self, item, max_failures = 10) -> None:
        self.item = item
        self.position = item.position
        self.region = item.region
        self.word = item.word
        self.identify_word = None
        self.click_success = False
        self.failures = 0
        self.max_failures = max_failures
        self.create_game_time = 60
    
    def _auto_click(self):
        ## Adjust setting fit your computer
        if self.item == quickstart_games:
            pyautogui.click(self.position[0], self.position[1])
            customized_sleep()

        else:
            pyautogui.click(self.position[0], self.position[1], clicks = 2)
            pyautogui.click(self.position[0] + 1, self.position[1], clicks = 2)

    def _identify_word(self):
        screenshot = ImageGrab.grab(bbox = self.region)
        self.identify_word = pytesseract.image_to_string(screenshot).strip()
        
        if self.word == self.identify_word:
            print(f"Sucessful identify {self.identify_word}")
            print("")
            self.click_success = True
            self.failures = 0

        else:
            print(f"Word: {self.word}")
            print(f"Identify word: {self.identify_word}")
            self.click_success = False
            self.failures += 1
            if self.failures >= self.max_failures:
                self.terminate_simulator()

    def terminate_simulator(self):
        raise SystemExit(f"Simulator terminated because unable to identify {self.word}.")

def auto_click(item):
    clicker = Click(item)

    while not clicker.click_success:
        clicker._auto_click()
        customized_sleep()
        clicker._identify_word()
    
def auto_click_random_place():
    pyautogui.click(random_place[0], random_place[1])

def enter():
    pyautogui.press('enter')

def normal_click(position):
    pyautogui.click(position[0], position[1], clicks = 2)
    pyautogui.click(position[0] + 1, position[1], clicks = 2)

def FirstGame_specialized_start(file_index, create_game_time):
    auto_click_random_place()
    auto_click(FirstGame_new_game)
    auto_click(FirstGame_start_new_quickstart_game)

    normal_click(select_template)
    customized_sleep()

    normal_click(enter_name_for_the_game)
    customized_sleep()

    pyautogui.write(f"{file_index}")
    customized_sleep()

    normal_click(create_game.position)
    create_game_clicker = Click(create_game)
    time.sleep(create_game_time)

    while not create_game_clicker.click_success:
        create_game_clicker._identify_word()
        if not create_game_clicker.click_success:
            time.sleep(1)

    normal_click(select_MIN_TWINS)
    customized_sleep()

    normal_click(select_team_OK)
    time.sleep(3)


def create_new_game_in_TEAMInterface_and_type_in_name(file_index, create_game_time):
    auto_click_random_place()
    auto_click(file_button)
    auto_click(quickstart_games)
    auto_click(start_new_quickstart_game)

    normal_click(select_template)
    customized_sleep()

    normal_click(enter_name_for_the_game)
    customized_sleep()

    pyautogui.write(f"{file_index}")
    customized_sleep()

    normal_click(create_game.position)
    create_game_clicker = Click(create_game)
    time.sleep(create_game_time)
    while not create_game_clicker.click_success:
        create_game_clicker._identify_word()
        if not create_game_clicker.click_success:
            time.sleep(1)

    normal_click(select_MIN_TWINS)
    customized_sleep()

    normal_click(select_team_OK)
    time.sleep(3)


def alter_starting_lineup():
    auto_click_random_place()
    auto_click(team_button)
    auto_click(lineup)
    customized_sleep()


def press_play():
    """
    PlayScripts:
    0. Start at Mar. 18th
    1. First attention: The Major League Baseball had its league structure altered -> OK 
    2. Second attention: You have received a personal message! -> OK (Mar. 20th)
    3. First Congrat. -> Nice (Mar. 22)
    4. Third attention: Congratulations, you have won it all! / This season is over! -> OK 
    5. Second Congrat. -> Nice (Apr. 1st)
    """
    auto_click_random_place()
    auto_click(play_button)
    auto_click(sim_till_next_month_attention1)
    time.sleep(1)

    first_attention_ok_clicker = Click(first_attention_ok)
    while not first_attention_ok_clicker.click_success: 
        first_attention_ok_clicker._identify_word()
        if first_attention_ok_clicker.click_success:
            time.sleep(0.5)
            enter()
            time.sleep(0.5)

            while True:
                first_attention_ok_clicker._identify_word()
                if first_attention_ok_clicker.click_success:
                    print("Word still identified after pressing enter, pressing enter again.")
                    enter()
                    time.sleep(0.5)
                    
                else:
                    print("Word no longer identified after pressing enter.")
                    print("")
                    break
            break

        else:
            time.sleep(1)

    auto_click(play_button)
    auto_click(sim_till_next_month_attention2)
    time.sleep(1)

    personal_message_ok_clicker = Click(personal_message_ok)
    while not personal_message_ok_clicker.click_success: 
        personal_message_ok_clicker._identify_word()
        if personal_message_ok_clicker.click_success:
            time.sleep(0.5)
            enter()
            time.sleep(0.5)

            while True:
                personal_message_ok_clicker._identify_word()
                if personal_message_ok_clicker.click_success:
                    print("Word still identified after pressing enter, pressing enter again.")
                    enter()
                    time.sleep(0.5)
                    
                else:
                    print("Word no longer identified after pressing enter.")
                    print("")
                    break
            break

        else:
            time.sleep(1)

    auto_click(play_button)
    auto_click(sim_till_next_month_congrat)
    time.sleep(1)

    congrat_nice_clicker = Click(congrat_nice)
    while not congrat_nice_clicker.click_success: 
        congrat_nice_clicker._identify_word()
        if congrat_nice_clicker.click_success:
            time.sleep(0.5)
            enter()
            time.sleep(0.5)

            while True:
                congrat_nice_clicker._identify_word()
                print("Word still identified after pressing enter, pressing enter again.")
                if congrat_nice_clicker.click_success:
                    enter()
                    time.sleep(0.5)

                else:
                    print("Word no longer identified after pressing enter.")
                    print("")
                    break
            break

        else:
            time.sleep(1)

    congrat_ok_clicker = Click(congrat_ok)
    while not congrat_ok_clicker.click_success: 
        congrat_ok_clicker._identify_word()
        if congrat_ok_clicker.click_success:
            time.sleep(0.5)
            enter()
            time.sleep(0.5)

            while True:
                congrat_ok_clicker._identify_word()
                if congrat_ok_clicker.click_success:
                    print("Word still identified after pressing enter, pressing enter again.")
                    enter()
                    time.sleep(0.5)

                else:
                    print("Word no longer identified after pressing enter.")
                    print("")
                    break
            break

        else:
            time.sleep(1)  

    auto_click(play_button)
    auto_click(sim_till_next_month_manager_of_the_year)
    time.sleep(1)

    manager_of_the_year_nice_clicker = Click(manager_of_the_year_nice)
    while not manager_of_the_year_nice_clicker.click_success: 
        manager_of_the_year_nice_clicker._identify_word()
        if manager_of_the_year_nice_clicker.click_success:
            time.sleep(0.5)
            enter()
            time.sleep(0.5)

            while True:
                manager_of_the_year_nice_clicker._identify_word()
                if manager_of_the_year_nice_clicker.click_success:
                    print("Word still identified after pressing enter, pressing enter again.")
                    enter()
                    time.sleep(0.5)

                else:
                    print("Word no longer identified after pressing enter.")
                    print("")
                    break
            break
        
        else:
            time.sleep(1)

    customized_sleep()


def MovePlayer(player, player_positions, from_pos, to_pos):
    pyautogui.moveTo(player_positions[from_pos], duration = 0.2)
    pyautogui.mouseDown(button = 'left')
    time.sleep(0.1)

    pyautogui.dragTo(player_positions[to_pos], duration = 0.2, button = 'left')
    pyautogui.mouseUp(button = 'left')
    time.sleep(0.1)


# batter_box = {
#     2: (50, 750, 170, 775),
#     3: (50, 775, 170, 795),
#     4: (50, 795, 170, 820),
#     5: (50, 820, 170, 842),
#     6: (50, 842, 170, 865),
#     7: (50, 865, 170, 890),
#     8: (50, 890, 170, 912)
# }

# def detect_sequence(player_sequence):
#     auto_click_random_place() # Move away the mouse
#     arranged_player_sequence = []
#     for _ in range(2, 9):
#         region = batter_box[_]
#         screenshot = ImageGrab.grab(bbox = region)
#         player = pytesseract.image_to_string(screenshot).strip()
#         arranged_player_sequence.append(player)
    
#     if player_sequence != arranged_player_sequence:
#         raise SystemExit(f"Misarrange batter sequence.")
#     else:
#         print("Correctly arrange batter sequence")