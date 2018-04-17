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


## References
* [libbitcoin-explorer](https://github.com/libbitcoin/libbitcoin-explorer/wiki/)
