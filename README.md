# OOTP Simulator
2024/07/04

## Preparation 1 Set the env
- Download the entire folder
- `pip install -r requirements.txt`
- Make sure the `division` excel file (40320_part9.csv) is at the same level with the code
- (Ignore the Jupyter nb, it's only for demo)

![alt text](<md/截圖 2024-07-05 09.14.17.png>)

## Preparation 2 Customize parameters

### Change the position on screen for each item

- Use `get_position.py` to get the position of each item on your screen

The code will return the position where your mouse currently at. You have **2 secs** (adjustable) to move the mouse to the desired position once the function is called.

- Replace EVERY single **position of screen** for the items in `utils.py`

![alt text](<md/截圖 2024-07-05 08.49.49.png>)
(Sketch for getting the position for "NEW GAME")

### Adjust the division_path
- Replace the **division_path** in `ootp_simulator.py` `main()` line 5
- Feel free to adjust any `time.sleep()` parameters as long as it works properly

## Step 1 Adjust the index of games for each simulation

`ootp_simulator.py` `main()` line 14
```python
## Run game 1 to game 300 (adjustable)
## Do not run all the files at once, the storage space may not be enough
## Remember to start with index 301 next time

for file_index in df.index[1:300]:
```

## Step 2 Run `ootp_simulator.py`

- For every simulation, make sure you start at the main screen

![alt text](<md/截圖 2024-07-05 09.23.54.png>)

## Step 3 Upload, Delete and Restart

- Upload and Delete the game files in saved_game folder
- Restart the new simulation

## Warnings
The simulator may NOT be finished yet as the game may have other scripts (遊戲腳本). If you find other scripts, please notify me immediately.

The current scripts

```
PlayScripts:
1. Start at Mar. 18th
2. First attention: The Major League Baseball had its league structure altered -> OK 
3. Second attention: You have received a personal message! -> OK (Mar. 20th)
4. First Congrat. -> Nice (Mar. 22)
5. Third attention: Congratulations, you have won it all! / This season is over! -> OK 
6. Second Congrat. -> Nice (Apr. 1st)
````

I have simulated a few games and it works for most of the situations. For those failed simulations, most of them are because the game has not enough time to react, so remember not to be too tight on time.sleep()