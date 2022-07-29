import pyfiglet
import termcolor

print('what would you like to print?')
msg = input()
print('what color?')
color_msg = input()
total_colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
if color_msg not in total_colors:
    color_msg = "red"
pmsg = pyfiglet.figlet_format(msg)
cmsg = termcolor.colored(pmsg, color=color_msg)
# print(pmsg)
print(cmsg)