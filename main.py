import pdfkit

print("               _     _                                  ")
print("              | |   | |                                 ")
print(" _ __ ___  ___| |__ | |_ ___                            ")
print("| '_ ` _ \/ __| '_ \| __/ _ \                           ")
print("| | | | | \__ \ |_) | ||  __/                           ")
print("|_| |_| |_|___/_.__/ \__\___|                           ")
print("                          _ _                           ")
print("                         | | |                          ")
print(" _ __ ___  __ _ ___ _   _| | |_ ___                     ")
print("| '__/ _ \/ _` / __| | | | | __/ __|                    ")
print("| | |  __/ (_| \__ \ |_| | | |_\__ \                    ")
print("|_|  \___|\__,_|___/\__,_|_|\__|___/                    ")
print("                                                        ")
print("______                    _                 _           ")
print("|  _  \                  | |               | |          ")
print("| | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ ")
print("| | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
print("| |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
print("|___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
print("                                                        ")

print("HEy PLease SElect FRom OPtions BElow")
print("1 : Download Specfic Reasult Using Seat Number")
print("2 : Download Using Starting And Ending Seat Number")

print("Please Choose Your Option ",end='')
menu_input = int(input())

if menu_input == 2:
    print("Please Double check before entering")
    print("Please Enter Starting SeatNumber : ",end='')
    starting_number = int(input())
    print("Please Enter Ending Seat Number : ",end='')
    ending_number = int(input())
    print("Now Seat Back Tight Let Me Do My Job")
    while starting_number <= ending_number:
        starting_number += 1
        save = starting_number
        save = f"{save}.pdf"
        pdfkit.from_url(f"https://msbte.org.in/BS19TEDIS/MBTESOMS19ESDIS/SeatNumber/21/{starting_number}Marksheet.html",save)
        print(f"Done {save} ")
elif menu_input == 1:
    print("Please Double check before entering")
    print("Enter your seat number : ",end='')
    specficseat = int(input())
    print("Now Seat Back Tight Let Me Do My Job")
    save = specficseat
    save = f"{save}.pdf"
    pdfkit.from_url(f"https://msbte.org.in/BS19TEDIS/MBTESOMS19ESDIS/SeatNumber/21/{specficseat}Marksheet.html",save)
else:
    print("Please Select Correct Option")


