import time             #module to control time
import sys              # module for control print 
#import zachs2loop as kitchen



def slow_mov(str):                   #def for controlling slow_mov function called multiple times
    for char in (str):
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()


answer_yes = ["Yes", "Y", "yes", "y","loft","Loft"]             #list of positive responses
answer_no = ["No", "N", "no", "n","search","Search"]            # list of negative responses

# 1st use of slow_mov manual inputted text string had a few problems with alignment so using r before triple quotes to print as literal tip leave a line to allow for spacing 
slow_mov(r"""

                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                     
                                                //\/\/\/\/\\/|||||||\//\/\/\/\/\\
                                               /////////////    |    \\\\\\\\\\\\\
                                              ///`````````//////|\\\\\\\````````\\\
                                             //||\\ <__-----///   \\\-----__> //||\\
                                            |||||||||||||||||/  /\ \|||||||||||||||||
                                            ||||||||||||||||/  /__\ \||||||||||||||||
                                            \\|||||||||||||/         \|||||||||||||//
                                             [============>___________<============]
                                              \\\\\\\\\\\ |||||||||||||| //////////
                                               ||||||||||||||/      \|||||||||||||
                                               [------------/        \-----------]
                                                                                              """)
# 2nd use of named function using ascii banner art 
slow_mov(r"""
#######                          #####                                 
   #    ######   ##   #    #    #     # #####  ###### ###### #    #    
   #    #       #  #  ##  ##    #       #    # #      #      ##   #    
   #    #####  #    # # ## #    #  #### #    # #####  #####  # #  #    
   #    #      ###### #    #    #     # #####  #      #      #  # #    
   #    #      #    # #    #    #     # #   #  #      #      #   ##    
   #    ###### #    # #    #     #####  #    # ###### ###### #    #    
                 
                ######                                              ######                                           
                #     # #####   ####  #    # #####  #      #   #    #     # #####  ######  ####  ###### #    # #####  ####
                #     # #    # #    # #    # #    # #       # #     #     # #    # #      #      #      ##   #   #   #
                ######  #    # #    # #    # #    # #        #      ######  #    # #####   ####  #####  # #  #   #    ####
                #       #####  #    # #    # #    # #        #      #       #####  #           # #      #  # #   #        #
                #       #   #  #    # #    # #    # #        #      #       #   #  #      #    # #      #   ##   #   #    #
                #       #    #  ####   ####  #####  ######   #      #       #    # ######  ####  ###### #    #   #    ####   ##
 """)
#standard print line to sim page change used r again for alinhgment (blame google :))
print(r"""
=========================================================================================================================================================
=========================================================================================================================================================






     MIght Add More art here...........Hmmm Maybe!












=========================================================================================================================================================
=========================================================================================================================================================
    """)
slow_mov(r"""
   #                                 ###           #     #                         
  # #    ####  ##### #  ####  #    # ###  ####     #     #   ##   #    # ######    
 #   #  #    #   #   # #    # ##   #  #  #         #     #  #  #  #    # #         
#     # #        #   # #    # # #  # #    ####     ####### #    # #    # #####     
####### #        #   # #    # #  # #          #    #     # ###### #    # #         
#     # #    #   #   # #    # #   ##     #    #    #     # #    #  #  #  #         
#     #  ####    #   #  ####  #    #      ####     #     # #    #   ##   ######    
                                                                                   
                         #####                                                                                           
                        #     #  ####  #    #  ####  ######  ####  #    # ###### #    #  ####  ######  ####              
                        #       #    # ##   # #      #      #    # #    # #      ##   # #    # #      #                  
                        #       #    # # #  #  ####  #####  #    # #    # #####  # #  # #      #####   ####              
                        #       #    # #  # #      # #      #  # # #    # #      #  # # #      #           # ### ### ### 
                        #     # #    # #   ## #    # #      #   #  #    # #      #   ## #    # #      #    # ### ### ### 
                         #####   ####  #    #  ####  ######  ### #  ####  ###### #    #  ####  ######  ####  ### ### ### 
""")
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



print(r"""                                             LET'S START YOUR ADVENTURE
                                                         

It is just turned 9 oclock and, after a long day at work, you have found yourself drifting off on the sofa.
All of a sudden you are jolted awake by the sound of ringing. 
You fumble around the cushions looking for your phone, but don't get to it in time before the call cuts off.
The phone screen shows no caller ID. You shrug it off, assuming it was somebody trying to sell you something.
The phone rings again. What do you do ?


Will you Answer the phone?. (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\n A strangers voice asks for your help, \nI'm trapped in the loft you will need to find something to break the lock.\nWill you help the stranger by searching the house. (Yes / No)\n")
    ans2 = input(">>\n")

    if ans2 in answer_yes:
        print("\nYou find a key and a broken hammer \nDo You head towards the loft now or keep searching for clues\n")
        ans3 =input(">>")
        if ans3 in answer_yes:
            #kitchen()
            slow_mov("""You search the kitch for more clues\n """)
    elif ans2 in answer_no:
        print("\nYou keep searching around looking for anything else that could help when suddenly you hear a scream!!.\n Followed by a loud thud from the loft.\nyou took long and the killer has struck.\n GAME OVER")

    #else:
    #    print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nSuddenly there's a loud banging at the door. \n Will you open the door? (Yes / No)\n")

    ans4 = input(">>")

    if ans4 in answer_yes:
        print("\nThere's nobody at the door as you open it,\n The phone begins to ring again.\n You turn to answer the phone and are struck a fatal blow from behind")

    elif ans4 in answer_no:
        print("\nThe Sorry! You are dead. ")

    #else:
        #print("\nYou typed the wrong input. GOODBYE!")

#else:
    #print("\nYou typed the wrong input. GOODBYE!")
