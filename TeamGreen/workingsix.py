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
\"This knife looks pretty handy 
I wonder what else I'll find in this creepy house?.\"
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
splash =(r"""

dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddooodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddc,;;:cloddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddlodddddddddddddddddxl'',,'',;cddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddl:,cxddddddddddddddddo;.''......':odddddddddddddolloodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddc,,,;lddddddxxxddddddl,.......;:cc:lddddddddddddxl,.'',:lddddddddddddddddddddddddddddddddddddddddxdclxdddddddddddddddddddddddddddddddd
ddddddddddxddddc'''''':lodxxxlcc,;lc,........;ddddddxdodxddddddddc....,:lddddddddddddddddddddddddddddddddddddddddxc.'dxddddddddddddddddddddddddddddddd
dddddddddddddxl'........',;;:,.......... ....,oxddddd:':dxxxdlcc;.....lxddddddddddddddddddddddddddddddddddddddddxo' .cxddddddddddddddddddddddddddddddd
ddddddddddddxd,..............           .coollodxdddc...',;:,.     .clodxxxxxxddddddddddddxdddddddddddddddxdddddd;   'oxdddddddddddddddddddddddddddddd
xxxxddddddxxxo::loooc...''..        .,;,:dddxxxxxxxo,.''....     ,clddxxxxxxxxdddxdddxxxxxxxxxddxxddxxxxxxdxxddxc.   .cxddxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxddxxxddxdccoddd:. .    .lxxddddddxxxxdxdllddccoo:,,..lxdxdxxxxxxxdxxxxxdlcc:::;:cldxxxxxxxxxxxxxddxl.     'oxddxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxdxocloc,. :xxxdc::::::ccldxxxxxxxxdxxxdloxxxxxxxxxxxxxxxxxd:.....;lodddxxxxxxxxxxxxxxo.       :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdxdc':xxxdl,'''...';ldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo:....';ldxxxxxxxxxxxxxxxdxo'        .oxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoodxxxd;.....:dxxxxxxdolloodxxxxxdodxxxxxxxdc;,,. ..'cdxxxxxxxxxxxxxxxxxxxo'          ;dxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl......;dxxxxxxo;''';ldxxdl;,;::::;;,'.    .cdddxxxxxxxxxxxxxxxxxxxo.           .lxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxodxxxxxxxxxdloc'.....;:ldxxxxxd;...cxxxxl'......',;;'',;;,;oxxxxxxxxxxxxxxxxxxxxxl.             ,dxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxo;;oxxxxxxdc'...    .ododxxxdl:,. .;ldxxdc;cloolldxxxddxxxxddxxxxxxxxxxxxxxxxxxxdc.              .cxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxd:'',;:ccc:;.      .;co:,;ccc;.  .'cdxxxxxdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.                .oxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxo;.'......        .lxxd;..........lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo'                   ;dxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxo,...''...,;' ... .cxxdc:olcodooocoxxxxxxxoc::;;;;:clodxxxxxxxxxxxxxxxxxxxxxxdc.                    .lxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxd;':oddc:oxxdllddo::oxxxxxxxxxxxxxxxxxxxxxdl,.....;oddxxxxxxxxxxxxxxxxxxxxxxo,                       'oxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxddxxxxxxxxxxxxxxxxddxxxxxxxxxxxxxxxxxxxdddc... .,coddxxxxxxxxxxxxxxxxxxxxxc.                         ;xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdlldxxxxxxdc,...  .':dxxxxxxxxxxxxxxxxxxxxxxxo,                           .lxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl,',;;;,,'...     .lxxxxxxxxxxxxxxxxxxxxxxxd:.                             'oxxxxxxxxxxxxxxxxxxxxxx
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
OOOOOOOOOOOkxxxddxddxxoodxocoxxddl'.';clc:,.,dd'                            .::cc..;ccc;.                          .dkllxx,   .'.''. 'xOOOOOOOOOOOOOOO
OOOOOOOOOOOkkkOOOOkOOOxoloooxxodxxo'.llloc''cc'                             .lolo:;oooo;.                          .cl:cdo'          ,kOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOkkOOOOdllodddoodkOOx,,doc,..'.                              ,xOkkc:xkkkl.                                            ;OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOxdxdxxdloxdo::coxkxdd;.cl'.:,                               'xkkOl;dkkk:                                             ;doclkOOOOOOOOOOO
OOOOOOOOOOOOOOkOxllc:oooxdoc;,'clllclo;.....                                'dxkOlckkxk;                                                 .oOOOOOOOOOOO
OOOOOOOOOOOOOkkxocc,.:l::cc:;:;::,,,;lo,                                    .;::c',lool.                                                  ,x0OOOOOOOOO
OOOOOOOOOOOOxoccc;'..';,,;:cll:coool:,;,                                                                                                   :OOOOOOOOOO
OOOOOOOOOOkxo:::cc;'',:coc;loclcclloo;.                                                                                                    .lOOOOOOOOO
00OOOOOOOOdc;;lxdl;,:cc:clc;:loc::;,,.                                                         .';.  ';.                                    .oOOOOOOOO
00OOOOkxkdo;',:c;:c:cdoloxdc:oddxd;.                                                         .:xOO: .x0Od;.                                  .oOO00000
O0Okxkxdddo;';;:lol::looddodl:loo;.                                                         .oOO0O: .x0O0Ox,                                  .oO000O0
000Okdolllc;,cl::ll:,,;looloo;'..                                                          .o0000O: .x000O0k,                                  .lO0000
0000Oxlc::,'.,;:;';,,'';c;;;,'                                                            .lO0000O: 'x0000O0x'                                  .cO000
000Okoc:lo:'............'',;;'.':;..                                                      ,k0O000O; 'x0000O00c                                    :k00
0000OOxlcclc;,'':l;.''','..','.','...                                                     l000000O; 'x0000000o.                                 .clx00
0000OOxddocc:;;,;:;,'',.','.','''..                                                      .o000000O; 'x0O00000o.                                .o00000
0000Oxocloodoll:,,;;;,'';;'.,;;ll;'..'.                                                  .l0O0000k, 'x0OOOOOOc                                 ,k00000
OxxkkdolokO0kdoloooool,'cc:lxdoc:;,:oc.                                                   .;;;:::;. .;;;;;;;'.                          ':::'  c000000
0kxxxoodoloooloddoc;;;cloldOkdc:ldollo,     ...........                                   'dxxxxxxc.ckxxxxxxo.                         .o000c .o000000
0Oxdxxddddl:;looo:;coxOOkoldoloxkxddddl.   .o0OOkclkkxkl.                                 ;O000000d'l0000000x.                         .lkkx; .x000000
00Oxxxolclllcllllok0000kddddkkkO000OOOx'   .o000Ood0000d.                                 ,O000000d'l0000000d.                         'dxxd' ,k000000
00000OkxkOOOOOxdk000OOkxdkxodk00000000k,    ;xxxdclxxxkl.                                 ,O000000o.l0000000o.           .,,;;'.,:::'  :000x' ;O000000
00000000000000000OO00OkkOOOOkxO0000000O;    ;OOOOdokkkOl.                                 ,k000000o.c0000000c            :0000dck000:  .;;;.  :O000000
0OO0OOOOOOkkkkO00kdkOxodxkOOOO00OO0000O;    'dkkkdd0000d.                                 ,k000000l.l000000O;            cOOOOocdkkx,         :O0O00O0
xodkkkdoddcclodxkkdllc::cc;;cc:;,,,,,::.     ......',,,.                                  'k00000Ko'oK00000k'            :xxxxlcdxkd.         ckdkOkkO
.....'',,;:;'''.......                                                                    .,;;;;;;..,llooooc.            l0000dxK0Kx.         ,cokooxk
                                                                                                                         'llll;;:::'          .,,,....
                                                                                                                                                      
                                                                                                                                                      
Team Green Proudly Presents\n The House That Jack Built.

""")

good_ends=(rf"""You scramble away from the ghost as it makes a swipe for you and desperately search the decaying body for clues. The box's lid is open and there is an indent shaped like a knife on the inside. You pull out the knife and in a last-ditch attempt place it down into the box. A perfect fit.
{sharps1}
{box}

A flash of light blinds you for a moment and the ghost screeches behind you. You squeeze your eyes shut, bracing yourself for impact, but nothing happens.
Where the horrifying apparition once was is now a man floating a couple inches off the ground holding the box. He smiles at you and, in another flash of light, vanishes. You blink and look around, not sure of what to do. Where the box had been in the hands of the body is now a pouch with a note tied to it.

{note2}

You open the pouch and find a small pile of gold coins. You're unsure of the value, but you're sure it's probably quite high.

You make your way to the front door. Sure enough the loft key fits the lock here too. You get into your car and drive home as the sun begins to rise.

Nobody is going to believe you about any of this.


Congratulations! You beat the game and got the Good Ending!
""")
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
        
def game():
    print_slow(splash)
    print_slow(f"{name}, Would you like to play a game? (Yes/No)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "yes" in answer or answer == "y":
            print_slow("Welcome to the game\n")
            phone()  
            break
        
        elif answer =="no" or answer == "n":
            print_slow("Okay maybe another Time\n")
            start_over()
            break
                     
        else:
            print_slow("That is not a valid responce, try again\n")  

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
                print(bad_ends)
                start_over()
                break
            else:
                print_slow("That's not a valid repsonce, try again\n")

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
            print(bad_ends)
            start_over()
            break
        else:
            print_slow("That's not a valid repsonce, try again\n")
                
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. \n"Hello?" You hear your voice echo back to you on the other end. \n"....." "No answer. \n"Listen if you're trying to sell me something then I'm not interested!" You say before hanging up.\n""")
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. \nThe noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    while True:        
        answer = (input())
        answer = answer.lower()
        if "open" in answer or answer=="o":
            note()
            break
        
        elif "dont" in answer or answer == "dont open""d":
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. \nYou're not sure why, but something in you is telling you not to answer the door. \nYou turn away from the door as the phone begins to ring once again.(answer/ignore)\n")
            phone2()
            break
                     
        else:
            print_slow("That is not a valid responce, try again?\nUsing any of these words: open,o,dont,dont open,d\n")  
            
def note():
    print_slow(f"""You turn the latch to the door and pull it open. \nThere's nobody there, just a cardboard box on your doorstep. That's weird, you could've sworn the knocking stopped right as you turned the latch... \nYou take a closer look at the box. It has a label that has "{name}, OPEN IN PRIVATE" in big red letters tied to it. \nYou know you should be suspicious of a strange parcel dropped on your doorstep, but there's a niggling feeling in the back of your mind that makes your curiosity take over.\n""")
    print_slow("You pick up the box and head back inside. Inside the box is a note and a photo of a house with an address scribbled on the back")
    print(note1)
    print_slow("""Your mind is spinning with questions, but you can't help but feel drawn to the house in the photo. 
    You're sure you've seen it before, the address isn't too far from where you grew up.
    You know deep down that this is all very suspicious, any sensible person would call the police. But....\n""")
    while True:
        answer = (input("What would you like to do? (go to house/call police)"))
        answer = answer.lower()
        if "house" in answer:
            kitchen()
            break
        elif "police" or "call" in answer:
            print_slow("You decide that some things just aren't worth it. This is probably just a prank, but it could be something way more dangerous. \nYou pull your phone out and type in 999.")
            print(phone_pic)
            print_slow("Over the next couple of days the police come, ask you some questions and take the box and its contents as evidence. \nYou explained to them that you don't know much, it just turned up on your doorstep one night. \nNothing comes of the mysterious note and life carries on as normal, the events of that night eventually fading away into memory.\n")
            print(police)
            print_slow("Congratulations, you were sensible and lived a long, normal life with absolutely 0 paranormal activity!\n")
            start_over()
            break
        else:
            print_slow("This is not a valid respose, try again\n")
def kitchen():
    global knife
    print_slow(r"""You move without thinking and grab your coat and your keys. The drive doesn't take too long and you get to the address just before 10.""")
    print(car)
    print_slow(r""" From the looks of things the place is abandoned. The garden is overgrown and the windows are filthy. \nIf anybody is stuck inside they definitely wouldn't be having a good time.""")
    print(rundown_house)
    print(hallway)
    print_slow(r"""As you approach the front of the house the front door swings open. The wind must've caught it, you think to yourself as you walk towards the entrance.""")
    print_slow(f""""Hello? Jack are you in here? It's {name}!"
You shout from the doorstep, but there's no answer. With a deep breath you take a step inside.

SLAM!

The door behind you swings shut, pushing you into the hallway. You grab the handle and try to open the door, but it's stuck.

You are now trapped inside the abandoned house. You make your way down the hall testing the doors to multiple rooms.

Eventually one door opens and you find yourself in the kitchen. The inside is dimly lit and it's difficult to make out. \nIn the middle of the room is a table, though you can't quite see what is on top of it. In the corner of the room is a large cupboard that looks like it's used for storage. \nWhat would you like to do?  (Search cupboard/Search kitchen) \n""")

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
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach. \nYou reach out and open it.
Inside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space. \nHe slowly turns to face you and your stomach drops.
His face is gaunt and his skin looks thin and stretched too tight across his skull. Where his eyes should be are dark, empty pits.
The man opens his mouth, lets out a screech and rushes towards you.

Without thinking you thrust the knife forwards. Your hand plunges straight through where the man's chest should be. \nBefore you can question why, he has passed completely through you.
When you turn around to look, he's gone. On the floor of the cupboard where the man had been is a key. \nYou pick it up, it seems to be quite old, but it must be used somewhere within the house.""")
                print_slow(key) 
                loft()
                break
            else:
                print_slow("""You head over to the cupboard. The door rattles slightly as you approach. \nYou reach out and open it.
Inside the cupboard is the shape of a man, tall and hunched over to fit in the confines of the space. \nHe slowly turns to face you and your stomach drops.
His face is gaunt and his skin looks thin and stretched too tight across his skull. Where his eyes should be are dark, empty pits.
The man opens his mouth, lets out a screech and rushes towards you. \nIn a panic you stumble back and fall onto the table.
You feel a sharp pain in your back, and look down. You must not have seen the large knife lying on the table.
Your vision fades, the last thing you see is the man standing over you, his feet levitating above the ground.""")
                print(bad_ends)
                start_over()
                break
        else:
            print_slow("This is not a valid responce, try again\n")
            answer = (input())
        
def loft():
    print_slow("As you head back out of the kitchen you notice that the key seems like it'd fit into the lock on the door. Before you can test it out you hear a blood curdling scream coming from the upper floor of the house, followed by a loud bang. You jump and nearly drop the key. Whoever it is sounds like they're in a lot of pain. Your hands are shaking and you find yourself fighting between two choices. What should you do? (leave/check upstairs)")
    while True:    
        answer = (input())
        answer = answer.lower()
        if "leave" in answer:
            print_slow("Your hands shaking, you get the key into the lock on the door, twist and- CLICK! You swing the door wide and sprint for your car, the sounds of screams following you from the house. You jump in the driver's seat and take off down the road just as the apparition burst from the door heading straight for your car.")
            print_slow("You narrowly avoided the ghost's attack and made your way home.")
            print_slow("""Images of the spirit's face flashed in your mind keeping you awake. You sat on your bed clutching the knife and staring at your bedroom door until morning came. The next day your co-workers asked what was wrong. "You look like you've seen a ghost" one of them commented. If only they knew...""")
            print_slow("Congratulations! You got out of there just in time and are left with lasting psychological damage. Oh well, could've been worse!")
            start_over()
            break
        elif "check" in answer or "upstairs" in answer:
            print_slow("You want to get out of there, but you can't just leave knowing someone else is in here. You stuff the old key in your pocket and run up the stairs in the direction of the noise.When you reach the top of the stairs you hear more clearly that the sound is coming from up in the attic. A ladder is propped up against the wall, but the latch appears to be locked.You climb up the ladder and pull out the old key. The lock clicks open and you enter the loft.")
            battle()
            break
        else:
            print_slow("This is not a valid repsponce, try again\n")
            
def battle():
    print_slow("""The inside of the attic is dark and everything is covered in a thick layer of dust. The noise has stopped and there's nobody here, or at least as far as you can tell.
As your eyes get used to the dark you begin to make out shapes. \nAt the far end of the room you can see what was once a person, slouched to one side with something in their lap. \nCloser to you on your right you can see a large crate that looks like it's open.

Before you can make a step forward you feel a cold chill run up your spine. The apparition fades into view, floating at the end of the room. It slowly raises its hand and points at you before letting out a wail and rushing towards you. 

What do you do? (check crate/check body)\n""")
   
    while True:    
        answer = (input())
        answer = answer.lower()
        if "crate" in answer:
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
                print_slow(good_ends, car)
                start_over()
                break
        elif "body" or "skeleton" in answer:
            print_slow(good_ends)
            break
        else:
            print_slow("This is not a valid repsonce, try again\n")
            
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
        if answer == "no" or answer == "n":
            print_slow("Have a nice day!")
            break
print(splash)            
name = print_slow("What is your name? \n")
name = input("")
knife = 0
game()
