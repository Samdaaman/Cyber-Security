[Go back to contents](../contents.md)  
# Target: c9_caesar.txt  -  Quality: high  
## Path: current/c9_caesar.txt  
---  
## Possible flags:  
 - Strings (All) recipe (Found matching regex: [a-zA-Z0-9]{4}:[a-zA-Z0-9]{12}): ``synt:nopqrtsuvwxy``  
 - Strings (All) recipe (When Caesar shifted by 13 we got:): ``flag:abcdegfhijkl``  
 - Strings (All) recipe (When Affine decrypted with a=1 and b=13 we got:): ``flag:abcdegfhijkl``  
 - Strings (All) recipe (Found matching regex: [a-zA-Z0-9]{12}:[a-zA-Z0-9]{4}): ``gjbhjbjhsynt:nopq``  
 - Strings (All) recipe (When reversed we get: ): ``qpon:tnyshjbjhbjg``  
  
---  
&nbsp;  
### Recipe: File recipe - Quality: unknown  
#### file current/c9_caesar.txt  
```  
current/c9_caesar.txt: ASCII text  
  
```  
&nbsp;  
  
### Recipe: Head recipe - Quality: unknown  
#### xxd current/c9_caesar.txt | head -n 40  
```  
00000000: 6a6b 6164 6268 676a 6268 6a62 6a68 7379  jkadbhgjbhjbjhsy  
00000010: 6e74 3a6e 6f70 7172 7473 7576 7778 797a  nt:nopqrtsuvwxyz  
00000020: 6162 6b6a 6162 6a6b 7666 626a 6b65 7262  abkjabjkvfbjkerb  
00000030: 766a 6862 0a                             vjhb.  
  
```  
&nbsp;  
  
### Recipe: Tail recipe - Quality: unknown  
#### xxd current/c9_caesar.txt | tail -n 40  
```  
00000000: 6a6b 6164 6268 676a 6268 6a62 6a68 7379  jkadbhgjbhjbjhsy  
00000010: 6e74 3a6e 6f70 7172 7473 7576 7778 797a  nt:nopqrtsuvwxyz  
00000020: 6162 6b6a 6162 6a6b 7666 626a 6b65 7262  abkjabjkvfbjkerb  
00000030: 766a 6862 0a                             vjhb.  
  
```  
&nbsp;  
  
### Recipe: Strings (Long) recipe - Quality: unknown  
#### strings current/c9_caesar.txt -n 8  
```  
jkadbhgjbhjbjhsynt:nopqrtsuvwxyzabkjabjkvfbjkerbvjhb  
  
```  
&nbsp;  
  
### Recipe: Strings (All) recipe - Quality: high  
#### strings current/c9_caesar.txt  
```  
jkadbhgjbhjbjhsynt:nopqrtsuvwxyzabkjabjkvfbjkerbvjhb  
  
```  
&nbsp;  
