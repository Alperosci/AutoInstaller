import os

def install_package(command):
    print(f"Installing with: {command}")
    os.system(command)

typeins = int(input("Debian based(1) or Arch based(2) > "))

print("""
What do you want to install (write the category if you want install all packages in that category):
-office-
1- libreoffice
2- GIMP
-web-
3- Firefox
4- Chromium
-communication-
5- Thunderbird
6- FileZilla
-multimedia-
7- VLC
8- Audacity
9- Kdenlive
14- OBS
-programming-
10- VScode (code)
11- Nvim
-gaming-
12- Steam
13- Retroarch
""")

prompt = input("> ")

pacman_packages = {
    "1": "sudo pacman -S libreoffice-fresh",
    "2": "sudo pacman -S gimp",
    "3": "sudo pacman -S firefox",
    "4": "sudo pacman -S chromium",
    "5": "sudo pacman -S thunderbird",
    "6": "sudo pacman -S filezilla",
    "7": "sudo pacman -S vlc",
    "8": "sudo pacman -S audacity",
    "9": "sudo pacman -S kdenlive",
    "10": "sudo pacman -S code",
    "11": "sudo pacman -S neovim",
    "12": "sudo pacman -S steam",
    "13": "sudo pacman -S retroarch",
    "14": "sudo pacman -S obs-studio",
    "office": "sudo pacman -S libreoffice-fresh gimp",
    "web": "sudo pacman -S firefox chromium",
    "communication": "sudo pacman -S thunderbird filezilla",
    "multimedia": "sudo pacman -S vlc audacity kdenlive obs-studio",
    "programming": "sudo pacman -S code neovim",
    "gaming": "sudo pacman -S steam retroarch"
}

apt_packages = {
    "1": "sudo apt install libreoffice-fresh",
    "2": "sudo apt install gimp",
    "3": "sudo apt install firefox",
    "4": "sudo apt install chromium",
    "5": "sudo apt install thunderbird",
    "6": "sudo apt install filezilla",
    "7": "sudo apt install vlc",
    "8": "sudo apt install audacity",
    "9": "sudo apt install kdenlive",
    "10": "sudo apt install code",
    "11": "sudo apt install neovim",
    "12": "sudo apt install steam",
    "13": "sudo apt install retroarch",
    "14": "sudo apt install obs-studio",
    "office": "sudo apt install libreoffice-fresh gimp",
    "web": "sudo apt install firefox chromium",
    "communication": "sudo apt install thunderbird filezilla",
    "multimedia": "sudo apt install vlc audacity kdenlive obs-studio",
    "programming": "sudo apt install code neovim",
    "gaming": "sudo apt install steam retroarch"
}

if typeins == 2:
    if prompt in pacman_packages:
        install_package(pacman_packages[prompt])
    else:
        print("Invalid selection, please choose a ID from the list.")
elif typeins == 1:
    if prompt in apt_packages:
        install_package(apt_packages[prompt])
    else:
        print("Invalid selection, please choose a ID from the list.")

