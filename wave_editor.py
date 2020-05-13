#################
# File: wave_editor.py
# Writers: yuval grader, yuvalgrader
# Exercise: intro2cs2 ex6 2020
# Description: wav files edit and compose
#################
from wave_helper import *

# general messages for user
ENTRY_MENU_MSG = "WELCOME: press the number of the option: \n" \
                 "1.edit wav \n" \
                 "2.compose wav\n" \
                 "3.abort program "
WAV_FILENAME_REQUEST = "write down wav filename"
WRONG_WAVE_FILENAME = "wave file name was incorrect"
CHANGING_WAVE_MENU_MSG = "File edit menu:press the number of the option: \n" \
                         "1. reverse wav \n" \
                         "2. audio off \n" \
                         "3. increase wav speed \n" \
                         "4. decrease wav speed\n" \
                         "5. increase wav volume \n" \
                         "6. decrease_wav volume\n" \
                         "7. low path filter \n" \
                         "8. move to end menu"
MENU_INPUT_INCORRECT = "your menu input was incorrect"

MAX_VOLUME = 32767
MIN_VOLUME = -32768
SAMPLE_RATE_DEFAULT = 2000
INCREASE_VOL = 1.2
DECREASE_VOL = 1.2


# help functions
def display(msg):
    """that function display messages to the user"""
    print(msg)


def get_menu_input(input_option, input_msg, wrong_input_msg):
    """display the menu for the user and asks for input, if currect return
    input else, display informative message for user"""
    while True:
        display(input_msg)  # menu message
        user_input = input()
        if user_input in input_option:
            return int(user_input)  # correct input
        else:
            display(wrong_input_msg)  # wrong input message


def load_wave_file():
    """while file name is incorrect - asks for the user to input file name
        else, return the sample rate,audio data and file name."""
    while True:
        display(WAV_FILENAME_REQUEST)  # request the file name
        file_name = input()
        load_file = load_wave(file_name)  # using wave_helper to load file
        if load_file != -1:  # file exists
            sample_rate, audio_data = load_file
            return sample_rate, audio_data, file_name  # return parameters
        else:
            display(WRONG_WAVE_FILENAME)  # display wrong file name message


# edit functions
def reverse_wav(audio_data):
    audio_data.reverse()


def audio_off(audio_data):
    for unit in audio_data:
        if unit[0] != MIN_VOLUME:
            unit[0] = -unit[0]
        if unit[1] != MIN_VOLUME:
            unit[1] = -unit[1]


def increase_wav_speed(audio_data):
    fast_wav = []
    for unit_loc in range(len(audio_data)):
        if unit_loc % 2 == 0:
            fast_wav.append(audio_data[unit_loc])


def decrease_wav_speed(audio_data):
    slow_wav = audio_data[0]
    average_unit = [0, 0]
    for unit_loc in range(len(audio_data) - 1):
        average_unit[0] = int((audio_data[unit_loc][0] +
                               audio_data[unit_loc + 1][0]) / 2)
        average_unit[1] = int((audio_data[unit_loc][1] +
                               audio_data[unit_loc + 1][1]) / 2)
        slow_wav.append([average_unit])
        slow_wav.append(audio_data[unit_loc + 1])
    audio_data = slow_wav


def increase__wav_volume(audio_data):
    for unit in audio_data:
        unit[0] = int(INCREASE_VOL * unit[0])
        unit[1] = int(INCREASE_VOL * unit[1])
        if unit[0] < MAX_VOLUME:
            unit[0] = MAX_VOLUME
        if unit[1] < MAX_VOLUME:
            unit[1] = MAX_VOLUME


def decrease__wav_volume(audio_data):
    for unit in audio_data:
        unit[0] = int(unit[0] / DECREASE_VOL)
        unit[1] = int(unit[1] / DECREASE_VOL)
        if unit[0] > MIN_VOLUME:
            unit[0] = MIN_VOLUME
        if unit[1] > MIN_VOLUME:
            unit[1] = MIN_VOLUME


def low_path_filter(audio_data):
    pass


def call_edit_function(user_input, audio_data):
    if user_input == 1:
        reverse_wav(audio_data)
    elif user_input == 2:
        audio_off(audio_data)
    elif user_input == 3:
        increase_wav_speed(audio_data)
    elif user_input == 4:
        decrease_wav_speed(audio_data)
    elif user_input == 5:
        increase__wav_volume(audio_data)
    elif user_input == 6:
        decrease__wav_volume(audio_data)
    elif user_input == 7:
        low_path_filter()
    elif user_input == 8:
        return "8"


def composition():
    pass


# menu functions

def end_menu(file_name):
    pass


def changing_wav_menu():
    sample_rate, audio_data, file_name = load_wave_file()
    in_edit_mode = True
    while in_edit_mode:
        user_input = get_menu_input(
            {'1', '2', '3', '4', '5', '6', '7', '8'}
            , CHANGING_WAVE_MENU_MSG
            , MENU_INPUT_INCORRECT)
        if call_edit_function(user_input, audio_data) is "8":
            in_edit_mode = False
        else:  # save wave file and another iteration
            save_wave(sample_rate, audio_data, file_name)
    end_menu()


def entry_menu():
    user_input = get_menu_input({'1', '2', '3'}, ENTRY_MENU_MSG,
                                MENU_INPUT_INCORRECT)
    if user_input == 1:
        changing_wav_menu()
    if user_input == 2:
        composition()
    if user_input == 3:
        end_menu()


def main_function():
    entry_menu()


main_function()
