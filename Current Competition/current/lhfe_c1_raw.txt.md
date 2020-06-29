[Go back to contents](../contents.md)  
# Target: c1_raw.txt  -  Quality: unknown  
## Path: current/c1_raw.txt  
---  
## Possible flags:  
  
---  
&nbsp;  
### Recipe: File recipe - Quality: unknown  
#### file current/c1_raw.txt  
```  
current/c1_raw.txt: ASCII text, with no line terminators  
  
```  
&nbsp;  
  
### Recipe: Head recipe - Quality: unknown  
#### xxd current/c1_raw.txt | head -n 40  
```  
00000000: 4b73 7a71 6361 7320 6863 2068 7677 6720  Kszqcas hc hvwg   
00000010: 7163 6164 7368 7768 7763 6221 2056 7366  qcadshwhwcb! Vsf  
00000020: 7320 7767 2068 7673 2068 736c 6820 6863  s wg hvs hslh hc  
00000030: 2068 7673 2074 7766 6768 2076 6f7a 7420   hvs twfgh vozt   
00000040: 6374 2068 7673 2071 766f 7a7a 7362 7573  ct hvs qvozzsbus  
00000050: 3a20 6367 6279 6c79                      : cgbyly  
  
```  
&nbsp;  
  
### Recipe: Tail recipe - Quality: unknown  
#### xxd current/c1_raw.txt | tail -n 40  
```  
00000000: 4b73 7a71 6361 7320 6863 2068 7677 6720  Kszqcas hc hvwg   
00000010: 7163 6164 7368 7768 7763 6221 2056 7366  qcadshwhwcb! Vsf  
00000020: 7320 7767 2068 7673 2068 736c 6820 6863  s wg hvs hslh hc  
00000030: 2068 7673 2074 7766 6768 2076 6f7a 7420   hvs twfgh vozt   
00000040: 6374 2068 7673 2071 766f 7a7a 7362 7573  ct hvs qvozzsbus  
00000050: 3a20 6367 6279 6c79                      : cgbyly  
  
```  
&nbsp;  
  
### Recipe: Strings (Long) recipe - Quality: unknown  
#### strings current/c1_raw.txt -n 8  
```  
Kszqcas hc hvwg qcadshwhwcb! Vsfs wg hvs hslh hc hvs twfgh vozt ct hvs qvozzsbus: cgbyly  
  
```  
&nbsp;  
  
### Recipe: Strings (All) recipe - Quality: unknown  
#### strings current/c1_raw.txt  
```  
Kszqcas hc hvwg qcadshwhwcb! Vsfs wg hvs hslh hc hvs twfgh vozt ct hvs qvozzsbus: cgbyly  
  
```  
&nbsp;  
