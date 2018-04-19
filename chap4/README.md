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




## References
* [libbitcoin-explorer](https://github.com/libbitcoin/libbitcoin-explorer/wiki/)
