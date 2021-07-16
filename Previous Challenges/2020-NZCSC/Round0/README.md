# Summary of the Challenges

- Challenge 1
  - Da Vinci Code, two halves quote:
  - Rot14 got he first half of the flag
  - -234875 was converted to 2's Complement then to hex for second half of the flag
- Challenge 2
  - GIF file, run `strings file.gif | grep galf | rev`
- Challenge 3
  - JSFUCK code, when executed printed flag
- Challenge 4
  - PCAP file with some UDP packets at the start
  - Found a zip file that was transmitted - containing a decryption python script
  - Found a potiential password in the UDP stream. Used that and the python file to decyrpt the rest of the packets and get flag.
- Challenge 5
  - XCF file that had a corrupted signature
  - Updated to latest version of GIMP, fixed signature, and got flag in the image
- Challenge 6
  - Audio steg that had the strings `phrase` and `toor` visible in the spectogram. Unfortunately neither of these were the flag.
  - Used steghide with the password `toor` and got the flag.
- Challenge 7
  - SQL Maped the textbox to dump the database. Found the flag in the output.
  - Needed to set level=5 and risk=3
- Challenge 8
  - Image file with `y = 25x + 5` on it.
  - Found a string in file that looked to be rot'ed or similar.
  - Used the linear equation given `mod 26` to get the flag.

