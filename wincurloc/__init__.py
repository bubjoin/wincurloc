import sys
import ctypes
import os

# Get a handle to the console output
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
hConsole = kernel32.GetStdHandle(-11) # -11 = STD_OUTPUT_HANDLE

# Typically, console Width: 80, Height: 25
W = 80
H = 25

###########################################
# How to Use
#
# import wincurloc as wcl
# wcl.hide_cursor()
# wcl.clear()
# wcl.locate_c(40, 13, 'C')
# wcl.locate(40,14)
# print('c', end='')
# wcl.locate_c(40, 14, ' ')
#
###########################################

def locate(x,y):
    # Make room in the lower 16bits for the x coordinate
    # the bitwise OR operation combines the shifted y value with the x coordinate
    # to pack both coordinates into a single 32-bit integer
    position = (y<<16)|x
    kernel32.SetConsoleCursorPosition(hConsole, position)

def locate_c(x, y, c):
    # Make room in the lower 16bits for the x coordinate
    # the bitwise OR operation combines the shifted y value with the x coordinate
    # to pack both coordinates into a single 32-bit integer
    position = (y<<16)|x
    kernel32.SetConsoleCursorPosition(hConsole, position)
    sys.stdout.write(c)
    sys.stdout.flush()

def hide_cursor():
    # Define a structure for CONSOLE_CURSOR_INFO
    class CONSOLE_CURSOR_INFO(ctypes.Structure):
        _fields_ = [("dwSize", ctypes.c_int),  # Size of the cursor
                    ("bVisible", ctypes.c_bool)]  # Visibility flag

    # Create an instance of the structure with the cursor hidden
    cursor_info = CONSOLE_CURSOR_INFO()
    kernel32.GetConsoleCursorInfo(hConsole, ctypes.byref(cursor_info))  # Get current settings
    cursor_info.bVisible = False  # Set visibility to False

    # Apply the updated cursor settings
    kernel32.SetConsoleCursorInfo(hConsole, ctypes.byref(cursor_info))

# CLS
def clear():
    os.system('cls' if os.name=='nt' else '')

# CF) ord('a') 97, ord(' ') 32, ord('A') 65, chr(91) [, chr(96) `
