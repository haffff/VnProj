# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
$import ch1
$import imgloc

#yes, these dont make sense, dont ask
define e = Character("Thomas the dank engine")
define g = Character("Taro")
define h = Character("Hikari")
define a = Character("Groostaj Alberto")
define aa = Character("Ania")
define hh = Character("Hania")
define s = Character("Janusz")
define j = Character("Justyna")
define sh = Character("Sekai")
define aaa = Character("Asia")
define nie = Character("???")

# The game starts here.
label ch1:
    jump start
        
label ch1e:
    jump start2
label ch2e:
            
    scene balck
    show mayewski
    image mayewski:
        "mayewski.jpg"
        yalign .7
    "Na razie to koniec"
    "A-ale będzie więcej"
    "Jak tylko ruszę swoją dupę do pracy, to jest"
    return
