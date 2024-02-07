import keyboard
import os
import loadcfg

current = 0


# counting logic (input key, name of output file, description of counter, config settings)
def counter(key, filename, desc, config):
    global current
    start = 0
    os.system("cls")

    # increases current by 1
    if key == config.key_count_up:
        current += 1
        print("Increased by 1!")

    # decreases current by 1
    elif key == config.key_count_down:
        current -= 1
        print("Decreased by 1!")

    # resets current
    elif key == config.key_reset:
        current = start
        print("Reseted to 0!")
        
    # refreshes written content
    with open(filename, "w") as f:
        f.writelines(f"{desc}: {current}")

    # console feedback
    print(f"{desc}: {current}\n")


def help(config, desc):
    os.system("cls")
    return f"Currently refreshing \"{config.filename}\" file" \
            f"\nCounter description: {desc}" \
            f"\nCounter increase key: {config.key_count_up}" \
            f"\nCounter decrease key: {config.key_count_down}" \
            f"\nCounter reset key: {config.key_reset}" \
            f"\nConfig reload key: {config.key_refresh}" \
            f"\nExit key: {config.key_quit}" \
            f"\n\nThe description supports UTF-8 encoding, feel free to use special characters EXCEPT \";\"." \
            f"\nYou can return to the counting screen by pressing \"{config.key_return}\"." \
            f"\nYour progression will remain the same." \
            f"\n\nBasic counter script for OBS. Made by pizo in 2024.\nVersion 1.0"


# engine
def main():

    # calls loadcfg.py and initializes loaded attributes
    config = loadcfg.load_cfg()
    filename = config.filename
    desc = config.description
    os.system("cls")
    print(f"Basic counter script for OBS. Made by pizo in 2024. Version 1.0")
    print(f"Config loaded!\nPress \"{config.key_help}\" for config information!")

    # checks for the keys declared in cfg.csv, calls and manages counter func
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_UP:
            key = event.name

            # checks for increase/decrease keys
            if key == config.key_count_up or key == config.key_count_down:
                counter(key, filename, desc, config)

            # checks for reset key
            elif key == config.key_reset:
                counter(key, filename, desc, config)

            # checks for exit key
            elif key == config.key_quit:
                break

            # checks for config reload key
            elif key == config.key_refresh:
                main()

            # checks for help key
            elif key == config.key_help:
                print(help(config, desc))
                continue

            # checks for return key
            elif key == config.key_return:
                os.system("cls")
                print(f"{desc}: {current}\n")
                continue

            # false inputs
            else:
                continue


if __name__ == '__main__':
    main()
