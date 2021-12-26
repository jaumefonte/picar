import FrontLights

def PrintVersion():
    print("Version 0.0.1")
    
def PrintHelp():
    print("exit\t\tCloses program. \nversion\t\tPrints version number. \nlight_red\tTint front lights of the robot red.\nlight_green\tTint front lights of the robot green.")

running = True
FrontLights.Setup()
FrontLights.Both_on()
try:    
    while(running):
        command = input('PICAR >')
        if(command == 'exit'):
            running = False
        elif(command == 'help'):
            PrintHelp()
        elif(command == 'version'):
            PrintVersion()
        elif(command == 'light_red'):
            FrontLights.ColorRed()
        elif(command == 'light_green'):
            FrontLights.ColorGreen()
        else:
            print("'"+command +"' is not a valid command. Type 'help' for available commands.")
except KeyboardInterrupt:
    print("bye")
    
FrontLights.Both_off()
print("Press 'Enter' to quit PICAR")
input()

    
