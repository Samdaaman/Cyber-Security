from base64 import b64decode, b64encode
from operator import countOf
import requests
from icecream import ic
from Crypto.Util.asn1 import DerSequence
from Crypto.Util.number import *
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA3_512
from Crypto.Signature import DSS
from Crypto.Math.Numbers import Integer


def sig_to_r_and_s(sig: bytes):
    r_len = sig[3]
    r = int.from_bytes(sig[4:r_len+4], 'big')
    s = int.from_bytes(sig[3+1+r_len+2:], 'big')
    return r, s


def real():
    urls = [
        'https://GOODCODE/update/abcd0b64039c6eff5a1cbf50f24eb6c62f25f8f39da28fdc112433b93ada6018',
        'https://GOODCODE/update/4d4b2429f62ded41b075fcd0f0528c3b4cbd281494f04f93697dae7e1e5562f3',
        'https://GOODCODE/update/3dced7a6fe020797c7bf1e5a08a576b777aa10a8816850a1fb6661d5c97081fb',
        'https://GOODCODE/update/4469f20adeeadcc700b97da48b21f143ce524ed338754471ef2638a3921b461c',
        'https://GOODCODE/update/380fde2d3c3c28b87fabba0728ab548713823f362914ed85cfa43baeddaeff16',
        'https://GOODCODE/update/80d786fdd1a65421fd1fb43cf39edbec91f6c3dbcb94a509dc772e3f36966c1f',
        'https://GOODCODE/update/3387677bc29d24ac5072d9b25bbc49971418ee938971a13c92d7c64e03b5c9b8',
        'https://GOODCODE/update/65f3f974b29b04c6f9186084fba8470b3d5fa8cdd4461e0ce110573d19ee0a3b',
        'https://GOODCODE/update/9209e22a576ea90d3ccd38435095f5c9b4729f3624c52169f3d0a861250bc958',
        'https://GOODCODE/update/c30f4d19422b374a7624f364d245ef208847c1f19d5d939acba777ccda6e79db',
        'https://GOODCODE/update/0f763be9b51eb80c732108b9da5a4e3110565604e6693141caf28c7ffc3ae509',
        'https://GOODCODE/update/e29faae8cd5dddf2098581a0b6a7023f6e81dd83afd284488400c5a5731d228e',
        'https://GOODCODE/update/403fa90dbe63c3374b71e57e6bf02c57dd8bcc730edec9b4f64213d2b9e048b6',
        'https://GOODCODE/update/5cd5a39511980526236f50bd2a36ef6520f88ea3cfcd8d064467c8e64b563cbe',
        'https://GOODCODE/update/a4e62ce498a676179e739c1e5346049a0ba69805ecf1e16d26b2defd3f6f6931',
        'https://GOODCODE/update/f8442ff7e69b88edf9fc4d5ee48967d72602ed7e811c1164cfba69ab46ce8a32',
    ]

    signatures = [
        'MEUCIQDygJ+KOWKxMIomSm4ejoR75yQiGRebnTIecMz+vAaLZgIgFlRE1/i/oP0IrSKy/jZhEanzrFDCK8siRsELIOrGxlA=',
        'MEQCIGLKyLXEGqqprGMgZC7ZcJysCKSP0wbvRUQ++1I/H0O1AiBkf/x4XMsLoHq6VUWZaDOs4J2ZU2DXWFqhyJ5+72zg/g==',
        'MEQCIBLpxSLhwVY7xD41tUgzYjzraXxUETO01DWcuYG1oluGAiB5CkYhYlvcTXpgSTb/avuuNFo9cEK04+OsqSx6DY1vzg==',
        'MEQCIEXuMldMbZ2Arz0CQgwJoEendtNRxAoG5XnVkfcEc2yMAiA+FpL/JC8kMxchpfaTImvLpRVWE4rTK6GgNQLBZOQIPw==',
        'MEYCIQCbkzxkYSed+cO6F3EaoBF1uh1uBojdCq0EjFUyxBPyLAIhALzNUWhc2/JSjHAyUklmOgPcw98CkApS5+TvPaz6zYc2',
        'MEYCIQDl93ncrNymmNpMO18iivyJA/888doaWDDbILHm7Af6dgIhAMngUbr1aw1jjBmzr+pGSzo0F0jsNxjHY0NZvhzS5RDn',
        'MEQCIDtlg/jov1uweEYV6TYMwqp59L28AplsK+p1wBOVy/G1AiB6aEEf5i8cANK77UIrAUPxdQeaWPc1dhkbB7CkyGzzhg==',
        'MEUCICjG/d2NXFhL1Ow8dJbqy/50P7KPgWH+BxCUUHAUGmmsAiEAyrq4wGx9Vfbo1TLltseRVRiAsImRE9u+7Z9xfb6BY1c=',
        'MEYCIQDh+I/CsJFTGl1Ocdy/oKvXCPJcXhRIxYk+TMH3cYqVsQIhANnezlyV7osSfpIr5F1zJdeHVQGi9l8y1ZdrFS0L1QFV',
        'MEQCIE835xvwnLWPuigxyxunD9K3T3enFx1ptLbW5Fo64xRqAiAS3kilsPL/uESCYO6ModsTui/M1zb77yXw5+DvWG2Wgg==',
        'MEYCIQCnWKUzpH1NoQ/PMQfh3ezJIbkfHhhzLh8w9Y9tSxI6LQIhAJt9R7a996lzpFVjoREFfjxV7+98Ff4Bp+DHPy1OkEa0',
        'MEUCIQDpalsTIHHoJExe/K/nFxP65CDtPpBvPwTKDLfXMbN7tAIgThZjvBAW0Y/1VCPNGAsBOcJGYK+4DzKvpZda7wQguoo=',
        'MEQCIECGFB050hcAMVdEbifHGCBWf/RbGaW+LzMC1oStTjwIAiAjgUO03H6KoVoFHaUjjMSXN1CoDpeyECjv6DemvAbG5g==',
        'MEYCIQDl93ncrNymmNpMO18iivyJA/888doaWDDbILHm7Af6dgIhALRF93QCEXTVsPCtITYnNpXQ2dM33YvrHhfK9t4P1VGN',
        'MEYCIQCJOv4ySbAeecUF2NKLAGzM3oemf4drCp0DSphf75MvVQIhAP/IhK0yYOvnKsYq/kKJN+8NBZwwSpv6qLuqRSpUT1tB',
        'MEYCIQDy5voOPCbpBS7BbnMbr8xO/Ddq4/XH/0oaIx7akii2LAIhAMdPoN9zBpXwQ5xfixaZSd59QHmyHDDQRhLDky6axSfc',
    ]

    hashes = [
        '92282994d5ccd40eb0d4441fb7335b934be8a79e09e556bf3eb7150201c5744dff4a5aef870d9c23d9cc4375708928b1e0bd60029f71ff46f808c1f4dd1bb888',
        '91a8c00accabf6edbbc4163189d6afd87fbc1c415cf9b2cbe744cd2010775c137872782b0a8d597e414eccae852f40c127e4dc67eaf0e2be61b525da52483792',
        '698cb584a26a713cb40a9aa9a911986f005750195200d08f6630bb05dedb4c9346cddbea79818b30f92f74f7b27446202e2c7e27536b9ab8d550e92cd98d2678',
        '177a39efa8b81cb65ba439d82af0e5f152d7d126302b9d004f9f82c41978bed9449e100bb4644395001f351437d99c187104c8a6aee0701998257ed398191434',
        'f1e45854200c507a85d3c11c9e7800bb88a32649ecee0f0d7b9a05c6dc267afa3a8823e88d8fb8658c26baeff6f72db88a3a9ce2c41aef8fe2afe76d1d1d91f8',
        '5d679a84cf4cd1e42dd956a3fa69dc8a4335f7146b06d62bb5f260e18962bd39519bd53e3d42e2ec5f20ab0d18b5eaa088b286264055792d40f09820af3b0ba9',
        '70f7e6b5f698e3e71f04958898bde673dd787ff781a87174181ff387ad8cd15eb261c508f7e254d674fde7a1f417b8ae7b3934c8732afab3e6916f913a5c4b3d',
        'a18af5d2285a0e1d0ac20c6d1b2433be943ccda1378d9162cf88611449e14dd4a1dce0af8d744f96d39ffcdd564ea3359d4fc30c6b99830365a67bb75ef5c9e1',
        '3d2596188765d2eae628172707f6967a6cb6eea8de7759322d0bdcd75316db3adf63d50637886deaea8e2b6661e7ea4f861b580fe9d9e6ca0a3f2849a9540222',
        'f5c5805315861a04d5bc12697631669d8ee450279bd33c679a6cb438e23faf9b660b0738f663f27fb249bc8cbf57d95820a4149baab03d9368edafc508070434',
        '7a77aa3fd94c98329ef9601060ac6dcedb774a0b9d364f245ab26e4c7da815a7cb0671cdb7d0233de953f011f73c298cfa604989064756e84f68f13c4a08081c',
        '73996c549f21129ad847cc069b0a0c059fe43e0cf9f210ad63d1936320094c9ada294608d1a1820f9e4a9cdbc17ff8b20751a6007da9b3680018888c16b08ff3',
        '2b897180cd1473bc5c71fb8d72d0c2aa306498fa2a3dce30ece6b536725d66f84b210bee620669ac94afcfb7af3635ada8fb30dec43f3f236ccbb532d8eca866',
        '0c9d0e2d72d32dbd80a5a48591153533d82ddc8115dc85eb8954ccd0b3a7fec58d1c1639dee25c226ab0d8e5c683b45e4872c77918400549258dc3ab2abd1469',
        '9a4c67e0ab3f577bf673b35b0baede7713391e69bad6e47cb4e7d86d71910ae2c65ff44f017e6f4632ddc5ca87fbefedf6b765c6bba3fbf9b3bdf5f24d9630cc',
        '4d364fda97aa5c226b7038fec0e28063ab8bc5800df52d331d3344505ceaaa29bfa0a605b135922190503b4d3a05a08df1ba0222f5e0e91fb852dfeb8ef271e7',
    ]

    def get_hash(url: str):
        r = requests.post('http://localhost:1337/update.cgi', data={'url': url, 'signature': '1'})
        url_hash = bytes.fromhex(r.text.split('URL hash: ')[1].split('\n')[0])
        return url_hash

    results = []
    for sig_b64 in signatures:
        sig = b64decode(sig_b64)
        results.append(sig_to_r_and_s(sig))

    duplicates = []
    for i, (r, s) in enumerate(results):
        if countOf([x[0] for x in results], r) > 1:
            duplicates.append((i, urls[i], b64decode(signatures[i]), hashes[i], r, s))

    i1, url1, sig1, hash1, r, s1 = duplicates[0]
    i2, url2, sig2, hash2, _, s2 = duplicates[1]

    # ic(i1, url1, sig1, hash1, r, s1)
    # ic(i2, url2, sig2, hash2, r, s2)


def test():
    hash1 = SHA3_512.new('123'.encode('latin1'))
    hash2 = SHA3_512.new('456'.encode('latin1'))

    k = 1
    def fixed_rng(l):
        return long_to_bytes(k).rjust(256, b'\x00')[:l]
    with open("app/secp256r1.key") as f:
        key = ECC.import_key(f.read())
    signer = DSS.new(key, 'fips-186-3', 'der', fixed_rng)
    sig1_test = signer.sign(hash1)
    r1_test, s1_test = sig_to_r_and_s(sig1_test)

    curve = ECC._curves['secp256r1']
    d = Integer(100447431826117939756205300033724007590664926705564045061635354585427798206739)
    h1 = Integer(bytes_to_long(hash1.digest()[:32]))
    k_inv = Integer(k).inverse(curve.order)
    ic(key)
    r1 = int((curve.G * k).x % curve.order)
    s1 = int(k_inv * (h1 + d * r1) % curve.order)
    assert r1 == r1_test
    assert s1 == s1_test
    
    sig2 = signer.sign(hash2)
    r2, s2 = sig_to_r_and_s(sig2)
    assert r1 == r2

    attack(hash1.hexdigest(), hash2.hexdigest(), r1, s1, s2)
    

def attack(hash1: str, hash2: str, r: int, s1: int, s2: int):
    h1 = bytes_to_long(bytes.fromhex(hash1)[:32])
    h2 = bytes_to_long(bytes.fromhex(hash2)[:32])
    ic(h1)
    ic(h2)

    curve = ECC._curves['secp256r1']
    n = int(curve.order)

    k = int(Integer(s1 - s2).inverse(n)) * (h1 - h2)
    r_inv = int(Integer(r).inverse(n))

    d = r_inv * (k * s1 - h1) % n
    ic(d)

    bad = 'https://EVILCODE/'
    bad_h = bytes_to_long(SHA3_512.new(bad.encode('latin1')).digest()[:32])
    k_inv = int(Integer(k).inverse(n))
    s = (bad_h + d * r) * k_inv % n
    ic(r)
    ic(s)
    
    sig = DerSequence((r, s)).encode()
    ic(sig.hex())
    ic(b64encode(sig).decode())


def main():
    test()
    

if __name__ == '__main__':
    main()
