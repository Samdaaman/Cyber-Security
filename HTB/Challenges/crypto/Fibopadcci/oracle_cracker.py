from abc import abstractmethod
from icecream import ic


class OracleCracker:
    def __init__(self, block_size: int = 16):
        self.block_size = block_size

    @abstractmethod
    def call_oracle(self, ct_block: bytes, iv: bytes) -> bool:
        pass

    @abstractmethod
    def get_pad_byte(self, padding_index: int, padding_len: int) -> int:
        pass

    def crack_block(self, ct_block: bytes, iv: bytes) -> bytes:
        pt = b''
        pre_xor_bytes = b'' 

        for i in range(self.block_size - 1, -1, -1):
            oracle_results = [False] * 256  # list of results after calling the oracle
            before = iv[:i]  # bytes before the bruteforced character
            padding_len = self.block_size - i  # (includes bruteforced char)
            after = bytes([self.get_pad_byte(j, padding_len) for j in range(1, padding_len)])  # bytes after the bruteforced character
            after = self.xor(after, pre_xor_bytes)  # XOR with decryption output (before XOR phase in CBC)

            padding_byte = self.get_pad_byte(0, padding_len)  # correct padding byte

            for b in range(256):
                iv_test = before + bytes([b]) + after
                oracle_results[b] = self.call_oracle(ct_block, iv_test)

            if oracle_results.count(True) == 2:
                # if the CT was correctly padded to start with, ignore the case where it was correctly padded (when b == iv[i])
                oracle_results[iv[i]] = False

            assert oracle_results.count(True) == 1, f"Oracle returned {oracle_results.count(True)} True's: should only return True once per 256 bit iteration"

            b_correct = oracle_results.index(True)
            pre_xor_byte = padding_byte ^ b_correct
            pre_xor_bytes = bytes([pre_xor_byte]) + pre_xor_bytes
            pt_byte = pre_xor_byte ^ iv[i]
            pt = bytes([pt_byte]) + pt
        
        return pt

    def crack(self, ct: bytes, iv: bytes) -> bytes:
        assert len(ct) % self.block_size == 0, "cipher text must be a multiple of block size"
        assert len(iv) == self.block_size, "iv must be the same length as block size"
        
        pt = b''

        for i in range(0, len(ct), self.block_size):
            ct_block = ct[i: i + self.block_size]
            if i > 0:
                iv = ct[i-16: i]
            pt_block = self.crack_block(ct_block, iv)
            pt += pt_block

        return pt


    def xor(self, a: bytes, b: bytes):
        assert len(a) == len(b), "lengths must match"
        return bytes([(i ^ j) % 256 for i, j in zip(a, b)])