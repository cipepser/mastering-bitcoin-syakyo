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

## References
* [libbitcoin-explorer](https://github.com/libbitcoin/libbitcoin-explorer/wiki/)
