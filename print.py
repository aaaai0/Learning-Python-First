# The command "print" write a message to the command line

print("You message text", end="")

# If you want to output several lines, then:
print("You")
print("message")
print("text", end="")

# else:
print("You \nmessage \ntext", end="")

# \n makes a line break 
# If you want print "\" you need write "\\"
print("You \\nmessage \\ntext", end="") #  \n will not work under these conditions

print("You \\message \\text", end="")

# end="" = \n but it only works at the end of the line and you need to write print again