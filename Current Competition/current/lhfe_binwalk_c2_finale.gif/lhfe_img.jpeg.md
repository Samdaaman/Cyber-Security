[Go back to contents](../../contents.md)  
# Target: img.jpeg  -  Quality: high  
## Path: current/lhfe_binwalk_c2_finale.gif/img.jpeg  
---  
## Possible flags:  
 - Strings (All) recipe (Found galf in output): ``0
f945cc88e1ee:galf
!1!%)+...
383``  
 - Strings (All) recipe (Found matching regex: [a-zA-Z0-9]{12}:[a-zA-Z0-9]{4}): ``f945cc88e1ee:galf``  
 - Strings (All) recipe (When reversed we get: ): ``flag:ee1e88cc549f``  
  
---  
&nbsp;  
### Recipe: File recipe - Quality: unknown  
#### file current/lhfe_binwalk_c2_finale.gif/img.jpeg  
```  
current/lhfe_binwalk_c2_finale.gif/img.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=5, xresolution=74, yresolution=82, resolutionunit=1], baseline, precision 8, 300x168, components 3  
  
```  
&nbsp;  
  
### Recipe: Head recipe - Quality: unknown  
#### xxd current/lhfe_binwalk_c2_finale.gif/img.jpeg | head -n 40  
```  
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......  
00000010: 0001 0000 ffe1 00b6 4578 6966 0000 4d4d  ........Exif..MM  
00000020: 002a 0000 0008 0005 011a 0005 0000 0001  .*..............  
00000030: 0000 004a 011b 0005 0000 0001 0000 0052  ...J...........R  
00000040: 0128 0003 0000 0001 0001 0000 0213 0003  .(..............  
00000050: 0000 0001 0001 0000 8769 0004 0000 0001  .........i......  
00000060: 0000 005a 0000 0000 0000 0001 0000 0001  ...Z............  
00000070: 0000 0001 0000 0001 0005 9000 0007 0000  ................  
00000080: 0004 3032 3332 9101 0007 0000 0004 0102  ..0232..........  
00000090: 0300 9213 0002 0000 0012 0000 009c a000  ................  
000000a0: 0007 0000 0004 3031 3030 a001 0003 0000  ......0100......  
000000b0: 0001 ffff 0000 0000 0000 6639 3435 6363  ..........f945cc  
000000c0: 3838 6531 6565 3a67 616c 6600 ffdb 0084  88e1ee:galf.....  
000000d0: 0009 0607 1210 1015 1210 1215 1615 1517  ................  
000000e0: 1615 1716 1715 1515 1516 1615 1516 1615  ................  
000000f0: 1515 1718 1d28 2018 1a25 1d15 1621 3121  .....( ..%...!1!  
00000100: 2529 2b2e 2e2e 171f 3338 332d 3728 2d2e  %)+.....383-7(-.  
00000110: 2b01 0a0a 0a0e 0d0e 1710 101a 2d26 1f25  +...........-&.%  
00000120: 2d2d 2e2d 2d2d 2d2d 2d2d 2b2d 2d2d 2d2d  --.-------+-----  
00000130: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d  ----------------  
00000140: 2b2d 2d2d 2d2d 2d2d 2d2b 2d2d 2d2d 2d2d  +--------+------  
00000150: 2d2d ffc0 0011 0800 a801 2c03 0111 0002  --........,.....  
00000160: 1101 0311 01ff c400 1b00 0001 0501 0100  ................  
00000170: 0000 0000 0000 0000 0000 0001 0304 0506  ................  
00000180: 0207 ffc4 004b 1000 0103 0202 0508 0508  .....K..........  
00000190: 0805 0207 0000 0001 0002 0304 1112 2105  ..............!.  
000001a0: 0631 4151 1322 3261 7181 91a1 0742 52b1  .1AQ."2aq....BR.  
000001b0: d123 3362 8292 a2c1 f014 1517 3453 7293  .#3b........4Sr.  
000001c0: e116 54d2 d3f1 24c2 3543 7383 a3b2 b3ff  ..T...$.5Cs.....  
000001d0: c400 1b01 0100 0203 0101 0000 0000 0000  ................  
000001e0: 0000 0000 0001 0203 0405 0607 ffc4 003a  ...............:  
000001f0: 1100 0201 0203 0504 0806 0202 0301 0000  ................  
00000200: 0000 0102 0311 0421 3105 1241 5161 1371  .......!1..AQa.q  
00000210: 91a1 0614 2232 81c1 d1e1 1533 4252 b1f0  ...."2.....3BR..  
00000220: 6292 34a2 23b2 f143 ffda 000c 0301 0002  b.4.#..C........  
00000230: 1103 1100 3f00 f6c4 0080 1002 0040 0801  ....?........@..  
00000240: 019f d31a 7832 4631 99d9 c317 65f3 f2ba  ....x2F1....e...  
00000250: ab65 e30b a2e9 c549 42bf 4b4f 0451 992a  .e.....IB.KO.Q.*  
00000260: 7006 376b 9c2f dc37 93d4 3355 9ce3 1579  p.7k./.7..3U...y  
00000270: 19e8 61ea 579a a749 5db3 2474 a688 a836  ..a.W..I].$t...6  
  
```  
&nbsp;  
  
### Recipe: Tail recipe - Quality: unknown  
#### xxd current/lhfe_binwalk_c2_finale.gif/img.jpeg | tail -n 40  
```  
00002a80: 7ffe 6fc7 ec39 5da8 aea6 a5fd 22aa a591  ..o..9]....."...  
00002a90: 59a0 9660 2f21 c764 60e2 01ce ddc3 6ee1  Y..`/!.d`.....n.  
00002aa0: 74f5 67cc 2db9 16ec a9bf 1fb0 e684 f477  t.g.-..........w  
00002ab0: 3d44 0d96 4944 25f9 8639 85ce c276 1773  =D..ID%..9...v.s  
00002ac0: 8589 db6e cec0 f567 cc3d bb04 edb8 fc7e  ...n...g.=.....~  
00002ad0: c6c7 5335 45da 3df2 bdd3 0931 b5ad c985  ..S5E.=....1....  
00002ae0: 96c2 49b9 bb8f 1596 952d c6dd ce7e 3f68  ..I......-...~?h  
00002af0: ac54 6315 1b59 f3bf c8e7 583d 2152 52dd  .Tc..Y....X=!RR.  
00002b00: b19e 5e41 eac6 4600 7e94 9b3c 2e56 6b9c  ..^A..F.~..<.Vk.  
00002b10: e8c1 b301 51e9 02ae 5a88 e47b f044 c918  ....Q...Z..{.D..  
00002b20: e314 7934 b438 1707 1daf b8b8 cf2e a0a2  ..y4.8..........  
00002b30: e64d c563 db01 be61 58c0 2a01 0940 65b5  .M.c...aX.*..@e.  
00002b40: a2ba e793 07b7 f155 64a1 cd5d a4c2 c2f2  .......Ud..]....  
00002b50: 3376 cecf ce5d c54a 05ba 03a6 0403 d4a2  3v...].J........  
00002b60: e4bb b876 0dbe 7ee4 207d 480b a004 0174  ...v..~. }H....t  
00002b70: 0174 0174 0174 02e2 4072 e8da 7777 8c90  .t.t.t..@r..ww..  
00002b80: 9b8d 3a9c ee37 edc9 4137 197b 08da 2dee  ..:..7..A7.{..-.  
00002b90: f142 6e41 9f46 c6ff 0056 c788 cbfb 28b0  .BnA.F...V....(.  
00002ba0: b905 fa0c 5f27 e5d6 2ff8 a585 cb28 210c  ...._'../....(!.  
00002bb0: 6868 d83f 3752 41da 1074 d401 52fb 46f3  hh.?7RA..t..R.F.  
00002bc0: f44f b902 33ba 334d 7224 870c 8ef5 0896  .O..3.3Mr$......  
00002bd0: 5f45 a6a2 70be 2537 2b62 cd48 0400 8010  _E..p.%7+b.H....  
00002be0: 0203 97c4 d710 4b41 c26e 2e01 b1e2 3814  ......KA.n....8.  
00002bf0: 067b 5c75 69f5 dc89 8e61 1ba1 7978 0e67  .{\ui....a..yx.g  
00002c00: 291b 8f36 c5cd b8b9 16f0 246f 50d1 68ca  )..6......$oP.h.  
00002c10: c68c 759b f5f1 5254 62ba 8e39 e374 5334  ..u...RTb..9.tS4  
00002c20: 3d8e 162d 3b0f 8204 ec78 76bc 68fa 6a6a  =..-;....xv.h.jj  
00002c30: b743 485d 85a0 6305 d883 5e6e 4b5a 76d8  .CH]..c...^nKZv.  
00002c40: 0b6d be77 5466 7836 d664 3d1b abb5 5531  .m.wTfx6.d=...U1  
00002c50: 3a58 2173 d8d3 8490 5b7b dae4 35a4 ddd9  :X!s....[{..5...  
00002c60: 11b0 1da9 625c 92d4 f6cd 4fa9 7c94 3019  ....b\....O.|.0.  
00002c70: 1ae6 bdac 11bc 3da5 aec5 1dd8 4907 3cf0  ......=.....I.<.  
00002c80: dfbd 5d18 25a9 7284 11ab ea44 6c2e f040  ..].%.r....Dl..@  
00002c90: 62a0 619e 6ed3 e5bb e3dc aa49 ae63 4340  b.a.n......I.cC@  
00002ca0: 0360 c829 02a0 3b3b 2c36 9c87 c501 2dad  .`.)..;;,6....-.  
00002cb0: b000 6e52 40a8 0100 2004 0174 0080 1002  ..nR@... ..t....  
00002cc0: 00ba 00ba 0171 201b 7c4d 3d5d 9f04 1721  .....q .|M=]...!  
00002cd0: bb69 1bc7 e3b1 4127 2804 4205 4245 da2c  .i....A'(.B.BE.,  
00002ce0: 761c 8a03 21a4 681f 1bc8 1ce1 bb8d b776  v...!.h........v  
00002cf0: a8b0 2bc9 b6db 8edb 8407 ffd9            ..+.........  
  
```  
&nbsp;  
  
### Recipe: Binwalk recipe - Quality: low  
#### binwalk -e current/lhfe_binwalk_c2_finale.gif/img.jpeg --directory "current/lhfe_binwalk_c2_finale.gif/lhfe_binwalk_img.jpeg"  
```  
  
DECIMAL       HEXADECIMAL     DESCRIPTION  
--------------------------------------------------------------------------------  
0             0x0             JPEG image data, JFIF standard 1.01  
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8  
  
  
```  
&nbsp;  
  
### Recipe: Strings (Long) recipe - Quality: unknown  
#### strings current/lhfe_binwalk_c2_finale.gif/img.jpeg -n 8  
```  
f945cc88e1ee:galf  
!1!%)+...  
383-7(-.+  
%--.-------+---------------------+--------+--------  
mVS1<?&\  
kA.'p	)(  
W6NJ6;{c  
QVV>]Znsr|s  
  
```  
&nbsp;  
  
### Recipe: Strings (All) recipe - Quality: high  
#### strings current/lhfe_binwalk_c2_finale.gif/img.jpeg  
```  
JFIF  
Exif  
0232  
0100  
f945cc88e1ee:galf  
!1!%)+...  
383-7(-.+  
%--.-------+---------------------+--------+--------  
"2aq  
x2F1  
-D}&\q  
#%[3%  
KV_)*  
0|v~'  
@Qk&  
r+l|}  
U\F($k  
!)+jo  
s's[  
'y=j  
oU{oE  
7nk?  
Xh%l  
D}	I  
fNn<O  
U<5)U  
I8ph/c?  
#q\yE  
))y?  
z)Xl  
mVS1<?&\  
F7FH  
lL.r  
`{yI  
`(<>  
YcZq  
,rqi  
Ak&X  
[) P  
-oD,m  
-usD  
f:8],  
l`pU1u  
(|_%  
1mZ3  
+ZdxoFf  
8{#k  
{wYe  
*GFs  
z$ZR  
kA.'p	)(  
[##### output truncated ######]  
?#9]  
,=N6}r  
Z6cZ2  
7Giy  
RT~4  
f;.3X%  
=M%g  
u4v0[  
QVV>]Znsr|s  
:(.F  
4qU){  
Tp6#  
ATqh  
Lcp8  
#|2}W  
gB5g  
:<s9  
6vK!  
Y4-s  
UY({Wi  
.;;7|T  
~j,Z  
/r_O  
'l2}W  
kb;lL  
}2Vo  
Gog~  
gC(|  
ii.c  
=e/(Y  
[wzWm;$  
@NR@  
U%N/TmQ  
`767  
V*Uk>  
fqvd  
lq6#  
X=!RR  
<.Vk  
?7RA  
3Mr$  
%7+b  
{\ui  
tS4=  
^nKZv  
wTfx6  
U1:X!s  
;;,6  
|M=]  
  
```  
&nbsp;  
