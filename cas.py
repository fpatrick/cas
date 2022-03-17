import subprocess


# Initial function to loop valid options
def start():
    print()
    print("***********************************************************************")
    print("*                Welcome to Command and Script v0.8                   *")
    print("* Dependency: Run with sudo. Install screen (sudo apt install screen) *")
    print("* https://github.com/fpatrick                                         *")
    print("***********************************************************************")
    print()
    print(">>> Choose an option: | 1 - Run commands in background | 2 - Create script to run on Cron | 0 - Exit ")

    menu_choice = int(input())
    while menu_choice > 2:
        menu_choice = int(input(">>> Please choose a valid option (0 to 2): "))

    return menu_choice


# Call initial function to start program
menu = start()


# Make folder to store scripts
def make_folder():
    print(">>> Please enter full path where the script will be created (ex: /example/yourfolder):")
    folder_path = input()
    command = "mkdir -p " + folder_path
    result_command = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result_command.returncode == 0:
        return folder_path
    else:
        print(">>> The folder couldn't be created due to an error:")
        print(result_command.stderr)
        return folder_path


# Make file and add the user commands on provided folder
def make_file(user_folder, user_command):
    print(">>> What will be the script name?")
    script_name = input()
    screen_command = "screen -dmS section_created_by_script  bash -c " + "'" + user_command + "'"
    try:
        f_path = user_folder + '/' + script_name + '.py'
        with open(f_path, 'w') as f:
            f.write('import subprocess\n')
            f.write('subprocess.run("' + screen_command + '", shell=True, capture_output=True, text=True)')

        print(f"\n*************** Script created on {f_path} ***************\n")
        return f_path
    except:
        print(">>> The script couldn't be created")


def close_program():
    print(">>> Would you like to exit this program? y / n")
    choice = input()
    while choice != "y" and choice != "n":
        choice = input(">>> Please write y or n: ")

    if choice == "y":
        exit()
    else:
        start()


# If choice is just to run a command
if menu == 1:
    print(">>> * Info: you can install screen with sudo apt install screen *")

    userCommand = input(">>> What command would you like to run?: ")
    screenCommand = "screen -dmS section_created_by_script  bash -c " + "'" + userCommand + "'"
    subprocess.run(screenCommand, shell=True, capture_output=True, text=True)
    result = subprocess.run("screen -ls", shell=True, capture_output=True, text=True)
    print(">>> Your screen section will remain open when command finish. (screen -list  and then  screen kill number)")
    print()
    print(result.stdout)
    close_program()

# If choice is to create a script
elif menu == 2:
    print(">>> What command would you like to run? ")
    userCommand = input()

    folder = make_folder()
    fullPath = make_file(folder, userCommand)
    print(">>> Instructions on how to make a cron job with the script created:\n")
    print("> Enter https://crontab.guru (and get the schedule)")
    print("> Enter on terminal: which python3 (and get the python's path)")
    print("> Enter on terminal: sudo crontab -e")
    print("> Write on same line: <schedule> <python3 path> <script full path>  <optional log>")
    print(f"> Example: * * * * * /usr/bin/python3 /folders/{fullPath} >> ~/cron.log 2>&1 \n\n")
    close_program()

elif menu == 0:
    exit()
