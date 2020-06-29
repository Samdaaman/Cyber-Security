[Go back to contents](../contents.md)  
# Target: c4_raw.pcapng  -  Quality: high  
## Path: current/c4_raw.pcapng  
---  
## Possible flags:  
 - Strings (All) recipe (Found flag in output): ``way, my key is flag:7245e1654e7a
``  
 - Strings (All) recipe (Found matching regex: [a-zA-Z0-9]{4}:[a-zA-Z0-9]{12}): ``flag:7245e1654e7a``  
  
---  
&nbsp;  
### Recipe: File recipe - Quality: unknown  
#### file current/c4_raw.pcapng  
```  
current/c4_raw.pcapng: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 65535)  
  
```  
&nbsp;  
  
### Recipe: Head recipe - Quality: unknown  
#### xxd current/c4_raw.pcapng | head -n 40  
```  
00000000: d4c3 b2a1 0200 0400 0000 0000 0000 0000  ................  
00000010: ffff 0000 0100 0000 0401 a95e f5fa 0100  ...........^....  
00000020: 2f00 0000 2f00 0000 0100 5e0c 5c20 1c1b  /.../.....^.\ ..  
00000030: 0d9f f563 0800 4500 0021 9d9b 4000 0111  ...c..E..!..@...  
00000040: d6d8 c0a8 0083 e80c 5c20 7230 7230 000d  ........\ r0r0..  
00000050: 364a 5069 6e67 210d 01a9 5ecc 7d02 002f  6JPing!...^.}../  
00000060: 0000 002f 0000 0001 005e 0c5c 2000 1a92  .../.....^.\ ...  
00000070: 0f8b 5c08 0045 0000 21e3 9740 0001 1190  ..\..E..!..@....  
00000080: e4c0 a800 7be8 0c5c 2072 3072 3000 0d29  ....{..\ r0r0..)  
00000090: 4c50 6f6e 672e 1501 a95e f770 0000 4400  LPong....^.p..D.  
000000a0: 0000 4400 0000 0100 5e0c 5c20 1c1b 0d9f  ..D.....^.\ ....  
000000b0: f563 0800 4500 0036 d896 4000 0111 9bc8  .c..E..6..@.....  
000000c0: c0a8 0083 e80c 5c20 7230 7230 0022 3f90  ......\ r0r0."?.  
000000d0: 4772 6561 742c 2069 7420 6d75 7374 2062  Great, it must b  
000000e0: 6520 776f 726b 696e 6721 1a01 a95e 851b  e working!...^..  
000000f0: 0d00 c400 0000 c400 0000 0100 5e0c 5c20  ............^.\   
00000100: 1c1b 0d9f f563 0800 4500 00b6 2129 4000  .....c..E...!)@.  
00000110: 0111 52b6 c0a8 0083 e80c 5c20 7230 7230  ..R.......\ r0r0  
00000120: 00a2 b035 4920 666f 756e 6420 7468 6973  ...5I found this  
00000130: 206f 6c64 206d 756c 7469 6361 7374 2075   old multicast u  
00000140: 6470 2063 6861 7420 636c 6965 6e74 2074  dp chat client t  
00000150: 6861 7420 4920 6d61 6465 2066 6f72 2043  hat I made for C  
00000160: 4f4d 5032 3032 2061 2066 6577 2079 6561  OMP202 a few yea  
00000170: 7273 2062 6163 6b2c 2061 6e64 2074 686f  rs back, and tho  
00000180: 7567 6874 2069 7420 6d69 6768 7420 6265  ught it might be  
00000190: 2061 2064 6563 656e 7420 7761 7920 746f   a decent way to  
000001a0: 2073 6861 7265 206d 7920 7072 6976 6174   share my privat  
000001b0: 6520 6b65 7920 7769 7468 2079 6f75 2201  e key with you".  
000001c0: a95e 040c 0000 a100 0000 a100 0000 0100  .^..............  
000001d0: 5e0c 5c20 001a 920f 8b5c 0800 4500 0093  ^.\ .....\..E...  
000001e0: 8479 4000 0111 ef90 c0a8 007b e80c 5c20  .y@........{..\   
000001f0: 7230 7230 007f ee11 5468 6572 6520 646f  r0r0....There do  
00000200: 6573 6e27 7420 7365 656d 2074 6f20 6265  esn't seem to be  
00000210: 2061 6e79 2073 6f72 7420 6f66 2065 6e63   any sort of enc  
00000220: 7279 7074 696f 6e2c 2062 7574 2073 7572  ryption, but sur  
00000230: 656c 7920 6e6f 626f 6479 2069 7320 6c69  ely nobody is li  
00000240: 7374 656e 696e 6720 696e 2077 6865 6e20  stening in when   
00000250: 796f 7520 7772 6f74 6520 7468 6520 636f  you wrote the co  
00000260: 6465 2073 6f20 6c6f 6e67 2061 676f 2e27  de so long ago.'  
00000270: 01a9 5e9c 8a01 009d 0000 009d 0000 0001  ..^.............  
  
```  
&nbsp;  
  
### Recipe: Tail recipe - Quality: unknown  
#### xxd current/c4_raw.pcapng | tail -n 40  
```  
0418c8b0: 0021 0001 6f68 ab5e 6d90 0400 5c00 0000  .!..oh.^m...\...  
0418c8c0: 5c00 0000 1c1b 0d9f f563 ec08 6bfa 0eec  \........c..k...  
0418c8d0: 0800 4500 004e 0000 4000 4011 b8ca c0a8  ..E..N..@.@.....  
0418c8e0: 0001 c0a8 0083 ded9 0089 003a d7e2 8826  ...........:...&  
0418c8f0: 0000 0001 0000 0000 0000 2043 4b41 4141  .......... CKAAA  
0418c900: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA  
0418c910: 4141 4141 4141 4141 4141 4100 0021 0001  AAAAAAAAAAA..!..  
0418c920: 6f68 ab5e ab90 0400 7800 0000 7800 0000  oh.^....x...x...  
0418c930: ec08 6bfa 0eec 1c1b 0d9f f563 0800 45c0  ..k........c..E.  
0418c940: 006a aa23 0000 4001 4ddb c0a8 0083 c0a8  .j.#..@.M.......  
0418c950: 0001 0303 7f1d 0000 0000 4500 004e 0000  ..........E..N..  
0418c960: 4000 4011 b8ca c0a8 0001 c0a8 0083 ded9  @.@.............  
0418c970: 0089 003a d7e2 8826 0000 0001 0000 0000  ...:...&........  
0418c980: 0000 2043 4b41 4141 4141 4141 4141 4141  .. CKAAAAAAAAAAA  
0418c990: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA  
0418c9a0: 4141 4100 0021 0001 6f68 ab5e b290 0400  AAA..!..oh.^....  
0418c9b0: b000 0000 b000 0000 1c1b 0d9f f563 5460  .............cT`  
0418c9c0: 0959 11f8 0800 4500 00a2 a48b 4000 4006  .Y....E.....@.@.  
0418c9d0: 135b c0a8 009c c0a8 0083 1f49 86e8 302b  .[.........I..0+  
0418c9e0: f311 5df4 aba7 8018 00f3 5fa5 0000 0101  ..]......._.....  
0418c9f0: 080a 0027 7517 9674 61bf 1703 0300 69a1  ...'u..ta.....i.  
0418ca00: a4c4 27aa 8288 7fe5 51dc 22fc d032 e319  ..'.....Q."..2..  
0418ca10: 41c8 acad 3c7b 6f8d b3b0 975f dfc7 a6ef  A...<{o...._....  
0418ca20: ba7e a05c e192 1da1 4ea0 1b6f 53e8 73d6  .~.\....N..oS.s.  
0418ca30: ad5e 3b44 2a1c 7dab 4b81 4d12 9fb2 8389  .^;D*.}.K.M.....  
0418ca40: 3e0e fd49 bf6e c439 f08f 4965 274a 748d  >..I.n.9..Ie'Jt.  
0418ca50: 3e6e 0879 d809 3353 cd73 1067 df35 b8e2  >n.y..3S.s.g.5..  
0418ca60: 3160 7d80 0131 86a6 6f68 ab5e d090 0400  1`}..1..oh.^....  
0418ca70: 4200 0000 4200 0000 5460 0959 11f8 1c1b  B...B...T`.Y....  
0418ca80: 0d9f f563 0800 4500 0034 5c9f 4000 4006  ...c..E..4\.@.@.  
0418ca90: 5bb5 c0a8 0083 c0a8 009c 86e8 1f49 5df4  [............I].  
0418caa0: aba7 302b f37f 8010 0141 8296 0000 0101  ..0+.....A......  
0418cab0: 080a 9674 623a 0027 7517 6f68 ab5e ef9f  ...tb:.'u.oh.^..  
0418cac0: 0700 5a00 0000 5a00 0000 3333 0000 0016  ..Z...Z...33....  
0418cad0: ecb1 d748 4ad1 86dd 6000 0000 0024 0001  ...HJ...`....$..  
0418cae0: fe80 0000 0000 0000 55ca 0491 bd23 60e2  ........U....#`.  
0418caf0: ff02 0000 0000 0000 0000 0000 0000 0016  ................  
0418cb00: 3a00 0502 0000 0100 8f00 f8ae 0000 0001  :...............  
0418cb10: 0200 0000 ff02 0000 0000 0000 0000 0000  ................  
0418cb20: 0000 00fb                                ....  
  
```  
&nbsp;  
  
### Recipe: Strings (Long) recipe - Quality: unknown  
#### strings current/c4_raw.pcapng -n 8  
```  
Great, it must be working!  
5I found this old multicast udp chat client that I made for COMP202 a few years back, and thought it might be a decent way to share my private key with you"  
There doesn't seem to be any sort of encryption, but surely nobody is listening in when you wrote the code so long ago.'  
Exactly. Plus, we wanted to do encryption via a shared secret. We've got to communicate in plaintext at some point.-  
I vote 'correct horse battery staple'6  
Not hunter2?=  
EI don't think ******* is a very secure password.F  
Very funny.N  
You started it.W  
4Anyway, my key is flag:7245e1654e7a  
LGreat. Now I'll need that script you made.g  
Here you go.m  
dencrypt.py  
dencrypt.pyPK  
(	%3049cee6a95d539a8a6b335f018b14fd  
e70cb756ee16e9e1a45090264a597022  
hdCba79caba7b23a76052869a8df66e2919bcbe77aa5b6b0c13129e07285f7d54a5326aece8e7a3bd8b7f1746648ff4708a  
1216ec9e491b403b049cd768ba62690d613646a86bb096addc62d5d967967c061797e3802a33ea8c63318de7d8402f52b29975ec0f9986dd2120f6c171763323fce08d521f8d5166005276ddfc6f7a31  
854c6906332ffb3f78333aa7f2027a628bca48b2b2cbe8f2f01a448bb214d9b4  
c2d2b25b91cda61c69800c4c38a15dcf8bca48b2b2cbe8f2f01a448bb214d9b4  
d0935f7ee326ad6479afa51c055cb0369d050cfd1a697ac87e0b3130360dee3f  
(#{bfa8ffd0e9d4b53b781caf8651943fa3  
OKANNOU%N  
Archer C9 v2  
Archer C9 v2  
1.02.65.  
edge-web	dual-gslb  
edge-web	dual-gslb  
edge-web	dual-gslb  
edge-web	dual-gslb  
edge-web	dual-gslb  
edge-web	dual-gslb  
open.spotify.com  
open.spotify.com  
open.spotify.com  
$::r>yax  
Q\_14@niB  
2018&-K$  
OKANNOU%N  
Archer C9 v2  
Archer C9 v2  
1.02.65.  
R?4b:n#u'"  
*_%9E5E7C8F47989526C9BCD95D24084F6F0B27C5ED  
_googlecast  
_googlecast  
.+Chromecast-9569eea099be6d71923747fbf22da8dd  
#id=9569eea099be6d71923747fbf22da8dd#cd=658594ACE5BC795F2DC5D9D58DFEF605  
rm=04124F56BF84DCB9  
md=Chromecast  
ic=/setup/icon.png  
[##### output truncated ######]  
BT-SEARCH * HTTP/1.1  
Host: 239.192.152.143:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: 239.192.152.143:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: 239.192.152.143:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
]BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
S#M-SEARCH * HTTP/1.1  
HOST: 239.255.255.250:1900  
MAN: "ssdp:discover"  
ST: urn:dial-multiscreen-org:service:dial:1  
USER-AGENT: Google Chrome/81.0.4044.113 Windows  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
  
```  
&nbsp;  
  
### Recipe: Strings (All) recipe - Quality: high  
#### strings current/c4_raw.pcapng  
```  
\ r0r0  
6JPing!  
\ r0r0  
)LPong.  
\ r0r0  
Great, it must be working!  
\ r0r0  
5I found this old multicast udp chat client that I made for COMP202 a few years back, and thought it might be a decent way to share my private key with you"  
\ r0r0  
There doesn't seem to be any sort of encryption, but surely nobody is listening in when you wrote the code so long ago.'  
\ r0r0  
Exactly. Plus, we wanted to do encryption via a shared secret. We've got to communicate in plaintext at some point.-  
\ r0r0  
I vote 'correct horse battery staple'6  
\ r0r0  
Not hunter2?=  
\ r0r0  
EI don't think ******* is a very secure password.F  
\ r0r0  
Very funny.N  
\ r0r0  
You started it.W  
>{l@  
\ r0r0  
4Anyway, my key is flag:7245e1654e7a  
\ r0r0  
LGreat. Now I'll need that script you made.g  
\ r0r0  
Here you go.m  
\ r0r0  
dencrypt.py  
'Tyn  
?Cl-  
Ph-uo  
SO&Zh  
t>;U  
ZQZ.E  
dencrypt.pyPK  
\ r0r0  
(	%3049cee6a95d539a8a6b335f018b14fd  
\ r0r0  
e70cb756ee16e9e1a45090264a597022  
\ r0r0  
hdCba79caba7b23a76052869a8df66e2919bcbe77aa5b6b0c13129e07285f7d54a5326aece8e7a3bd8b7f1746648ff4708a  
\ r0r0  
1216ec9e491b403b049cd768ba62690d613646a86bb096addc62d5d967967c061797e3802a33ea8c63318de7d8402f52b29975ec0f9986dd2120f6c171763323fce08d521f8d5166005276ddfc6f7a31  
^dr	  
\ r0r0  
854c6906332ffb3f78333aa7f2027a628bca48b2b2cbe8f2f01a448bb214d9b4  
\ r0r0  
c2d2b25b91cda61c69800c4c38a15dcf8bca48b2b2cbe8f2f01a448bb214d9b4  
[##### output truncated ######]  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
]BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
BT-SEARCH * HTTP/1.1  
Host: [ff15::efc0:988f]:6771  
Port: 6881  
Infohash: 4b569534714088c2e22d4525ad9916132072bf07  
cookie: 3e71ece2  
Z) #  
b7,@  
OEl@  
S7-@  
47.@  
@Em@  
(En@  
/3nh  
/3nh  
S#M-SEARCH * HTTP/1.1  
HOST: 239.255.255.250:1900  
MAN: "ssdp:discover"  
MX: 1  
ST: urn:dial-multiscreen-org:service:dial:1  
USER-AGENT: Google Chrome/81.0.4044.113 Windows  
>.L[G  
T`	Y  
8	$&  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  
cT`	Y  
^;D*  
Ie'Jt  
T`	Y  
  
```  
&nbsp;  
