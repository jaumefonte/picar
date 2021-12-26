running = True

def PrintVersion():
    print("Version 0.0.1")
    
def PrintHelp():
    print("exit\t\tCloses program. \nversion\t\tPrints version number.")

try:    
    while(running):
        command = input('PICAR >')
        if(command == 'exit'):
            running = False
        elif(command == 'help'):
            PrintHelp()
        elif(command == 'version'):
            PrintVersion()
        else:
            print("'"+command +"' is not a valid command. Type 'help' for available commands.")
except KeyboardInterrupt:
    print("bye")


    
