import cfg
import colorama

from simple_term_menu import TerminalMenu

import time
import datetime
import random

import steam



def output_menu():
    mailsetup = False
    setup = False
    while True:
        mailsetup = False
        setup = False

        if not steam.logged_in:
            options = ["View Current Info", "Log in", "Change Password", "Change Username", "Settings", "Quit"]

        else:
            options = ["View Current Info", ("[Logged in]"), "Change Password", "Change Username", "Settings", "Quit"]

        terminalmenu = TerminalMenu(options)
        menu_entry_index = terminalmenu.show()

        #Print info
        if menu_entry_index == 0:
            print_info_append()


        if menu_entry_index == 1:
            if not steam.logged_in:
                print_out("Attempting to log in to steam..", colorama.Fore.YELLOW)
                steam.login()

            else:
                 print_out("You are already logged in.", colorama.Fore.YELLOW)

        #Change password
        if menu_entry_index == 2:
            print_out("New password?:", colorama.Fore.RED)
            new_pass = input()

            if not steam.logged_in:
                print_out("Not logged in, logging in..", colorama.Fore.GREEN)
                steam.login()

            steam.setSteamPassword(new_pass)

        #Change username
        if menu_entry_index == 3:
            print_out("New Profile Name?:", colorama.Fore.YELLOW)
            new_username = input()

            if not steam.logged_in:
                print_out("Not logged in, logging in..", colorama.Fore.GREEN)
                steam.login()

            steam.setSteamProfileName(new_username)

        #Lengthy settings
        if menu_entry_index == 4:
            settings2 = ["Rerun Setup", "Set email settings", "Back"]
            terminalmenu2 = TerminalMenu(settings2)
            menu_entry_index2 = terminalmenu2.show()

            if menu_entry_index2 == 0:
                print_out("What is your steam username? (Enter to skip)", colorama.Fore.CYAN)
                username = input()
                if username == "":
                    username = cfg.loadEncryptedCFG()[0]

                print_out("What is your steam password? (Enter to skip)", colorama.Fore.CYAN)
                password = input()
                if password == "":
                    password = cfg.loadEncryptedCFG()[1]

                
                print_out("Do you want to automatically use mail codes?", colorama.Fore.CYAN)
                aggjf = ["y", "n"]
                FGJfd = TerminalMenu(aggjf)
                yesorno = FGJfd.show()

                if yesorno == 0:
                    useemail = True

                    print_out("What is your email? (Enter to skip)", colorama.Fore.CYAN)
                    emailuser = input()
                    if emailuser == "":
                        emailuser = cfg.loadEncryptedCFG()[2]


                    print_out("What is your email password? (Enter to skip)", colorama.Fore.CYAN)
                    emailpass = input()
                    if emailpass == "":
                        emailpass = cfg.loadEncryptedCFG()[3]


                    print_out("What is your email provider?", colorama.Fore.CYAN)
                    #username = input()
                    #if username == "":
                    #    username = cfg.loadEncryptedCFG()[3]

                    aaaaa = ["gmail", "protonmail"]
                    bbbbb = TerminalMenu(aaaaa)
                    asdasd = bbbbb.show()

                    if asdasd == 0:
                        emailprov = "gmail"

                    elif asdasd == 1:
                        emailprov = "protonmail"

                    cfg.saveEncryptedCFG(username, password, emailuser, emailpass, emailprov, True)

                else:
                    useemail = False

                    cfg.saveEncryptedCFG(username, password)

                

                print_out("Ran setup, restart", colorama.Fore.CYAN)

            if menu_entry_index2 == 1:
                settings3 = ["Set email provider and email credentials", "Toggle manual / automatic mail", "Back"]
                terminalmenu3 = TerminalMenu(settings3)
                menu_entry_index3 = terminalmenu3.show()

                if menu_entry_index3 == 0:
                    print_out("What is your email provider? (Enter to skip)", colorama.Fore.CYAN)
                    emailprov = input()
                    if emailprov == "":
                        emailprov = cfg.loadEncryptedCFG()[4]


                    print_out("What is your email username? (Enter to skip)", colorama.Fore.CYAN)
                    emailusr = input()
                    if emailusr == "":
                        emailusr = cfg.loadEncryptedCFG()[2]


                    print_out("What is your email password? (Enter to skip)", colorama.Fore.CYAN)
                    emailpass = input()
                    if emailpass == "":
                        emailpass = cfg.loadEncryptedCFG()[3]

                    usrname = cfg.loadEncryptedCFG()[0]
                    passwrd = cfg.loadEncryptedCFG()[1]

                    cfg.saveEncryptedCFG(usrname, passwrd, emailusr, emailpass, emailprov, True)

                    print_out("Set email settings.", colorama.Fore.CYAN)

                if menu_entry_index3 == 1:
                    print_out(f"Automatically using email: {cfg.loadEncryptedCFG()[5]}", colorama.Fore.CYAN)
                    print_out("Automatically use email?:", colorama.Fore.CYAN)

                    yn = ["y", "n"]
                    terminalmenu4 = TerminalMenu(yn)
                    menu_entry_index4 = terminalmenu4.show()

                    if menu_entry_index4 == 0:
                        cfg.saveEncryptedCFG(cfg.loadEncryptedCFG()[0], cfg.loadEncryptedCFG()[1], cfg.loadEncryptedCFG()[2], cfg.loadEncryptedCFG()[3], cfg.loadEncryptedCFG()[4], True)

                    if menu_entry_index4 == 1:
                        cfg.saveEncryptedCFG(cfg.loadEncryptedCFG()[0], cfg.loadEncryptedCFG()[1], cfg.loadEncryptedCFG()[2], cfg.loadEncryptedCFG()[3], cfg.loadEncryptedCFG()[4], False)

        #Quitter boi
        if menu_entry_index == 5:
            quit(105)

        print(" ")
        print(" ")

        time.sleep(2)

        


def print_out(out, color):


    print("")
    print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + color, out, colorama.Style.RESET_ALL)


def print_info_append():
    username, password, email, emailpass, mailprovider, usingemail = cfg.loadEncryptedCFG()
    print("")
    print("")
    if usingemail:
        print(colorama.Fore.CYAN, "  username: ", username, colorama.Fore.GREEN, "password: ", password, colorama.Fore.YELLOW, "mailp: ", mailprovider, colorama.Fore.MAGENTA, "email: ", email, colorama.Fore.RED, "email password: ", emailpass, colorama.Style.RESET_ALL, end="\r")

    else:
        print(colorama.Fore.CYAN, "  username: ", username, colorama.Fore.GREEN, "password: ", password)