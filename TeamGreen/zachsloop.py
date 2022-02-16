import sys
import time
def slow_mov(str):
    for char in (str):
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()


#answer_yes =["yes","Yes","Y","y",]
#answer_no = ["No","no","N",""]
# "answer" or "answer the phone" or "answer phone" or "pick up" or "pick up phone"
#"ignore" or "ignore phone" or "ignore call" or "dont answer" or "don't answer" or "don't pick up" or "dont pick up"       
def print_slow(str):
    for char in str:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
def game():
    print_slow(f"{name}, Would you like to play a game? (yes/no) ")
    
    while True:        
        answer = (input())
        answer = answer.lower()

        if answer == "yes":
            slow_mov(r"""

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
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      

""")
            print_slow("Welcome to the game\n")    
            print_slow(f"You are {name}. It is just turned 9 oclock and, after a long day at work, you have found yourself drifting off on the sofa. All of a sudden you are jolted awake by the sound of ringing. You fumble around the cushions \nlooking for your phone, but don't get to it in time before the call cuts off. The phone screen shows no caller ID. You shrug it off, assuming it was somebody trying to sell you something.\n")
            print_slow("The phone rings again. What do you do?(answer/ignore)\n")
            phone()
            break
        
        elif answer =="no":
            print_slow("Okay maybe another Time")
            break
                     
        else:
            print_slow("That is not a valid responce, try again ")  
def phone():
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "answer":
            door()
            break
        
        elif answer == "ignore":
            print_slow("You turn your phone on silent and switch on the TV. You never pick up your phone for withheld numbers, it's always robots trying to scam you. You spend the rest of the night watching a show about truck drivers working in dangerous conditions. Hey, it passes the time.\n")
            print_slow("Thank you for... not playing the game!")
            break
        else:
            print_slow("That's not a valid repsonce, try again  ")
def door():           
    print_slow("""Confused as to why they rang back, you answer the phone. "Hello?" "You hear your voice echo back to you on the other end. "....." "No answer. "Listen if you're trying to sell me something then I'm not interested!" "You say before hangingup.\n""")
    print_slow("As soon as you press the red button on your phone screen you hear a loud, urgent banging on your front door. The noise makes you jump and nearly drop your phone. You stand up as the knocking gets louder.\n")
    print_slow("Nobody would call round at this time of night... What do you do?(open the door/dont open)\n")
    
    while True:        
        answer = (input())
        answer = answer.lower()
        if answer == "open the door":
            print_slow("You open the door")
            break
        
        elif answer =="dont open":
            print_slow("As you go to turn the latch and unlock the door a sense of dread suddenly washes over you. You're not sure why, but something in you is telling you not to answer the door. You turn away from the door as the phone begins to ring once \nagain.(answer/ignore)\n")
            phone()
            break
                     
        else:
            print_slow("That is not a valid responce, try again ")  
name = print_slow("What is your name? ")
name = input("")
game()