"""
Write a switch statement that writes instructions for a driver at a stop light.
Assume a character variable "color" is defined:
if color is 'r' (for red), write the message "stop".
if color is 'g' (for green), write the message "go".
if color is any other value, write the message "caution".
"""
color = input("Enter a color: ")
match color:
    case 'r':
        print("stop")
    case 'g':
        print("go")
    case default:
        print("caution")
