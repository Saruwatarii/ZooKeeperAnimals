'''
This program is made in order to help the zookeeper check on the animals and see if they are well.
It will take an input (command from the zoo staff) and show the animals on the monitor
The user will use the number as an index of the habitat to print its content.
'''

# Store the animals in string variables
camel = """
Switching on camera from habitat with camels...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \\
     |     \    _.-'             \\
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Yey, our little camel is sunbathing!"""

lion = """
Switching on camera from habitat with lions...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is croaking!"""

deer = """
Switching on camera from habitat with deers...
   /|       |\\
`__\\\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \\
     ;;`-'   `---__________-----.-.
     ;;;                         \_\\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Our 'Bambi' looks hungry. Let's go to feed it!"""

goose = """
Switching on camera from habitat with lovely goose...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \\
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \\
 <_  `     (  <`<            \              `-._\\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
This bird stares intently at you... (Maybe it's time to change the channel?)"""

bat = """
Switching on camera from habitat with bats...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\\\  W  //           <
       /             /~---~\             \\
      /_            |       |            _\\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\\
                ~-. /  \_/  \ .-~
                   V         V
It looks like this bat is fine."""

rabbit = """
Switching on camera from habitat with rabbits...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \\
\//\/      .- \\
 Y        /    Y 
 l       I     !
 ]\      _\    /"\\
(" ~----( ~   Y.  )
It seems there will be more rabbits soon!"""

# As long as the zoo staff does not write "exit", the program will continue to ask about the animals.
while True:
    habitat = input("Which habitat # do you need? ")
    # when the zoo staff input exit, the while loop will stop and jump to the next line after the while loop
    if habitat == "exit":
        break
    # Put the animals inside a list in order to index the animals.
    # Since input is original a str, int() have been used for converting it into number to use for indexing the list
    animals = [camel, lion, deer, goose, bat, rabbit]
    animal = animals[int(habitat)]
    # Printing out the animal on the monitor
    print(animal)


# Print out a goodbye message
print("See you!!")

