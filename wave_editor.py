from wave_helper import *

# messages for user
ENTRY_MSG = "WELCOME: press the number of the option: \n" \
            "1.edit wav \n2.compose wav \n3.abort program "
WAV__FILENAME_REQUEST = "write down wav filename"
WRONG_WAVE_FILENAME = "wave file name was incorrect"
CHANGING_WAVE_MENU_MSG = "File edit menu:press the number of the option: \n " \
                         " 1. reverse wav \n        2. audio off \n" \
                         " 3. increase wav volume \n4. increase wav speed\n " \
                         " 5.decrease wav volume \n 6.  decrease_wav_speed \n" \
                         " 7.low path filter \n     8.  move to end menu"
MENU_INPUT_INCORRECT = "your menu input was incorrect"


# help functions
def display(msg):
    print(msg)


def get_menu_input(input_option, wrong_input_msg):
    user_input = input()
    if int(user_input) in input_option:
        return user_input
    else:
        display(wrong_input_msg)
        get_menu_input(input_option, wrong_input_msg)


# edit functions
def reverse_wav(wave_file):
    return wave_file[1]


def audio_off(file_name):
    pass


def increase_wav_speed(file_name):
    pass


def decrease_wav_speed(file_name):
    pass


def increase__wav_volume(file_name):
    pass


def decrease__wav_volume(file_name):
    pass


def low_path_filter(file_name):
    pass


def load_wave_file():
    while True:
        display(WAV__FILENAME_REQUEST)
        file_name = input()
        load_file = load_wave(file_name)
        if load_file != -1:
            return load_file, file_name
        else:
            display(WRONG_WAVE_FILENAME)


def call_edit_function(user_input, wave_file):
    if user_input == 1:
        reverse_wav(wave_file)
    elif user_input == 2:
        audio_off()
    elif user_input == 3:
        increase__wav_volume()
    elif user_input == 4:
        increase_wav_speed()
    elif user_input == 5:
        decrease__wav_volume()
    elif user_input == 6:
        decrease_wav_speed()
    elif user_input == 7:
        low_path_filter()
    elif user_input == 8:
        return "8"


def end_menu(file_name):
    pass


def changing_wav_menu():
    wave_file, file_name = load_wave_file()
    wave_file = list(wave_file)
    in_edit_mode = True
    while in_edit_mode:
        display(CHANGING_WAVE_MENU_MSG)
        user_input = get_menu_input({1, 2, 3, 4, 5, 6, 7, 8}
                                    , MENU_INPUT_INCORRECT)

        if call_edit_function(user_input, wave_file) is "8":
            in_edit_mode = False
        else:  # save wave file and another iteration
            save_wave(wave_file[0], wave_file[1], file_name)
    end_menu()


def composition():
    pass


def entry_menu():
    display(ENTRY_MSG)
    user_input = get_menu_input({1, 2, 3}, MENU_INPUT_INCORRECT)
    if user_input == 1:
        changing_wav_menu()
    if user_input == 2:
        composition()
    if user_input == 3:
        end_menu()


def main_function():
    entry_menu()


main_function()

print('1111111232323')
