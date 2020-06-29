[Go back to contents](../../contents.md)  
# Target: linear.png  -  Quality: high  
## Path: current/c8/linear.png  
---  
## Possible flags:  
 - Strings recipe (Found matching regex: [a-zA-Z0-9]{4}:[a-zA-Z0-9]{12}): ``aufz:menrtgzjrihm``  
 - Strings recipe (When Affine decrypted with a=25 and b=5 we got:): ``flag:tbsomzgwoxyt``  
  
---  
&nbsp;  
### Recipe: Binwalk recipe - Quality: low  
#### binwalk -e current/c8/linear.png --directory "current/c8/lhfe_binwalk_linear.png"  
```  
  
DECIMAL       HEXADECIMAL     DESCRIPTION  
--------------------------------------------------------------------------------  
0             0x0             PNG image, 500 x 100, 8-bit/color RGBA, non-interlaced  
  
  
```  
&nbsp;  
  
### Recipe: Strings recipe - Quality: high  
#### strings current/c8/linear.png  
```  
IHDR  
1CIDATx  
,   Ei  
A@#   
VU%",  
}T-[  
#5=K  
T-,64  
mUmmm  
&o&O  
UWW{=z  
~t0G  
h'v#  
cn#:  
_>,)  
oqEDO  
ZBc6  
M}'4<  
!wK,  
X@,4  
2:=7  
v8=r  
O!'!9  
eSl|  
uL`u  
MZDe~  
4f[c  
h90e  
H\HK_  
PHrX  
9% !  
WSSc  
R$lP  
)m.8  
f}f]%  
	4T)  
F$W^  
M\2-  
Jr9I  
E],b  
<USS  
u7G{*!p  
/'1p  
;RYd  
uMar  
WiZhL  
PX4G<  
6 vm  
jgit  
5f%I  
?}]7G  
[##### output truncated ######]  
w{O>  
?gzhA  
t'5pc   
.@gGM  
:USS  
x^k\  
|Sq4  
{`/t  
h4&~  
1Lz`  
s.%a^J)  
~8zi  
Kcpn  
/oZn  
$^`>\o  
I<P	  
Sib;  
{NQ5&  
#7~#  
+%$r  
eYzEC  
:(xY  
&DK>  
c='H  
[ll^  
g~F^m  
6<aEN1Q  
w]om  
UUf	  
6|XY:r`  
%F4Z  
cOw7  
n{0ZiQ  
C=Xm  
M=ry  
78BT  
;uV'  
RX*/  
33E]  
T]]]^  
Jgye  
8Tom  
vA'!  
#U;`  
OPXY  
^#i'1  
J@2+  
IEND  
aufz:menrtgzjrihm  
  
```  
&nbsp;  
