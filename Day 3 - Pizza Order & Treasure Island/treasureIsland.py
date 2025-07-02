print('''
.------------------------------------------------------------------------------------------.
|                        _                                     _     _                 _   |
|     ,-""-.        /)  | |                                   (_)   | |               | |  |
|    /  c/-}       //   | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |  |
|   ( ,--)T-.     //    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |  |
|    `/ ,_) )\__,-/     | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |  |
|    / /.   \'_,-"<       \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|  |
|   / /  ) _`).__                                                                          |
| _/,'  (    ""-."-.                                                                       |
|'-/   _/`-----. ),'                                                                       |
|o!O '"-'"""----"                                                                          |
`------------------------------------------------------------------------------------------`  
      ''')

print("Welcome to Treasure Island. Your mission is to find the treasure")

ti_direction = input("\nChoose direction left or right: ")

if ti_direction.lower() == "left":
    ti_action = input("Choose to swim or wait: ")

    if ti_action.lower() == "wait":
        ti_door = input("Choose red, yellow, or blue door: ")

        if ti_door.lower() == "yellow":
            print("You Win!")
            
        else:
            print("Game Over.")

    else:
        print("Game Over.")
    
else:
    print("Game Over.")