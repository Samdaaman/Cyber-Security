[Go back to contents](../../../contents.md)  
# Target: img.jpeg  -  Quality: high  
## Path: current/c2/lhfe_binwalk_finale.gif/img.jpeg  
---  
## Possible flags:  
 - Strings recipe (Found galf in output): ``0
f945cc88e1ee:galf
!1!%)+...
383``  
 - Strings recipe (Found matching regex: [a-zA-Z0-9]{12}:[a-zA-Z0-9]{4}): ``f945cc88e1ee:galf``  
 - Strings recipe (When reversed we get: ): ``flag:ee1e88cc549f``  
  
---  
&nbsp;  
### Recipe: Binwalk recipe - Quality: low  
#### binwalk -e current/c2/lhfe_binwalk_finale.gif/img.jpeg --directory "current/c2/lhfe_binwalk_finale.gif/lhfe_binwalk_img.jpeg"  
```  
  
DECIMAL       HEXADECIMAL     DESCRIPTION  
--------------------------------------------------------------------------------  
0             0x0             JPEG image data, JFIF standard 1.01  
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8  
  
  
```  
&nbsp;  
  
### Recipe: Strings recipe - Quality: high  
#### strings current/c2/lhfe_binwalk_finale.gif/img.jpeg  
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
