# 第4章 鍵、アドレス、ウォレット

libbitcoin-explorerの[DLページ](https://github.com/libbitcoin/libbitcoin-explorer/wiki/Download-BX)からOSX版を落とす。
パスを通してもいいけど、いったんchap4の中だけで触る前提で進める。

```sh
❯ mv bx-osx-x64-qrcode bx
❯ chmod 744 bx
```

秘密鍵の生成

```sh
❯ ./bx seed | ./bx ec-new | ./bx ec-tg++o-wif
// 秘密鍵が表示される
```

表示された秘密鍵は、圧縮WIF形式(Lから始まっており、suffixとして0x01を追加してBase58CHeckエンコーディングしたもの)で以下のようにするとhexで見れる。

```sh
❯ ./bx wif-to-ec <秘密鍵 圧縮WIF形式>
// hexの秘密鍵が表示される
```

圧縮されていないWIFは以下でデコードできる。

```sh
❯ ./bx base58check-decode <秘密鍵 圧縮WIF形式>
wrapper
{
    checksum 1086419139
    payload <hex 秘密鍵>
    version 128
}
```

逆にエンコードするときは以下。`128`はversion prefix

```sh
❯ ./bx base58check-encode <hex 秘密鍵> --version 128
// 圧縮WIF形式の秘密鍵が表示される
```

pybitcointoolsを使って秘密鍵の生成からBitcoin Addressの作成まで。
先に以下をインストール。

```sh
❯ pip install bitcoin
```

```python
import bitcoin

valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < bitcoin.N

print "Private Key (hex) is: ", private_key
print "private Key (decimal) is: ", decoded_private_key

wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print "Private Key (WIF) is: ", wif_encoded_private_key

compressed_private_key = private_key + '01'
print "Private Key Compressed (hex) is: ", compressed_private_key

wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
print "Public Private Key (WIF-Compressed) is: ", wif_compressed_private_key

public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print "Public Key (x,y) coordinates is: ", public_key

hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print "Public Key (hex) is: ", hex_encoded_public_key

(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
    compressed_prefix = '02'
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print "Compressed Public Key (hex) is: ", hex_compressed_public_key

print "Bitcoin Address (b58check) is: ", bitcoin.pubkey_to_address(public_key)

print "Compressed Bitcoin Address (b58check) is: ", \
    bitcoin.pubkey_to_address(hex_compressed_public_key)
```

実行すると以下のようになる。毎回ランダムで秘密鍵を生成しているので結果は異なるが、suffixや各フォーマットのprefixは同じになる。

```sh
Private Key (hex) is:  b457cb514aee10ef220a4439995f1a0f215b20b12c55cd82a17201fa2d1bfb5c
private Key (decimal) is:  81571431685778792184227295726627626480566101607618562145556148059429505071964
Private Key (WIF) is:  5KBiCZ8QW5Zk3GjbnvEX995fWunpZ3RbxbiftFWCyCGpFEciRPt
Private Key Compressed (hex) is:  b457cb514aee10ef220a4439995f1a0f215b20b12c55cd82a17201fa2d1bfb5c01
Public Private Key (WIF-Compressed) is:  L3GGqzogjM9Wy2T2Zfxg2vfb121EtRhbJQEvdD1uq2koXQDGW3Bp
Public Key (x,y) coordinates is:  (58267297018440033530326923729234301977737564316099172296358591600257564791929L, 109112151528072890448107021346230180838035048850803743098219832131836667287791L)
Public Key (hex) is:  0480d21f14d8e7bfe636dcd56225a392116ec1370b53d1b64c10e81b472405d479f13b4a0ba06cb79b44a86886c3b43195a99034c33ca17cca20b525810da4d8ef
Compressed Public Key (hex) is:  0380d21f14d8e7bfe636dcd56225a392116ec1370b53d1b64c10e81b472405d479
Bitcoin Address (b58check) is:  16LvcQx1xbESn8uquG26TWhmSUEptcG8Fr
Compressed Bitcoin Address (b58check) is:  1JZuSgTijdEL6RK1tUkmksxrbz61MmFV8k
```

次に[Secp256k1](https://en.bitcoin.it/wiki/Secp256k1)の楕円曲線で遊んでみる。
パラメータも上記リンクにある(コピペできる)。

```python
import ecdsa
import os
from ecdsa.util import string_to_number, number_to_string

_p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
_r=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
_b=0x0000000000000000000000000000000000000000000000000000000000000007L
_a=0x0000000000000000000000000000000000000000000000000000000000000000L
_Gx=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
_Gy=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8L

curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)
old_secp256k1 = (1, 3, 132, 0, 10)
SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, old_secp256k1)
ec_order = _r

curve = curve_secp256k1
generator = generator_secp256k1

def random_secret():
    convert_to_int = lambda array: int("".join(array).encode("hex"), 16)
    byte_array = os.urandom(32)
    
    return convert_to_int(byte_array)

def get_point_pubkey(point):
    if point.y() & 1:
        key = '03' + '%064x' % point.x()
    else:
        key = '02' + '%064x' % point.x()
    return key.decode('hex')

def get_point_uncompressed(point):
    key = '04' + '%064x' % point.x() + '%064x' % point.y()
    return key.decode('hex')

secret = random_secret()
print "Secret: ", secret

point = secret * generator
print "EC point: ", point

print "BTC public key: ", get_point_pubkey(point).encode('hex')

point1 = ecdsa.ellipticcurve.Point(curve, point.x(), point.y(), ec_order)
assert point1 == point
```

実行結果

```sh
Secret:  56869471220463491038010591534043434331348000118931540949271452746364952529379
EC point:  (100329234455886164789099046941675396348038955027986496187259362480712577288216,97057135012951096800461757946404241174912348190292225552012224403248824367829)
BTC public key:  03ddd055976015d76ddb7994fcec3f24f2e3de21903236ab3e99c200f5d8258818
```


## References
* [libbitcoin-explorer](https://github.com/libbitcoin/libbitcoin-explorer/wiki/)
* [Secp256k1 - bitcoinwiki](https://en.bitcoin.it/wiki/Secp256k1)