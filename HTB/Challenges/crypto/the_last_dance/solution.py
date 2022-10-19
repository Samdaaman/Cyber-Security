from Crypto.Util.strxor import strxor


iv = bytes.fromhex('c4a66edfe80227b4fa24d431')
message_ct = bytes.fromhex('7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990')
flag_ct = bytes.fromhex('7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7')

message_pt = b"Our counter agencies have intercepted your messages and a lot "
message_pt += b"of your agent's identities have been exposed. In a matter of "
message_pt += b"days all of them will be captured"

key_stream = strxor(message_pt, message_ct)

flag = strxor(key_stream[:len(flag_ct)], flag_ct)
print(flag)