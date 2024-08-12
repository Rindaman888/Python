print('''    .:'    Dragon                        `:.
  ::'       Art by                       `::
 :: :.    Ronald Allan Stanions         .: ::
  `:. `:.             .             .:'  .:'
   `::. `::           !           ::' .::'
       `::.`::.    .' ! `.    .::'.::'
         `:.  `::::'':!:``::::'   ::'
         :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
       ::: `H TH::.  `!'  .::HT H' :::
       ::..  `THHH:`:   :':HHHT'  ..::
       `::      `T: `. .' :T'      ::'
         `:. .   :         :   . .:'
           `::'               `::'
             :'  .`.  .  .'.  `:
             :' ::.       .:: `:
             :' `:::     :::' `:
              `.  ``     ''  .'
               :`...........':
               ` :`.     .': '
                `:  `"""'  :'
 ''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
way = input("Left or right? : ").lower()

if way == 'left':
  leftway = input("swim or wait? : ").lower()
  if leftway == 'wait':
    door = input("Which door? Red/Yellow/Blue : ").lower()
    if door == 'red':
      print("Burned by fire. Game Over.")
    elif door == 'yellow':
      print("You Win!")
    elif door == 'blue':
      print("Eaten by beasts. Game Over.")
    else:
      print("Game Over")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")
