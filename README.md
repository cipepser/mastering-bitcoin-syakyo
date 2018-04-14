# Mastering Bitcoinを写経する記録

## 第3章 ビットコインクライアント

2018/04/13時点で安定バージョンの以下を使う。`git tag`で`rc`がないものが安定バージョン。

```sh
❯ git checkout v0.14.2
```

セットアップ

```sh
❯ ./autogen.sh
configuration failed, please install autoconf first
```

怒られたので`autoconf`を入れる

```sh
❯ brew install autoconf
❯ brew instal automake
```

セットアップ再挑戦。

```sh
❯ ./autogen.sh
glibtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
glibtoolize: copying file 'build-aux/ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
glibtoolize: copying file 'build-aux/m4/libtool.m4'
glibtoolize: copying file 'build-aux/m4/ltoptions.m4'
glibtoolize: copying file 'build-aux/m4/ltsugar.m4'
glibtoolize: copying file 'build-aux/m4/ltversion.m4'
glibtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:45: installing 'build-aux/compile'
configure.ac:45: installing 'build-aux/config.guess'
configure.ac:45: installing 'build-aux/config.sub'
configure.ac:28: installing 'build-aux/install-sh'
configure.ac:28: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
parallel-tests: installing 'build-aux/test-driver'
glibtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
glibtoolize: copying file 'build-aux/ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
glibtoolize: copying file 'build-aux/m4/libtool.m4'
glibtoolize: copying file 'build-aux/m4/ltoptions.m4'
glibtoolize: copying file 'build-aux/m4/ltsugar.m4'
glibtoolize: copying file 'build-aux/m4/ltversion.m4'
glibtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:10: installing 'build-aux/compile'
configure.ac:5: installing 'build-aux/config.guess'
configure.ac:5: installing 'build-aux/config.sub'
configure.ac:9: installing 'build-aux/install-sh'
configure.ac:9: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
parallel-tests: installing 'build-aux/test-driver'
glibtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
glibtoolize: copying file 'build-aux/ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
glibtoolize: copying file 'build-aux/m4/libtool.m4'
glibtoolize: copying file 'build-aux/m4/ltoptions.m4'
glibtoolize: copying file 'build-aux/m4/ltsugar.m4'
glibtoolize: copying file 'build-aux/m4/ltversion.m4'
glibtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:72: installing 'build-aux/compile'
configure.ac:22: installing 'build-aux/config.guess'
configure.ac:22: installing 'build-aux/config.sub'
configure.ac:32: installing 'build-aux/install-sh'
configure.ac:32: installing 'build-aux/missing'
Makefile.am:12: warning: user variable 'GZIP_ENV' defined here ...
/usr/local/Cellar/automake/1.16.1/share/automake-1.16/am/distdir.am: ... overrides Automake variable 'GZIP_ENV' defined here
src/Makefile.am: installing 'build-aux/depcomp'
src/Makefile.am:480: warning: user target '.mm.o' defined here ...
/usr/local/Cellar/automake/1.16.1/share/automake-1.16/am/depend2.am: ... overrides Automake target '.mm.o' defined here
parallel-tests: installing 'build-aux/test-driver'
```

```sh
❯ ./configure
```

