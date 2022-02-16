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

sharps1 =(r"""
__,,..,^            _,.--''------'' ||   _____  ______________`''--._
 \      `\   __..--''                ||  /::: / /::::::::::::::\      `\
  \       `''                        || /____/ /___ ____ _____::|    .  \
   \                          ______ ||           `    `     \_|   ( )  |
    `.                       /`     `\\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
\n I knew this would come in handy!
""")
phone_pic =(r"""
            _.._           
     __.--"" __ ""--.__    
   .'//   .-"  "-.   \\`,  
  : :'  .'.  :;  ,`.  `; ; 
 /; ;  /  T. $$ ,P  \  : : 
/: :  ;    T.:;,P    :  ; ;
)| | :      `  '      ; | |
`j | :.--------------.: | |
 ; ; |                | : :
 ; ; |                | : :
 | | |                | | |
 | | |                | | |
 : : |                | ; ;
 : : :________________: ; ;
  ; ;__    _...._    __: : 
  | ;  "-./ ,--, \,-"  : | 
  | '._   \ ;  : /   _.' | 
  :  __`-. `."",' .-'__  ; 
   ;`.__> `.J__L.' <__.':  
   ;.--._   .--.   _.--,:  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   |`.__.' `.__.' `.__.'|  
   |.--._   .--.   _.--,|  
   ;`.__.' `.__.' `.__.':  
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
                 '
            *          .
                   *       '
              *                *





   *   '*
           *
                *
                       *
               *
                     *

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
                 |    |`,-,...,/      ,'     
  /              \    | |_|   /     ,' __  r-'',
 /                |___|/  |, /  __ /-''  `'`)  |  
/_______       _,-'   ||__\ /,-' /     _,.--|  (
|        |  .-'       )   `(_   / _,.-'  ,-' _,/
|        |   `-------'       `--''       `'''


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


Team Green Proudly Presents
The House That Jack Built.

""")
gold =(r"""
   _____
  /   \\\
 |__%___|
 / : :   \
( GOLD    )
 `-------'

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

good_ends =("""
You scramble away from the ghost as it makes a swipe for you and desperately search the decaying body for clues.\nThe box's lid is open and there is an indent shaped like a knife on the inside.\n""")

good_ends2=("""You pull out the knife and in a last-ditch attempt place it down into the box.\nA perfect fit!.""")

good_ends3=("""A flash of light blinds you for a moment and the ghost screeches behind you.\nYou squeeze your eyes shut, bracing yourself for impact,\n
but nothing happens.\n""")

good_ends4=("""Where the horrifying apparition once was is now a man floating a couple inches off the ground holding the box.\nHe smiles at you and, in another flash of light, vanishes. You blink and look around, not sure of what to do. Where the box had been in the hands of the body is now a pouch with a note tied to it.""")
# add art of floating man +brilliant flash +pouch of gold and a loft hatch 
# """)

good_ends5=("""You open the pouch and find a small pile of gold coins. \nYou're unsure of the value, but you're sure it's probably quite high.""")

good_ends6=("""You make your way to the front door.\nSure enough the loft key fits the lock here too.\nYou get into your car and drive home as the sun begins to rise.

Nobody is going to believe you about any of this.


Congratulations! You beat the game and got the Good Ending!""")


def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
#This funcion allows the text throughout the game to print each character in the terminal 1 by 1.

#.sleep allows to change how fast or slow it shows each character in the terminal
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
            start_over()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")  
#This function starts the game

#The answer variable in most of the functions is what allows the player to respond to any options the player can do.

#With .lower forces any letter given to be forced in lower case, this allows the code to able to take any input that includes a capital letter.

#The while loop within this function and throughout the rest of the functions
#makes sure that any input that isn't either of the responses requiered to progress shows up as a invalid response in the terminal.

#The True that is used with the while loop is mostly used as a placeholder to allow the loop to work

#The break allows the code to come out of the while loop once the player has given a valid input.

#the \n makes it so it spaces out the line of code when it prints in the terminal.
def phone():
        print_slow(f"You are {name}. It is just turned 9 oclock and, after a long day at work,\nYou have found yourself drifting off on the sofa.\nAll of a sudden you are jolted awake by the sound of ringing.\nYou fumble around the cushions looking for your phone, but don't get to it in time before the call cuts off.\nThe phone screen shows no caller ID.\nYou shrug it off, assuming it was somebody trying to sell you something.\n")
        print(phone_pic1)
        print_slow("The phone rings again. What do you do?(answer/ignore)\n")
        while True:        
            answer = (input())
            answer = answer.lower()
            if "answer" or "pick up" in answer or answer == "a":
                door()
                break
            
            elif "ignore" in answer or answer =="i":
                print(phone_pic1)
                print_slow("You turn your phone on silent and switch on the TV. \nYou never pick up your phone for withheld numbers, it's always robots trying to scam you. \nYou spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
                print_slow("Thank you for... not playing the game!\n")
                print(spoilsport)
                start_over()
                break
            else:
                print_slow("That's not a valid repsonce, try again\n")

#This function is used once the game starts and asks the player if they want to answer the phone or to ignore

#The print function is mostly used to show ascii art used throughout the game to show up instantly in the terminal

#In the ascii pictures we used the r""" function (which the r stands for raw input) which allows the art to be able to be displayed
#exactly how they look in the terminal without causing the code to read the symbols incorrectally.

#using if "answer" in answer, makes it so when a input it provided, it will look at all the characters in the string
#and if it finds the word within the string, it accepts that input.

#the start_over function gets used each time the player either gets any ending (Which the function is explained how it works in lines 899 to 903)

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
            print_slow("That's not a valid repsonce, try again\n")

#This function acted as a solution for one of the problems we came across when responding to "dont open" to the door function below
#as the problem we had was that it would loop the start of the story if the player didn't open the door, so we created a phone2
#function which gets used if the player says dont open instead of using the phone function.
                
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. \n"Hello?" You hear your voice echo back to you on the other end. \n"....." "No answer. \n"Listen if you're trying to sell me something then I'm not interested!" You say before hanging up.\n""")
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. \nThe noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "dont" in answer or "don't" in answer or answer == "d":
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. \nYou're not sure why, but something in you is telling you not to answer the door. \nYou turn away from the door as the phone begins to ring once again.(answer/ignore)\n")
            phone2()
            break
        
        elif answer == "open" or answer=="open door" or answer=="open the door" or answer=="o":
            note()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")

#This function gets used once the player answers the phone.

#Another problem we originally come across was the code was getting confused as both the word open as it is an answer for both
#Open and don't open, we solved this by changing the elif statment to accept dont or if "dont open" is an exact match
            
def note():
    print_slow(f"""You turn the latch to the door and pull it open. \nThere's nobody there, just a cardboard box on your doorstep. That's weird, you could've sworn the knocking stopped right as you turned the latch... \nYou take a closer look at the box. It has a label that has "{name}, OPEN IN PRIVATE" in big red letters tied to it. \nYou know you should be suspicious of a strange parcel dropped on your doorstep, but there's a niggling feeling in the back of your mind that makes your curiosity take over.\n""")
    print_slow("You pick up the box and head back inside. Inside the box is a note and a photo of a house with an address scribbled on the back")
    print(note1)
    print_slow("""Your mind is spinning with questions, but you can't help but feel drawn to the house in the photo.  
You're sure you've seen it before, the address isn't too far from where you grew up.
You know deep down that this is all very suspicious, any sensible person would call the police. But....\n""")
    while True:
        answer = (input("What would you like to do? (go to house/call police)\n"))
        answer = answer.lower()
        if "house" or "go" in answer:
            kitchen()
            break
        elif "police" or "call" in answer:
            print_slow("You decide that some things just aren't worth it. This is probably just a prank, but it could be something way more dangerous. \nYou pull your phone out and type in 999.")
            print(phone_pic1)
            print_slow("Over the next couple of days the police come, ask you some questions and take the box and its contents as evidence. \nYou explained to them that you don't know much, it just turned up on your doorstep one night. \nNothing comes of the mysterious note and life carries on as normal, the events of that night eventually fading away into memory.\n")
            print(police)
            print_slow("Congratulations, you were sensible and lived a long, normal life with absolutely 0 paranormal activity!\n")
            start_over()
            break
        else:
            print_slow("This is not a valid respose, try again\n")

#This function is used once the player has opened the door to the house. similar code layout to the phone function

def kitchen():
    global knife
    print_slow(r"""You move without thinking and grab your coat and your keys. The drive doesn't take too long and you get to the address just before 10.""")
    print(car)
    print_slow(r""" From the looks of things the place is abandoned. The garden is overgrown and the windows are filthy. If anybody is stuck inside they definitely wouldn't be having a good time.""")
    print(rundown_house)
    print_slow("""As you approach the front of the house the front door swings open. The wind must've caught it, you think to yourself as you walk towards the entrance.\n""")
    print_slow(f"\"Hello? Jack are you in here? It's {name}!\"")
    print_slow (r"""You shout from the doorstep, but there's no answer. With a deep breath you take a step inside. """)
    print(hallway)
    print_slow(r"""SLAM!

The door behind you swings shut, pushing you into the hallway. You grab the handle and try to open the door, but it's stuck.

You are now trapped inside the abandoned house. You make your way down the hall testing the doors to multiple rooms.""")
    print(hallway2)
    print_slow("""
Eventually one door opens and you find yourself in the kitchen.\nThe inside is dimly lit and it's difficult to make out. \nIn the middle of the room is a table, though you can't quite see what is on top of it. In the corner of the room is a large cupboard that looks like it's used for storage. \n
""")
    print(dimkit)
    print_slow("What would you like to do? (Search cupboard/Search kitchen)\n")
   
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
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach.You reach out and open it.
Inside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space.
He slowly turns to face you and your stomach drops.
His face is gaunt and his skin looks thin and stretched too tight across his skull. Where his eyes should be are dark, empty pits.
The man opens his mouth, lets out a screech and rushes towards you.

Without thinking you thrust the knife forwards. Your hand plunges straight through where the man's chest should be.
Before you can question why, he has passed completely through you.
When you turn around to look, he's gone. On the floor of the cupboard where the man had been is a key.
You pick it up, it seems to be quite old, but it must be used somewhere within the house.""")
                print(key) 
                loft()
                break
            else:
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach.
You reach out and open it.
Inside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space.
He slowly turns to face you and your stomach drops.
His face is gaunt and his skin looks thin and stretched too tight across his skull. Where his eyes should be are dark, empty pits.
The man opens his mouth, lets out a screech and rushes towards you.
In a panic you stumble back and fall onto the table.
You feel a sharp pain in your back, and look down. You must not have seen the large knife lying on the table.
Your vision fades, the last thing you see is the man standing over you, his feet levitating above the ground.""")
                print(bad_ends)
                start_over()
                break
        else:
            print_slow("This is not a valid responce, try again\n")
            answer = (input())

#This function is used once the player has read the note in the house

#The global knife is used as a flag check if the player has obtained the knife after they searched the kitchen
#as the code will print a differnt line of code depending if they have the knife or not

#The way this code works is that using multiple if commands, we made it so if the player 
#searches the kitchen first, the variable of the knife will change to 1 meaning they have the knife
#searching the kitchen again will show a differnt string of text as the original text only shows if the knife value = 0

#Having the knife is requiered to progress in the game as without the knife, it will end with the start over function


def loft():
    print_slow("As you head back out of the kitchen you notice that the key seems like it'd fit into the lock on the door.\nBefore you can test it out you hear a blood curdling scream coming from the upper floor of the house, followed by a loud bang.\nYou jump and nearly drop the key. Whoever it is sounds like they're in a lot of pain. Your hands are shaking and you find yourself fighting between two choices. What should you do? (leave/check upstairs)\n")
    while True:    
        answer = (input())
        answer = answer.lower()
        if "leave" in answer:
            print_slow("Your hands shaking, you get the key into the lock on the door, twist and- CLICK!\nYou swing the door wide and sprint for your car, the sounds of screams following you from the house.\nYou jump in the driver's seat and take off down the road just as the apparition burst from the door heading straight for your car.\n")
            print_slow("You narrowly avoided the ghost's attack and made your way home.\n")
            print_slow("""Images of the spirit's face flashed in your mind keeping you awake. You sat on your bed clutching the knife and staring at your bedroom door until morning came.\nThe next day your co-workers asked what was wrong. "You look like you've seen a ghost" one of them commented. If only they knew...\n""")
            print_slow("Congratulations! You got out of there just in time and are left with lasting psychological damage. Oh well, could've been worse!\n")
            start_over()
            break
        elif "check" in answer or "upstairs" in answer:
            print_slow("You want to get out of there, but you can't just leave knowing someone else is in here.\nYou stuff the old key in your pocket and run up the stairs in the direction of the noise.\nWhen you reach the top of the stairs you hear more clearly that the sound is coming from up in the attic.\nA ladder is propped up against the wall, but the latch appears to be locked.You climb up the ladder and pull out the old key.\nThe lock clicks open and you enter the loft.")
            print(loft_step)
            battle()
            break
        else:
            print_slow("This is not a valid repsponce, try again\n")

#The loft function is used once the player checks the cupboard if they have the knife.

#Saying leave will result in one of the endings and the start over function to be used.
            
def battle():
    print_slow("""The inside of the attic is dark and everything is covered in a thick layer of dust. The noise has stopped and there's nobody here, or at least as far as you can tell.
As your eyes get used to the dark you begin to make out shapes. \nAt the far end of the room you can see what was once a person, slouched to one side with something in their lap. \nCloser to you on your right you can see a large crate that looks like it's open.

Before you can make a step forward you feel a cold chill run up your spine.\nThe apparition fades into view, floating at the end of the room. It slowly raises its hand and points at you before letting out a wail and rushing towards you.\n""") 
    print(floater)
    print_slow("What do you do? (check crate/check body)\n")
   
    while True:    
        answer = (input())
        answer = answer.lower()
        if "crate" in answer or answer=="c":
            print_slow("""You jump out of the way of the spirit and run over to the crate on your right. \nIt must have something that can help you inside it, right? Behind you the ghost screams and turns to charge at you again.
You fling open the lid to find..... It's empty. \nYou don't know what you were expecting, what could even help you in this situation? \nI mean how do you kill a ghost, they're already dead!""")
            random_number = random.randint(0,1)
            if random_number == 1:
                print_slow("""The spirit flies into you, knocking you forward into the crate. The impact sends the lid crashing down and trapping you inside. \nYou try to slam against it but it's held down by an unimaginable force. \nYou cry out for help, banging and screaming... \nBut nobody can hear you.
You are trapped in the loft. \nYears pass before the next person comes to inspect the house, compelled by a mysterious note left on their doorstep. \nHowever, they didn't find just one spirit trapped inside the House That Jack Built.""")
                print(bad_ends)
                start_over()
                break

            else:
                print_slow("You duck out of the way of the spirit as it passes through the crate inches from your head. \nYou look around wildly for anything that might be able to help- and notice the box the corpse is holding.\n")
                print_slow(good_ends)
                print_slow(good_ends2)
                print(box)
                print_slow(good_ends3)
                print(flash)
                print_slow(good_ends4)
                print(note2)
                print_slow(good_ends5)
                print(gold)
                print_slow(good_ends6)
                start_over()
                break
        
        elif "body" in answer:
            print_slow(good_ends)
            print_slow(good_ends2)
            print(box)
            print_slow(good_ends3)
            print(flash)
            print_slow(good_ends4)
            print(note2)
            print_slow(good_ends5)
            print(gold)
            print_slow(good_ends6)
            start_over()
            break
        else:
            print_slow("This is not a valid repsonce, try again\n")

#The battle function is used once the player checks upstairs

#The way this code works is that if the player inputs crate, then it uses the random.radient function to generate a number between 0 and 1
#if the number is 1 then it a bad ending and then the start over function
#if the number is any other number (it can only print out 0 or 1 so it's a 50% chance)
#then it will print out the good ending using variables and the start over function at the end
            
def start_over():
    global knife
    global name
    print_slow("Would you like to start over? (Yes/No) \n")
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
            print_slow("Have a nice day!")
            break
        else:
            print("This is not a valid resonces, try again")

#This function is used each time the player gets to any ending in the game

#if the player says yes then the knife value gets set back to 0 to prevent players to skip searching the kitchen after replying it.
#it also resets the players name, allowing differnt players to change their name each time the game is replayed without using the game function again.
#saying no will fully stop the entier game.

print(splash)
name = print_slow("What is your name? \n")
name = input("")
knife = 0

#This is the very first part of code the player will see once the game runs, the knife value is hidden from view.

game()