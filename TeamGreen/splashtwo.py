import  time
import sys

def slow_mov(str):
    for char in str:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()



splash=(r""")

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

slow_mov(splash)
