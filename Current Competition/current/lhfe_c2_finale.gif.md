[Go back to contents](../contents.md)  
# Target: c2_finale.gif  -  Quality: high  
## Path: current/c2_finale.gif  
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
### Recipe: Binwalk recipe - Quality: medium  
#### binwalk -e current/c2_finale.gif --directory "current/lhfe_binwalk_c2_finale.gif"  
```  
  
DECIMAL       HEXADECIMAL     DESCRIPTION  
--------------------------------------------------------------------------------  
0             0x0             GIF image data, version "89a", 220 x 193  
59584         0xE8C0          JPEG image data, JFIF standard 1.01  
59614         0xE8DE          TIFF image data, big-endian, offset of first image directory: 8  
71100         0x115BC         JPEG image data, JFIF standard 1.01  
71130         0x115DA         TIFF image data, big-endian, offset of first image directory: 8  
82616         0x142B8         JPEG image data, JFIF standard 1.01  
82646         0x142D6         TIFF image data, big-endian, offset of first image directory: 8  
94132         0x16FB4         GIF image data, version "89a", 220 x 193  
153716        0x25874         JPEG image data, JFIF standard 1.01  
153746        0x25892         TIFF image data, big-endian, offset of first image directory: 8  
165232        0x28570         Zip archive data, at least v2.0 to extract, uncompressed size: 11516, name: img.jpeg  
176627        0x2B1F3         End of Zip archive, footer length: 22  
  
  
```  
&nbsp;  
  
### Recipe: Strings recipe - Quality: high  
#### strings current/c2_finale.gif  
```  
GIF89a  
NETSCAPE2.0  
imgjpeg  
y4'r  
GG<-r  
^<'>  
tS>S  
Q[lZ  
)iwW  
(JKU  
A!>w  
E;,a=  
m6A?M=  
{e)T  
1Qf#  
@r}1)  
:]$n+  
)KI	"  
yf{ZE  
+d3#2  
P$;"y  
bG0]g%q\  
&S#'  
pqEQ  
~{JS  
	?2=.  
:ld-D  
MzDr  
)IcJld/l;  
7dbj  
_|l=  
tx0K  
NL<1:  
W{fy  
_R;f  
H6qP  
e%DX  
=Nv'  
)91r^  
\/Gs  
arbX  
"AS"r  
#a!Z  
.@F-  
dbA~x  
_"QCx  
dY:i  
)>IA  
6}OjB  
T3Sy8  
A3?SY  
[##### output truncated ######]  
 QVZ  
S+u)	S  
EK[[7	0  
3iJeL$  
:rS   
1*U;  
"dQle  
DQ3B9  
T8U]  
eP#s|4K3  
7C)L@5)6  
;TR!  
BLr26  
b$$Z  
o"T|  
X;F,$  
C'7r  
g@o1  
`DV\e  
5gzk  
25no%  
io4*  
8:x:  
I)|,CYZ  
=[3)  
jn=R  
.:!O`  
T^fhr1;  
mvy,  
V/,z  
e~K,!bX  
18&p  
R!$'  
Etie{e=  
Ab+z  
wli.  
nrZ_  
!^YU  
]`/F  
E*Fx@  
KhdR  
-`9M  
K\\*  
:SR1l  
T ]b  
@O9!  
,sr`  
zcX-$  
img.jpegUT  
  
```  
&nbsp;  
