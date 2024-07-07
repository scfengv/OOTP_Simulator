import time
import pyautogui

# Position on my screen
# Sleep after every operation for the game to react
# Make sure to click random place every time before next step to make sure the game work properly
random_place = (17, 172)

## 1-1 Start First game at the main screen
FirstGame_new_game = (181, 532)
FirstGame_start_new_quickstart_game = (177, 773)

## 1-2 Start the new game when you are in the game
file_button = (319, 87)
quickstart_games = (310, 234)
start_new_quickstart_game = (531, 250)
select_template = (571, 296)
enter_name_for_the_game = (777, 443) ## MAKE SURE TO DOUBLE CLICK
create_game = (877, 779)
select_MIN_TWINS = (304, 325)
select_team_OK = (1186, 832)

## Before adjust the lineup
team_button = (812, 86)
lineup = (762, 255)
overview = (72, 301)

## Position of each player at the switching lineup
player_left = {
    2: (355, 765),
    3: (355, 783),
    4: (355, 807),
    5: (355, 830),
    6: (355, 853),
    7: (355, 877),
    8: (355, 898),
    9: (355, 920),
}

player_right = {
    # player_left (x + 440, y)
    2: (795, 765),
    3: (795, 783),
    4: (795, 807),
    5: (795, 830),
    6: (795, 853),
    7: (795, 877),
    8: (795, 898),
    9: (795, 920),
}

## Play workflow
play_button = (901, 85)
sim_till_next_month = (872, 347)
first_attention_ok = (915, 573)
personal_message_ok = (886, 551) # Second attention
congrat_nice = (979, 696)
congrat_ok = (888, 560)
manager_of_the_year_nice = (972, 699)

def customized_sleep():
    time.sleep(1.1)

def auto_click(module):
    pyautogui.click(module[0], module[1], clicks = 2)
    pyautogui.click(module[0] + 1, module[1], clicks = 2) ## Double check cause the game is really written poorly

def FirstGame_specialized_start(file_index):
    auto_click(random_place)
    customized_sleep()

    auto_click(FirstGame_new_game)
    customized_sleep()

    auto_click(FirstGame_start_new_quickstart_game)
    customized_sleep()

    auto_click(select_template)
    customized_sleep()

    auto_click(enter_name_for_the_game)
    customized_sleep()

    pyautogui.write(f"{file_index}")
    customized_sleep()

    auto_click(create_game)
    time.sleep(75)  ## Avg around 1min5sec, but leave some buffer time just in case

    auto_click(select_MIN_TWINS)
    customized_sleep()

    auto_click(select_team_OK)
    time.sleep(3)


def create_new_game_in_TEAMInterface_and_type_in_name(file_index):
    auto_click(random_place)
    customized_sleep()

    auto_click(file_button)
    customized_sleep()

    # auto_click(quickstart_games)
    pyautogui.click(quickstart_games[0], quickstart_games[1])
    customized_sleep()

    auto_click(start_new_quickstart_game)
    customized_sleep()

    auto_click(select_template)
    customized_sleep()

    auto_click(enter_name_for_the_game)
    customized_sleep()

    pyautogui.write(f"{file_index}")
    customized_sleep()

    auto_click(create_game)
    time.sleep(75)

    auto_click(select_MIN_TWINS)
    customized_sleep()

    auto_click(select_team_OK)
    time.sleep(5)


def alter_starting_lineup():
    auto_click(random_place)
    customized_sleep()

    auto_click(team_button)
    customized_sleep()

    auto_click(lineup)
    customized_sleep()

    auto_click(overview)
    customized_sleep()


def MovePlayer(player, player_positions, from_pos, to_pos):
    pyautogui.moveTo(player_positions[from_pos], duration = 0.2)
    pyautogui.mouseDown(button = 'left')
    customized_sleep()

    pyautogui.dragTo(player_positions[to_pos], duration = 0.2, button = 'left')
    pyautogui.mouseUp(button = 'left')
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
    auto_click(random_place)
    customized_sleep()

    auto_click(play_button)
    customized_sleep()

    auto_click(sim_till_next_month)
    customized_sleep()

    auto_click(first_attention_ok)
    customized_sleep()

    auto_click(play_button)
    customized_sleep()

    auto_click(sim_till_next_month)
    time.sleep(4)

    auto_click(personal_message_ok)
    customized_sleep()

    auto_click(play_button)
    customized_sleep()

    auto_click(sim_till_next_month)
    time.sleep(5)

    auto_click(congrat_nice)
    customized_sleep()

    auto_click(congrat_ok)
    customized_sleep()

    auto_click(play_button)
    customized_sleep()

    auto_click(sim_till_next_month)
    time.sleep(3)

    auto_click(manager_of_the_year_nice)
    customized_sleep()
