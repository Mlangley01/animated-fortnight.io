import sys
import time
import random
bad_ends =(r""" 
                                           .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |   |:::::||              |////}                `-. \
                |   \:::::||             //'///                    `.\
                |    |::::||            //  ||'                      `|
                /    |::://        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ || You Have met
             /`  |   |'' ||           \   |||    with a Ghostly Demise !!!
           /`    \   |   ||            |  /||   MWAAAAAHHHH!!!!!       
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              ||
 ||||  /                    /              || 
 `\\` /`                    |              || 
     |`                     \              ||  
    /               |^         |           ||  
  /`                 |\         \          ||  
/`                    |\        |          ||    
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`
         """)
             
note1= (r""" 
    ______________________________
  / \                             \.
 |   |                            |.
  \_ |  My name is Jack Daniels   |.
     |                            |.
     |  I am an old friend of     |.
     |  of your parents.          |.
     |                            |.
     |  I am trapped at the       |.
     |  enclosed address, I need  |.
     |  your help to get out.     |.
     |  Please, come get me       |.
     |  before midnight tonight.  |.
     |                            |.
     |  You're my only hope!      |.
     |                            |.
     |   _________________________|___
     |  /                            /.
     \_/____________________________/.
""")
note2=(r"""
    ______________________________
  / \                             \.
 |   |                            |.
  \_ |                            |.
     |     Cheers for that!       |.
     |                            |.
     |    I've been stuck here    |.
     |     for 20 years and I     |.
     |   wasn't myself anymore.   |.
     |                            |.
     |   I hope the contents of   |.
     |    this pouch will help    |.
     |   make up for my actions   |.
     |                            |.
     |   -Jack                    |.
     |   _________________________|___
     |  /                            /.
     \_/____________________________/.
""")
sharps =(r"""
                                
 __,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
This knife looks pretty handy 
I wonder what else I'll find in this creepy house?.
""")

sharps2 =(r"""
                                
 __,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
I wonder what else I could of found in that creepy house?.
""")

sharps1 =(r"""
__,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
I knew this would come in handy!
""")
phone_pic =(r"""
                       
     __.-==========-.__    
   .'//   .-"  "-.   \\`,  
  : :'  .' ______ `.  `: : 
 /: /  /  |. $$ .|  \  \ :\ 
 : :  ;    T.:;,P    :  ; ;
   | :      `  '      ; | |
 j | :.--------------.: | |
 ; ; |  CALL WITHELD  | : :
 ; ; |    #######     | : :
 | | |                | | |
 | | |                | | |
 : : |                | ; ;
 : : :________________: ; ;
  ; ;__    _...._    __: : 
  | ;  "-./ ,--, \,-"  : | 
  | '._   \ ;  : /   _.' | 
  :  __`-. `."",' .-'__  ; 
  ; `.__> `.J__L.' <__.' :  
  ; .--._   .--.   _.--, :  
  | `.__.' `.__.' `.__.' |  
  | .--._   .--.   _.--, |  
  | `.__.' `.__.' `.__.' |  
  | .--._   .--.   _.--, |  
  ; `.__.' `.__.' `.__.' :  
  : .--._   .--.   _.--, ; 
  ; `.__.' `.__.' `.__.' : 
  ;                      : 
  '--..__          __..--' 
         ----------
""")
key = (r""")         
          .---.
         /    |\________________
        | ()  | ________   _   _)
         \    |/        | | | |
          `---'         "-" |_|
""")
car =(r"""

              ____----------- _____
\~~~~~~~~~~/~_--~~~------~~~~~     \
 `---`\  _-~      |                   \
   _-~  <_         |                     \[]
 / ___     ~~--[""] |      ________-------'_
> /~` \    |-.   `\~~.~~~~~                _ ~ - _
 ~|    ||\&|        |    ~  ._                ~ _   ~ ._ _
   \`_//|_%\        |          ~  _.              ~-_  / \
          `--__     |    _-____  / \                ~-_\_/.
               ~--_ /  ,/ -~-_ \ \_ /         _______---~/
                   ~~-/._<   \ \`~~~~~~~~~~~~~     ##--~/
                         \ *  ) |`------##---~~~~-~  ) )
                          \-_/_/                   ~~/



""")

rundown_house =(r"""


                                =====        ___..--'  .`.
                                |   |__...--'     -  .` `.`.
                           ___..|   |_      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |           |`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |           |        |              |                       |
    |           |    |   |              |                       |
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _|  |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |  |  |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |  |- |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._        ^\'' /^   ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'    \^/   --     .   ''\|/¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . '\|/     `--._ ---------`--._   -- . :''\|/¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
          :' \|/    `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._\|/
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._

""")

hallway =(r"""
 _____________________________________________
|     Hmmm Looks safe                          |
|                Enough!!!!                    |
|                                              |
|                                              |
|.'.'|.'.'.|                         |.'.'.'.'.|
|.'.'|.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'|.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'|.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'|.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,','|,',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.|'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.|.'. |---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.|.'. |===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.|'., |%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.|,',         /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','         /%%%%%%%%%%%\        ','.'.'.|
|.'.','          /%%%%%%%%%%%%%\         ','.'.|
|.','           /%%%%%%%%%%%%%%%\          ','.|
|;____________ /%%%%%&&&&&&%%%%%%\____________;|

""")

hallway2 =(r"""
 _____________________________________________
|                                              |
|      Which way to go                         |
|             They all look Creepy             |
|                                              |
|.'.'|.'.'.|                         |.'.'.'.'.|
|.'.'|.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'|.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'|.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'|.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,','|,',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.|'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.|.'. |---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.|.'. |===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.|'., |%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.|,',         /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','         /%%%%%%%%%%%\        ','.'.'.|
|.'.','          /%%%%%%%%%%%%%\         ','.'.|
|.','           /%%%%%%%%%%%%%%%\          ','.|
|;____________ /%%%%%&&&&&&%%%%%%\____________;|

""")

police =(r"""
                      ______
                   ,-~   _  ^^~-.,               ________
                 ,^        -,____ ^,        __..(        )__
                /           (____)  |      (               /
               ;  .---._    | | || _|     (    I AM THE    )
               | |      ~-.,\ | |!/ |     /_     LAW!...  _\ 
               ( |    ~<-.,_^\|_7^ ,|     _//_    ___  _\
               | |      ", 77>   (T/|   _/'   \/\/   \/
               |  \_      )/<,/^\)i(|
               (    ^~-,  |________||
               ^!,_    / /, ,'^~^',!!_,..---.
                \_ "-./ /   (-~^~-))' =,__,..>-,
                  ^-,__/#w,_  '^' /~-,_/^\      )
               /\  ( <_    ^~~--T^ ~=, \  \_,-=~^\
  .-==,    _,=^_,.-"_  ^~*.(_  /_)    \ \,=\      )
 /-~;  \,-~ .-~  _,/ \    ___[8]_      \ T_),--~^^)
   _/   \,,..==~^_,.=,\   _.-~O   ~     \_\_\_,.-=}
 ,{       _,.-<~^\  \ \\      ()  .=~^^~=. \_\_,./
,{ ^T^ _ /  \  \  \  \ \)    [|   \oDREDD >
  ^T~ ^ { \  \ _\.-|=-T~\\    () ()\<||>,' )
   +     \ |=~T  !       Y    [|()  \ ,'  / 

""")
flash =(r"""

         .                      .
         .                      ;
         :                  - --+- -
         !           .          !
         |        .             .
         |_         +
      ,  | `.
--- --+-<#>-+- ---  --  -
      `._|_,'
         T
         |
         !
         :         . : 
         .       *
             _,._
           ,'   ,`-.
          /     _____,
         (  ,-,-` ). `-._ __
          \)\,'     `\  /'  `\
           ` (, ,  /  \ \     \
               `,_/`, /\,`-.__/`.
                  | ` /    /    `-._
                  `-/'    /         `-.
           _______,-/_   /'             \
     ---'`|       |`  ),' `---.  ,       |
      \..-`--..___|_,/          /       /
   |             |    |`,-,...,/      ,'     
| / '''''''/|    \    | |_|   /     ,' __  r-'',
|/        / |     |___|/  |, /  __ /-''  `'`)  |  
/________/      _,-'  ||__\ /,-' /     _,.--|  (
|        |  .-'       )   `(_   / _,.-'   ,-' _,/
|        |   `-------'       `--''        `'''


""")
box =(r"""
             _,._
           ,'   ,`-.
          /     _____,
         (  ,-,-` ). `-._ __
          \)\,'     `\  /'  `\
   |\      ` (, ,  /  \ \     \
   \ \         `,_/`, /\,`-.__/`.
    \ \            | ` /    /    `-._
     \\\           `-/'    /         `-.
      \\`/ _______,-/_   /'             \
     ---'`|       |`  ),' `---.  ,       |
      \..-`--..___|_,/          /       /
                 |    |`,-,...,/      ,'     
                 \    | |_|   /     ,' __  r-'',
                  |___|/  |, /  __ /-''  `'`)  |  
               _,-'   ||__\ /,-' /     _,.--|  (
            .-'       )   `(_   / _,.-'  ,-' _,/
             `-------'       `--''       `'''

""")

phone_pic1 =(r"""
 __i
|---|    
|[_]|    
|:::|    
|:::|    
`\   \   
  \_=_\ 

""")


floater =(r"""
                  .-""-.
      (          /-.{}  \
    (            | _\__.|
                 \/^)^ \/
                  \ =  /        )
              .---./`--`\.--._   )
             /     `;--'`     \
            ;        /`       ;
            |       |*        |
            /   |   |     |    \
            |    \  |*    /    |
            \_   |\_|____/|  __/       \     \
              \__//======\\__/
              / //        \\ \
              -//          \\       |  
              //      |     \\     |
              ---------------->

             ^   ^    ^    ^   ^  ---------
----------
           ------

==============================================          
                                                  """)



spoilsport =(r"""

           _..--""---.
          /           ".
          `            l
          |'._  ,._ l/"\
          |  _J<__/.v._/
           \( ,~._,,,,-)
            `-\' \`,,j|
               \_,____J
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'\
     \$          \`-(               /&\\\
     ||       _  /`-(               l|///__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  \
/"\.-"_.-"  | |                 /          \   \
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
  \\\       |-\               \j ..          L,,'. `/
 __\\\     ( .-\           .--'    ``--../..'      '-..
   `'''`----`\\\\ .....--'''
              \\\\                           -


""")

old_photo =(r"""

        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~

""")
splash=(r"""

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo;..,;;,';cll::llllloxxxxxxxxxxxxxxxxxxxxdc.                                ;xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdooodxxxxxxxxoclxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdc;,'..                            .cxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo;,,'',;oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;                        ...'cxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc'...;ldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl.                      'oxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkl....cxxxxxxxxxxxxxxxxxxxxxxxxkxxxxxxxxxxxxxxxxxxxxxxxxxxxxkl.    .'.;,        ..   :xxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkxxxxxxkx;....;dxxxxxxxxxxxkxxxxxxxkkxo:,,coxxkkkxxxxxxxxxxxxxxxxxxxko.   .ll,od'     .clc, .okxxxxxxxxxxxxxxkkxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxkxkxol:.. .lxxxxxxxkkxxxxxxxxxoc::,.     ...',lxxxxxxxxxxxxxxxxxxxkd.   ,xl;ox,     ,dlo: ,xkxxxxxxxxxxxxxxxxxxxxxxxxx
kkkkkkkkkkkkkkkkkkkxxxkxddkxxxkxxkd:...  .;dxxxxkkkkkkxxkkxxko.               .dkxxxxkxxkxxxxxxxkxkd'   'dc,ll.     'c;l;.:kxkxxkxxxxxxxxxxxxxxxxxxxxx
kkkkkkkkkkkkkkkkkkkkkkkl,;oxkkkxxoc.    .lkxxkkkkkkkkkkkkkkxkc.               .lkxkkkkkkkkkkkkkkkkkd'   ,xocxo.     cl:l,.lkxkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkd:''';;;;,'..     .lkxkkkkkkkkkkkkkkkkx,                 :kkkkkkkkkkkkkkkkkkkx,   ,xolxl.    .lood''dkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkko,''...... ... .,;,:dkkkkkkkkkkkkkkkkko.                 'dkkkkkkkkkkkkkkkkkkx,   .;,';'      ',;;.:kkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkko'........'lxdldkkkxxkkkkkkkkkkkkkkkkx;                  .lkkkkkkkkkkkkkkkkkkx;                   .lkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkd,...:odl:dkkkkkkkkkkkkkkkkkkkkkkkkkkc.                   ,xkkkkkkkkkkkkkkkkkx;                   .dkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkx:.,dkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxo.                    .lkd:cdkkkkkkkkkkkkx;   .:;cl.     ',.  ,xkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkdlxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd,                      ,d;  .okkkkkkkkkkkx;   ;xclkc    .lol, ckkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx;                        ,.   .:xkkkkkkkkkx;   :xclxc    'olo;.lo;',:codxkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx:                                'okkkkkkkkx,   ;d::o;    .ccl, .       ..;dkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxkx:                                  .;dkkkkkkx,   cklok:    .odd,            ckkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdxxxkkkkkkkkdoxd,                                     .;dkkkkx'   cxldk;    .odd,            'xkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxkkkxdoodddxkxkkxxocc'                                   .    .;oxOx'   .'.''.     .,,.            .ckkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxlokkkdollxocoxloddddl:;;;;,.                            .. .      .:c.                               'xkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkxdxkkd:cdxxoccoxo;lxlcloooollolcc:.  .'.'.    ,'''.                                                         ckkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkxdodkxl:ldxloooxdloolccllodolllcc:. .l:'l;   'o;,c:.                                                        .oOkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkxoloollccclxkooodolcclcldxol:;co:. .c;.:;.  .c,;lc'                                                         ,xkkkkkkkkkkkkkk
kkOkkkkkkkkkkkkOkkkkkkkkkkkkxo::c::loxxl:ldxlclc;lxkdcc:cc;' .,,';,.  .::col,                                                          ;kkkkkkkkkkkkkk
OOOOOOOOOOkkkOOOkxddxxxxkkxdddlolcllldxoc:odlll;;ldol:::;;:;..:;;l;.  .oolxk:                                                           :kOkkOOkkOOOOO
OOOOOOOOOOOOOOOOkxdolooooxxddddccclocldoc:ccclc;:lodoll:',cc. ,,';.   .cc;cl'                                                            ;xOkOOkOOOOOO
OOOOOOOOOOOOOOOOOxddollccldooxxclc:clc::l:,;clc;:oxdolc;.,lc.                                                                             'dOkOOOOOOOO
OOOOOOOOOOOOOOOkkxoolccccldlcolclccdo::::,;clcc::olcc:lc';l:.    ..                                                                    .,:lxOOOOOOOOOO
OOOOOOOOOOOOOOOkkxdolllc::lc:ol:ooloool:,.co::olc:;,,;:,':l;.   .;.'.                                                                 .dOOOOOOOOOOOOOO
OOOOOOOOOOOOkxddddolcodoc;;:cxd:ol:cloc,.':clkx;',;;;;;,,'.,.   ,,.,,                                                                 ,xOOOOOOOOOOOOOO
OOOOOOOOOOOOOkdollolloolccc,,cc::;clllc'.,,:dxc',oolcc:,'..c,  .;;.,;.                                                          ..    ;kOOOOOOOOOOOOOO
OOOOOOOOOOOOOkkxxOOkkxl:::::;,,,:c:ccll,,:,:oo;'coolcc:. .:c'   ':,:c.         ,c. ,;.                                ..       :ooc.  :OOOOOOOOOOOOOOO
OOOOOOOOOOOOOkOkkxxxddolll:;;'..;cccc;'.;l;,lo:coc;;;:'..'::.   .;;::.       .ckk,.:dxc.                             'llc.    'kddx,  cOOOOOOOOOOOOOOO
OOOOOOOOOOOOkxdxdoodddollll::;...;,',,..;:,'l:;loddo:;',cdxxc.  .....       .cdxd'.lxooc.                           .dxlko.   'dlld' .lOOOOOOOOOOOOOOO
OOOOOOOOOOkxdooooc:cc:;;;,;lol:'.''':,.';:;,c;;clodxl..,coll:.              ,llol..ldooo'                           :Odlkk,   ,xoox, .oOOOOOOOOOOOOOOO
OOOOOOOOOOkxollccc;::::::clooc:c:..;;,c:,;;,':o:. ... .'''';,.             .;olll..cdodo'                          .;l::dd'   ;kdxk, .dOOOOOOOOOOOOOOO
""")
gold =(r"""
   _____
  /   \\\
 |__%___|
 / : :   \
( GOLD    )
 `-------'

""")
gate =(r"""

                                {} {}
                         !  !  ! II II !  !  !
                      !  I__I__I_II II_I__I__I  !
                      I_/|__|__|_|| ||_|__|__|\_I
                   ! /|_/|  |  | || || |  |  |\_|\ !       
       .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
      /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \
      \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
       }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
      {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
_!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
_I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
-|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
 |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
 |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
 |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
 |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  | 
_|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
-|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
-|--|--|| |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  | 
~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~

""")

bangbang = (r"""
#                                ^
  #                              ^
 #                               @
#####    ##   #    #  ####  <<<<@@@>>>>>
#    #  #  #  ##   # #    #      @
#####  #    # # #  # #           ^
#    # ###### #  # # #  ###      ^
#    # #    # #   ## #    # 
#####  #    # #    #  ####  
                            
                                        
            #####    ##   #    #  ####  
            #    #  #  #  ##   # #    # 
            #####  #    # # #  # #      
            #    # ###### #  # # #  ### 
            #    # #    # #   ## #    # 
            #####  #    # #    #  ####  
                                        
                                                    
                        #####    ##   #    #  ####  
                        #    #  #  #  ##   # #    # 
                        #####  #    # # #  # #      
                        #    # ###### #  # # #  ### 
                        #    # #    # #   ## #    # 
                        #####  #    # #    #  ####  
                                                    

""")

dimkit =(r"""
_____________________________________________________
____________________________________________________\\
|.-------.-------.|_.----._.----._|.-------.-------.\\\
|]       |       [|      /|\      |]       |       [ \\\
||       |       ||     .'|'.     ||       |       |  |\\
||       |       ||    .' | '.    ||       |       |  |\\\
||     (O|O)     ||   .'  |  '.   ||     (O|O)     |  | \\\
||       |       ||  .'===|==='.  ||       |       | O|  |\\
||       |       ||=='    |    '==||       |       |  |  |\\\
|]       |       [|  )    |    (  |]       |       [  |O | \\\
||_______|_______||"" ____|_____""||_______|_______|  |  |  |\\
'-----------------'_______________'----------------'  |  |  |\\\
|.--------.  |    '---------------'  (o)______)(0)  \ |  |  | \\\
||        |::|_________________________________())___\|  | O|  \\\______
||        |::|-----______*!*______-------------))( .'.\  |  |   | _____ |
||________|::|  _ /       '       \|  _        _  (__.'\ |  |O  ||     ||
|____________| _  \_______________/|    _           (_.'\|  |   ||  _  ||
 __________________________________|________      _  (___\  |   ||     ||
||.-----.|.------.|.-.-.--.--.-.-.||.-----.||\   _        \ |   ||     ||
||| === ||| ==== ||| | |  |  | | |||| === ||| \     _      \|   ||    _||
||'-----'|'------'|'-'-'--'--'-'-'||'-----'||. \          _ \   ||     ||
||.-----.|.------.|.------.------.||.-----.|| `|\       _    \  || _   ||
||| === |||      |||      |      |||| === |||\ | \  _         \ ||_____||
||'-----'|]      ||]      |      [||'-----'|| \|. \        _   \|_______|
||.-----.||    (O|||    (O|O)    |||.-----.||  | `|\                   ||
||| === |||      |||      |      |||| === |||  |\ | \__________________||
|||     ||]      ||]      |      [|||     ||| O| \|. |  _____________  ||
||'-----'||______|||______|______|||'-----'||  |  | `| |             | ||
||_______|________|_______________||_______||  |O |\ | |   _         | ||
''-----------------------------------------' \ |  | \| |          _  | ||
   ____                 _______               \|  |  | |       _     | ||
           _________                  ______   \  |O | |             | ||
                                                \ |  | |   _      _  | ||
                                _________        \|  | |             | ||
      ___________        __                       \  | | _        _  | ||
    __                              _________      \ | |_____________| ||
               ___________                          \|_________________||

""")

loft_step =(r"""
          
           ______________________          
==========/_____________________/==================
          {}



         @\_______/@
         |XXXXXXXX |
         |X||    X |
         |X||    X |
         |XXXXXXXX |         
         |X||    X |            
         |X||   .X |
         |X||.  .X |            
        |%XXXXXXXX%||
        |X||  . . X||
        |X||  .   X||
        |X|| .    X||.                            
        |X||.     X||
       |XXXXXXXXXXXX|
       |XXXXXXXXXXXX||         .                 .  
       |XX||       X||                        .   
       |XX||       X||                   .          
       |XX||       X||              .          .        .
       |XX||====== X||======================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
ktab=(r"""

          _________________________________________________
        .' ____________________________________________ _.'|
      .' .'____________________________________________|_| |
    .' .'.'                                           .'.' |
  .' .'.'              <=====//=#=#                 .'.'  .'
 __.'.'___________________________________________.'.'  .'|
|  |'______.-.__________________________.-.____ __.'  .'| |
|  |                                           |  | .'  | |
|__|______________________________________   __|__|' |  | |
  |  | |   | |  |                            |  | |__|  | |
  |  | |   | |  |                            |  | | . . | |
  |  | |   |_|. '                            |  | |'.'__|.'
  |  | | ____________________________________|  | |'.'
  |  | |_____________________________________|  | |'
  |  | |                                     |  | |
  |__|.'                                     |__|.'

""")

gimage =(r"""

                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |       (   (      .',
              \  \  __ ,-` `  ,  , `/ |        Y     (   /_L\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`

""")

gimage1 = (r"""

                        _,--~~~,
                       .'        `.
                       |           ;
                       |           :
                      /_,-==/     .'
                    /'`\*  ;      :      
                  :'    `-        :      
                  `~*,'     .     :      
                     :__.,._  `;  :      
                     `//    )  '  `,     
                         |\-/  '     )     
                         :'           \ _
                          `~---,-~    `,)
          ___                   \     /~`\
    /---__ `;~~~-------------~~~(| _-'    `,
  ---, ' \`-._____     _______.---'         \
 /--- `~~-`,      ~~~~~~                     `,
/----      )                                   \
/----.  __ /                                    `-
 /----'` -~____--------,.___                    ```\_
                          \
""")

face =(r"""

                                       ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \    A very scary Face Indeed!!!             
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'

""")

sunrise =(r"""

        .       .        .
         .      .       .        .'               .--.
 '.       .     .      .       .'       ________.'_.'_____.--.___
   '.      .    .     .      .'        ()_() ooo   ~/   -.|      "-._
     '.     .   .    .     .'          ((((<____   |      |  ____  = )
       '.    .  .   .    .'       .-'  (__)/ () \___\_____|_/ () \__/)
.        '   ______    .'      .-'    ___'.'.__.'_________'.'.__.'____
 '-.      .-~      ~-.      .-'      /
    '-. .'            '. .-'      __/
_      .                .      _./
 '-._ .                  . _.-'  |
      :                  :      /
  .-' .                  . '- .'
-'     .                . . .'
    .'  '.            .' _.'
  .'  .'  '__________'.-'
~~~~~~~~~~~~~~~~~~~~~/
~~  ~~~    ~~~ ~~ ~ /
  ~~   ~~~~  ~~~~ ~/

""")

mutley =(r"""

             
             ,       /$$$$$$e.
              '.    /$$.$'$$$$$.
                \   |$/$$$$$$$$$\
           ""--._|_ |/$'$$$$$$\"*'
     .ee.   .-"   _""*$$$$$$)"-'
    /$$$$ee/ A \|'-)""  \"**'
    |$$$$$/|/ '-e$*     _\ \"-.
    /$$$$$|"   $$.-   ."\'\ \  '.
    |$$$$$|\ (_$/  / /.-"\ \ \,  \
     \$A/\|"-_"' -"  '\   \ |/    \
         /-"" "        \--| /      \
      .-====-          | ||        \
   .-"                  |_|/         \
 .'     _.sjw.          |/ |        . |
/   .e$$$$$$$$)         | /         | \
| .e$$$$$$$$$$/     .-._/ |         |  \
\ \$$***$$/  )      \  /  |         |  |
 \ '*(  \/ ."__      \/ ,"|        /   |
 /"-._)    ""  \   .-"." /         /   |
/  -"/__.   --./--".-"   |        /    |
|      /../\  )--""      |.  ,   /     /
\     ""/ | "-" ,        /\ /||\/      /
 "-.__.-" |     |         |\|  /-,    /
          /     |         \      )    |    /|
          |     |,        \ . --"|    /   / /
          /     \\         '.'-."     /  / /
          ||     \\          ""      / .' /-
          |\ .     \        .       /."  ".'
          |/\ \ .   \  .    /    .  / _.-'
          ' \ \ |\,    |,  /|/| /|,/__,7
             \|\|\\\   |\|/ | |/ "V
            .-',' \ '-.\ V  / V
            |-. "-.\  |"   /_..--.
            ( /".     |       .--)
             V       _A     "-.  \
              "---`""  ".     ) ."
                         '-.." ,\

""")

tchest=(r"""

           __________
          /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       %%%%

""")

scream =(r"""

#     # ####### #       ######  ### ### ### ### 
#     # #       #       #     # ### ### ### ### 
#     # #       #       #     # ### ### ### ### 
####### #####   #       ######   #   #   #   #  
#     # #       #       #                       
#     # #       #       #       ### ### ### ### 
#     # ####### ####### #       ### ### ### ### 


""")
good_ends =("""
You scramble away from the ghost as it makes a swipe for you and desperately search the decaying body for clues.\nThe box's lid is open and there is an indent shaped like a knife on the inside.\nYou pull out the knife and in a last-ditch attempt place it down into the box.\nA perfect fit!.
A flash of light blinds you for a moment and the ghost screeches behind you.\nYou squeeze your eyes shut, bracing yourself for impact,
but nothing happens.\n""")

good_ends2=("""Where the horrifying apparition once was is now a man floating a couple inches off the ground holding the box.\n He smiles at you and, in another flash of light, vanishes. You blink and look around, not sure of what to do. Where the box had been in the hands of the body is now a pouch with a note tied to it.""")
# add art of floating man +brilliant flash +pouch of gold and a loft hatch 
# """)

good_ends3=("""You open the pouch and find a small pile of gold coins.\nYou're unsure of the value, but you're sure it's probably quite high.\nYou make your way to the front door.\nSure enough the loft key fits the lock here too.\nYou get into your car and drive home as the sun begins to rise.""")
good_ends4=("""Nobody is going to believe you about any of this.\nCongratulations! You beat the game and got the Good Ending!""")


def print_slow(str):
    for char in str:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        
def game():
    print_slow(f"{name}, Would you like to play a game? (Yes/No)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "yes" in answer or answer == "y":
            print_slow("Welcome to The House That Jack Built\n")
            phone()  
            break
        
        elif answer =="no" or answer == "n":
            print_slow("Okay maybe another Time\n")
            print(spoilsport)
            start_over()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\nUsing any of these words:yes,y,no,n")  

def phone():
        print_slow(f"You are {name}. It is just turned 9 oclock and, after a long day at work,\nYou have found yourself drifting off on the sofa.\nAll of a sudden you are jolted awake by the sound of ringing.\nYou fumble around the cushions looking for your phone, but don't get to it in time before the call cuts off.\nThe phone screen shows no caller ID.\nYou shrug it off, assuming it was somebody trying to sell you something.\n")
        print(phone_pic)
        print_slow("The phone rings again. What do you do?(answer/ignore)\n")
        while True:        
            answer = (input())
            answer = answer.lower()
            if "answer" in answer or answer == "a":
                door()
                break
            
            elif "ignore" in answer or answer =="i":
                print_slow(phone_pic1)
                print_slow("You turn your phone on silent and switch on the TV. \nYou never pick up your phone for withheld numbers, it's always robots trying to scam you. \nYou spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
                print_slow("Thank you for... not playing the game!\n")
                print(spoilsport)
                start_over()
                break
            else:
                print_slow("That's not a valid repsonce, try again\nUsing any of these words: answer,a,ignore,i")

def phone2():
    while True:
        answer = (input())
        answer = answer.lower()
        if "answer" in answer or answer=="a":
            door()
            break
            
        elif "ignore" in answer or answer =="i":
            print_slow("You turn your phone on silent and switch on the TV. \nYou never pick up your phone for withheld numbers, it's always robots trying to scam you. \nYou spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
            print_slow("Thank you for... not playing the game!\n")
            print(spoilsport)
            start_over()
            break
        else:
            print_slow("That's not a valid repsonce, try again/\nUsing any of these words: answer,a,ignore,i\n")
                
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. \n"Hello?" You hear your voice echo back to you on the other end. \n"....." "No answer. \n"Listen if you're trying to sell me something then I'm not interested!" You say before hanging up.\n""")
    print(phone_pic)
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. \nThe noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print(bangbang)
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "dont open" or answer== "d":
            note()
            break
        
        elif "open" in answer or answer == "o":
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you.\nYou're not sure why, but something in you is telling you not to answer the door.\nYou turn away from the door as the phone begins to ring once again.(answer/ignore)\n")
            answer=(input())
            answer =answer.lower
            phone2()
            break
                     
        else:
            print_slow("That is not a valid responce, try again?\nUsing any of these words: open,o,dont,d\n")  
            
def note():
    print_slow(f"""You turn the latch to the door and pull it open. \nThere's nobody there, just a cardboard box on your doorstep. That's weird, you could've sworn the knocking stopped right as you turned the latch... \nYou take a closer look at the box. It has a label that has "{name}, OPEN IN PRIVATE" in big red letters tied to it. \nYou know you should be suspicious of a strange parcel dropped on your doorstep, but there's a niggling feeling in the back of your mind that makes your curiosity take over.\n""")
    print_slow("You pick up the box and head back inside. Inside the box is a note and a photo of a house with an address scribbled on the back")
    print(note1)
    print_slow("""Your mind is spinning with questions, but you can't help but feel drawn to the house in the photo.""") 
    print(old_photo)
    print_slow("""You're sure you've seen it before, the address isn't too far from where you grew up.\nYou know deep down that this is all very suspicious, any sensible person would call the police. But....\n""")
    while True:
        answer = (input("What would you like to do? (go to house/call police)\n"))
        answer = answer.lower()
        if "house" or "h" in answer:
            kitchen()
            break
        elif "police" or "call" in answer :
            print_slow("You decide that some things just aren't worth it. This is probably just a prank, but it could be something way more dangerous. \nYou pull your phone out and type in 999.")
            print(phone_pic)
            print_slow("Over the next couple of days the police come, ask you some questions and take the box and its contents as evidence. \nYou explained to them that you don't know much, it just turned up on your doorstep one night. \nNothing comes of the mysterious note and life carries on as normal, the events of that night eventually fading away into memory.\n")
            print(police)
            print_slow("Congratulations, you were sensible and lived a long, normal life with absolutely 0 paranormal activity!\n")
            start_over()
            break
        else:
            print_slow("This is not a valid respose, try again?\nUsing any of these words: house,h,police,call")
def kitchen():
    global knife
    print_slow("""You move without thinking and grab your coat and your keys.\nThe drive doesn't take too long and you get to the address just before 10.""")
    print(car)
    print_slow("""From the looks of things the place is abandoned.\nThe garden is overgrown and the windows are filthy.\nIf anybody is stuck inside they definitely wouldn't be having a good time.""")
    print(rundown_house)
    print_slow("""As you approach the front of the house the front door swings open.\nThe wind must've caught it, you think to yourself as you walk towards the entrance.""")
    print(gate)
    print_slow(f"Hello? Jack are you in here? It's {name}!")
    print_slow ("""You shout from the doorstep, but there's no answer. With a deep breath you take a step inside. """)
    print(hallway)
    print_slow("""SLAM!\n
    The door behind you swings shut, pushing you into the hallway. You grab the handle and try to open the door, but it's stuck.""")
    print_slow("""You are now trapped inside the abandoned house. You make your way down the hall testing the doors to multiple rooms.""")
    print(hallway2)
    print_slow("""Eventually one door opens and you find yourself in the kitchen.""")
    print(dimkit)
    print_slow("""The inside is dimly lit and it's difficult to make out.\nIn the middle of the room is a table, though you can't quite see what is on top of it.\n In the corner of the room is a large cupboard that looks like it's used for storage. \nWhat would you like to do?  (Search cupboard/Search kitchen) \n""")
    print(ktab)
    answer = (input())
    answer = answer.lower()
    while True:
        if "kitchen" in answer:
            if knife == 0:
                knife =+ 1
                print_slow("You look around the kitchen. In the dim light you can't find much of use, however a glint on the table grabs your attention. You find a large knife. \nThis should come in handy if you come across anything dangerous.\n")
                print(sharps)                                
                print_slow("What do you want to do (Search kitchen/Search cupboard) \n")
                answer = (input())
            else:
                print_slow("You search around the kitchen again, but can't find anything\n")
                print_slow("What do you want to do (Search kitchen\Search cupboard) \n")
                answer = (input())
        elif "cupboard" in answer:
        
            if knife == 1:
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach.\nYou reach out and open it.\nInside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space.""")
                print_slow("""He slowly turns to face you and your stomach drops.\nHis face is gaunt and his skin looks thin and stretched too tight across his skull.""")
                print(face)
                print(""" Where his eyes should be are dark, empty pits.The man opens his mouth, lets out a screech and rushes towards you.""")
                print(gimage)
                print_slow("""Without thinking you thrust the knife forwards. Your hand plunges straight through where the man's chest should be.\nBefore you can question why, he has passed completely through you.
When you turn around to look, he's gone. On the floor of the cupboard where the man had been is a key.""")
                print(key)
                print_slow("""You pick it up, it seems to be quite old, but it must be used somewhere within the house.""") 
                loft()
                break
            else:
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach.\nYou reach out and open it.
Inside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space.""")
                print(face)
                print_slow("""He slowly turns to face you and your stomach drops.\nHis face is gaunt and his skin looks thin and stretched too tight across his skull. Where his eyes should be are dark, empty pits.
The man opens his mouth, lets out a screech and rushes towards you.""")
                print(gimage1)
                print_slow("""In a panic you stumble back and fall onto the table.
You feel a sharp pain in your back, and look down. You must not have seen the large knife lying on the table.
Your vision fades, the last thing you see is the man standing over you, his feet levitating above the ground.""")
                print(bad_ends)
                start_over()
                break
        else:
            print_slow("This is not a valid responce, try again\nusing any of these words: kitchen,cupboard")
            answer = (input())
        
def loft():
    print_slow("As you head back out of the kitchen you notice that the key seems like it'd fit into the lock on the door.\nBefore you can test it out you hear a blood curdling scream coming from the upper floor of the house, followed by a loud bang.\nYou jump and nearly drop the key. Whoever it is sounds like they're in a lot of pain. Your hands are shaking and you find yourself fighting between two choices. What should you do? (leave/check upstairs)\n")
    while True:    
        answer = (input())
        answer = answer.lower()
        if "leave" in answer:
            print_slow("Your hands shaking, you get the key into the lock on the door, twist and- CLICK!\nYou swing the door wide and sprint for your car, the sounds of screams following you from the house.\nYou jump in the driver's seat and take off down the road just as the apparition burst from the door heading straight for your car.\n")
            print_slow("You narrowly avoided the ghost's attack and made your way home.\n")
            print_slow("""Images of the spirit's face flashed in your mind keeping you awake.""")
            print(face)
            print_slow("""You sat on your bed clutching the knife and staring at your bedroom door until morning came.\nThe next day your co-workers asked what was wrong. "You look like you've seen a ghost" one of them commented. If only they knew...\n""")
            print(sharps2)
            print_slow("Congratulations! You got out of there just in time and are left with lasting psychological damage.\nOh well, could've been worse!\n")
            start_over()
            break
        elif "check" in answer or "upstairs" in answer:
            print_slow("You want to get out of there, but you can't just leave knowing someone else is in here.\nYou stuff the old key in your pocket and run up the stairs in the direction of the noise.\nWhen you reach the top of the stairs you hear more clearly that the sound is coming from up in the attic.\nA ladder is propped up against the wall, but the latch appears to be locked.You climb up the ladder and pull out the old key.\nThe lock clicks open and you enter the loft.")
            print(loft_step)
            battle()
            break
        else:
            print_slow("This is not a valid repsponce, try again\nUsing any of these words:leave,check,upstairs")
            
def battle():
    print_slow("""The inside of the attic is dark and everything is covered in a thick layer of dust.\nThe noise has stopped and there's nobody here.""")
    print_slow("""At least as far as you can tell.\nAs your eyes get used to the dark you begin to make out shapes.\nAt the far end of the room you can see what was once a person.""")
    print_slow("""Slouched to one side with something in their lap.\nCloser to you on your right you can see a large crate that looks like it's open.""")
    print(tchest)
    print_slow("""Before you can make a step forward you feel a cold chill run up your spine.\nThe apparition fades into view.""")
    print_slow("""Floating at the end of the room. It slowly raises its hand and points at you before letting out a wail and rushing towards you.""")
    print(gimage)
    print_slow("""What do you do? (check crate/check body)\n""")
   
    while True:    
        answer = (input())
        answer = answer.lower()
        if "crate" in answer or answer=="c":
            print_slow("""You jump out of the way of the spirit and run over to the crate on your right.\nIt must have something that can help you inside it.""")
            print_slow(""" right? Behind you the ghost screams and turns to charge at you again.\nYou fling open the lid to find..... It's empty.""")
            print_slow("""You don't know what you were expecting, what could even help you in this situation?\nI mean how do you kill a ghost, they're already dead!""")
            print(mutley)
            random_number = random.randint(0,1)
            if random_number == 1:
                print_slow("""The spirit flies into you, knocking you forward into the crate.\nThe impact sends the lid crashing down and trapping you inside.""")
                print_slow("""You try to slam against it but it's held down by an unimaginable force.\nYou cry out for help, banging and screaming.""")
                print(scream)
                print_slow("""But nobody can hear you.\nYou are trapped in the loft.\nYears pass before the next person comes to inspect the house, compelled by a mysterious note left on their doorstep.\nHowever, they didn't find just one spirit trapped inside the House That Jack Built.""")
                print_slow("So long Jack")
                print(bad_ends)
                start_over()
                break
            else:
                print_slow("You duck out of the way of the spirit as it passes through the crate inches from your head.\nYou look around wildly for anything that might be able to help- and notice the box the corpse is holding.\n")
                print_slow(good_ends)
                print(flash)
                print_slow(good_ends2)
                print(gold)
                print_slow(good_ends3)
                print(floater)
                print_slow(good_ends4)
                start_over()
                break
        elif "body" or "skeleton" in answer:
            print_slow(good_ends)
            print(flash)
            print_slow(good_ends2)
            print(gold)
            print_slow(good_ends3)
            print(floater)
            print_slow(good_ends4)
            start_over()
            break
        else:
            print_slow("This is not a valid repsonce, try again\nUsing any of these words:crate,c,body,skeleton")
            
def start_over():
    global knife
    global name
    print_slow("Would you like to start over? (Yes/No)\n")
    while True:
        answer = (input())
        answer = answer.lower()
        if "yes" in answer or answer == "y":
            knife = 0
            name = print_slow("What is your name? \n")
            name = input("")
            phone()
            break
        elif answer == "no" or answer == "n":
            print(spoilsport)
            print_slow("Have a nice day!")
            break
        else:
            print("This is not a valid resonces, try again\nUsing any of these words:yes,y,no.n")
print(splash)
name = print_slow("What is your name? \n")
name = input("")
knife = 0
game()
# the game can be run in this version but requires a few minor image tweaks 
# and a little bit more fine tuning of the inputs and responses not always following correct path 
# possibly me tired misspelling 