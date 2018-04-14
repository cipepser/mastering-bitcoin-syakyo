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

いくつかerrorが出た。

```sh
configure: error: libdb_cxx headers missing, Bitcoin Core requires this library for wallet functionality (--disable-wallet to disable wallet functionality)
```
これも含めて先に依存関係があるツールは入れておいたほうがいい。

```sh
brew install automake berkeley-db4 libtool boost miniupnpc openssl pkg-config protobuf python qt libevent qrencode
```

うまくいくと以下のようになる。

```sh
❯ ./configure
checking build system type... x86_64-apple-darwin17.5.0
checking host system type... x86_64-apple-darwin17.5.0
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... build-aux/install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether to enable maintainer-specific portions of Makefiles... yes
checking whether make supports nested variables... (cached) yes
checking for g++... g++
checking whether the C++ compiler works... yes
checking for C++ compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of g++... gcc3
checking whether g++ supports C++11 features with -std=c++11... yes
checking whether std::atomic can be used without link library... yes
checking whether we are using the GNU Objective C++ compiler... yes
checking whether g++ -std=c++11 accepts -g... yes
checking dependency style of g++ -std=c++11... gcc3
checking how to print strings... printf
checking for gcc... gcc
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking dependency style of gcc... gcc3
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /Library/Developer/CommandLineTools/usr/bin/ld
checking if the linker (/Library/Developer/CommandLineTools/usr/bin/ld) is GNU ld... no
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 196608
checking how to convert x86_64-apple-darwin17.5.0 file names to x86_64-apple-darwin17.5.0 format... func_convert_file_noop
checking how to convert x86_64-apple-darwin17.5.0 file names to toolchain format... func_convert_file_noop
checking for /Library/Developer/CommandLineTools/usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ar... ar
checking for archiver @FILE support... no
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /bin/dd
checking how to truncate binary pipes... /bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking for dsymutil... dsymutil
checking for nmedit... nmedit
checking for lipo... lipo
checking for otool... otool
checking for otool64... no
checking for -single_module linker flag... yes
checking for -exported_symbols_list linker flag... yes
checking for -force_load linker flag... yes
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... yes
checking for gcc option to produce PIC... -fno-common -DPIC
checking if gcc PIC flag -fno-common -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin17.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -std=c++11 -E
checking for ld used by g++ -std=c++11... /Library/Developer/CommandLineTools/usr/bin/ld
checking if the linker (/Library/Developer/CommandLineTools/usr/bin/ld) is GNU ld... no
checking whether the g++ -std=c++11 linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking for g++ -std=c++11 option to produce PIC... -fno-common -DPIC
checking if g++ -std=c++11 PIC flag -fno-common -DPIC works... yes
checking if g++ -std=c++11 static flag -static works... no
checking if g++ -std=c++11 supports -c -o file.o... yes
checking if g++ -std=c++11 supports -c -o file.o... (cached) yes
checking whether the g++ -std=c++11 linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin17.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking for ar... /usr/bin/ar
checking for ranlib... /usr/bin/ranlib
checking for strip... /usr/bin/strip
checking for gcov... /usr/bin/gcov
checking for lcov... no
checking for python3.6... no
checking for python3.5... no
checking for python3.4... no
checking for python3... no
checking for python2.7... /usr/local/bin/python2.7
checking for genhtml... no
checking for git... /usr/local/bin/git
checking for ccache... no
checking for xgettext... no
checking for hexdump... /usr/bin/hexdump
checking for readelf... no
checking for c++filt... /usr/bin/c++filt
checking for objcopy... no
checking whether C++ compiler accepts -Werror... yes
checking whether C++ compiler accepts -Wall... yes
checking whether C++ compiler accepts -Wextra... yes
checking whether C++ compiler accepts -Wformat... yes
checking whether C++ compiler accepts -Wvla... yes
checking whether C++ compiler accepts -Wformat-security... yes
checking whether C++ compiler accepts -Wunused-parameter... yes
checking whether C++ compiler accepts -Wself-assign... yes
checking whether C++ compiler accepts -Wunused-local-typedef... yes
checking whether C++ compiler accepts -Wdeprecated-register... yes
checking for port... no
checking for rsvg-convert... no
checking for rsvg... no
checking for brew... brew
checking whether the linker accepts -Wl,-headerpad_max_install_names... yes
checking for pkg-config... /usr/local/bin/pkg-config
checking pkg-config is at least version 0.9.0... yes
checking whether byte ordering is bigendian... no
checking whether gcc is Clang... yes
checking whether Clang needs flag to prevent "argument unused" warning when linking with -pthread... no
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking whether more special flags are required for pthreads... no
checking for PTHREAD_PRIO_INHERIT... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether strerror_r is declared... yes
checking for strerror_r... yes
checking whether strerror_r returns char *... no
checking whether the linker accepts -Wl,--large-address-aware... no
checking for __attribute__((visibility))... no
checking for __attribute__((dllexport))... no
checking for __attribute__((dllimport))... no
checking for library containing clock_gettime... none required
checking whether C++ compiler accepts -fPIC... yes
checking whether C++ compiler accepts -Wstack-protector... yes
checking whether C++ compiler accepts -fstack-protector-all... yes
checking whether C++ preprocessor accepts -D_FORTIFY_SOURCE=2... yes
checking whether C++ preprocessor accepts -U_FORTIFY_SOURCE... yes
checking whether the linker accepts -Wl,--dynamicbase... no
checking whether the linker accepts -Wl,--nxcompat... no
checking whether the linker accepts -Wl,--high-entropy-va... no
checking whether the linker accepts -Wl,-z,relro... no
checking whether the linker accepts -Wl,-z,now... no
checking whether C++ compiler accepts -fPIE... yes
checking whether the linker accepts -pie... yes
checking whether the linker accepts -Wl,-dead_strip... yes
checking endian.h usability... no
checking endian.h presence... no
checking for endian.h... no
checking sys/endian.h usability... no
checking sys/endian.h presence... no
checking for sys/endian.h... no
checking byteswap.h usability... no
checking byteswap.h presence... no
checking for byteswap.h... no
checking stdio.h usability... yes
checking stdio.h presence... yes
checking for stdio.h... yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for strings.h... (cached) yes
checking for sys/types.h... (cached) yes
checking for sys/stat.h... (cached) yes
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/prctl.h usability... no
checking sys/prctl.h presence... no
checking for sys/prctl.h... no
checking whether strnlen is declared... yes
checking whether daemon is declared... yes
checking whether le16toh is declared... no
checking whether le32toh is declared... no
checking whether le64toh is declared... no
checking whether htole16 is declared... no
checking whether htole32 is declared... no
checking whether htole64 is declared... no
checking whether be16toh is declared... no
checking whether be32toh is declared... no
checking whether be64toh is declared... no
checking whether htobe16 is declared... no
checking whether htobe32 is declared... no
checking whether htobe64 is declared... no
checking whether bswap_16 is declared... no
checking whether bswap_32 is declared... no
checking whether bswap_64 is declared... no
checking for MSG_NOSIGNAL... no
checking for mallopt M_ARENA_MAX... no
checking for visibility attribute... yes
checking for Berkeley DB C++ headers... default
checking for main in -ldb_cxx-4.8... yes
checking miniupnpc/miniwget.h usability... yes
checking miniupnpc/miniwget.h presence... yes
checking for miniupnpc/miniwget.h... yes
checking for main in -lminiupnpc... yes
checking miniupnpc/miniupnpc.h usability... yes
checking miniupnpc/miniupnpc.h presence... yes
checking for miniupnpc/miniupnpc.h... yes
checking for main in -lminiupnpc... (cached) yes
checking miniupnpc/upnpcommands.h usability... yes
checking miniupnpc/upnpcommands.h presence... yes
checking for miniupnpc/upnpcommands.h... yes
checking for main in -lminiupnpc... (cached) yes
checking miniupnpc/upnperrors.h usability... yes
checking miniupnpc/upnperrors.h presence... yes
checking for miniupnpc/upnperrors.h... yes
checking for main in -lminiupnpc... (cached) yes
checking for Qt5Core Qt5Gui Qt5Network Qt5Widgets... yes
checking for Qt5Test... yes
checking for Qt5DBus... yes
checking for static Qt... no
checking whether -fPIE can be used with this Qt config... yes
checking for moc-qt5... no
checking for moc5... no
checking for moc... /usr/local/Cellar/qt/5.10.1/bin/moc
checking for uic-qt5... no
checking for uic5... no
checking for uic... /usr/local/Cellar/qt/5.10.1/bin/uic
checking for rcc-qt5... no
checking for rcc5... no
checking for rcc... /usr/local/Cellar/qt/5.10.1/bin/rcc
checking for lrelease-qt5... no
checking for lrelease5... no
checking for lrelease... /usr/local/Cellar/qt/5.10.1/bin/lrelease
checking for lupdate-qt5... no
checking for lupdate5... no
checking for lupdate... /usr/local/Cellar/qt/5.10.1/bin/lupdate
checking whether the linker accepts -framework Foundation -framework ApplicationServices -framework AppKit... yes
checking whether to build Bitcoin Core GUI... yes (Qt5)
checking for boostlib >= 1.47.0... yes
checking whether the Boost::System library is available... yes
checking for exit in -lboost_system... yes
checking whether the Boost::Filesystem library is available... yes
checking for exit in -lboost_filesystem... yes
checking whether the Boost::Program_Options library is available... yes
checking for exit in -lboost_program_options-mt... yes
checking whether the Boost::Thread library is available... yes
checking for exit in -lboost_thread-mt... yes
checking whether the Boost::Chrono library is available... yes
checking for exit in -lboost_chrono-mt... yes
checking whether the Boost::Unit_Test_Framework library is available... yes
checking for dynamic linked boost test... yes
checking for mismatched boost c++11 scoped enums... ok
checking for libssl... yes
checking for libcrypto... yes
checking for protobuf... yes
checking for libqrencode... yes
checking for libevent... yes
checking for libevent_pthreads... yes
checking for libzmq >= 4... no
configure: WARNING: libzmq version 4.x or greater not found, disabling
checking whether EVP_MD_CTX_new is declared... no
checking for protoc... /usr/local/bin/protoc
checking whether to build bitcoind... yes
checking whether to build utils (bitcoin-cli bitcoin-tx)... yes
checking whether to build libraries... yes
checking if ccache should be used... no
checking if wallet should be enabled... yes
checking whether to build with support for UPnP... yes
checking whether to build with UPnP enabled by default... no
checking whether to build GUI with support for D-Bus... yes
checking whether to build GUI with support for QR codes... yes
configure: WARNING: "xgettext is required to update qt translations"
checking whether to build test_bitcoin-qt... yes
checking whether to build test_bitcoin... yes
checking whether to reduce exports... no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating libbitcoinconsensus.pc
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating doc/man/Makefile
config.status: creating share/setup.nsi
config.status: creating share/qt/Info.plist
config.status: creating src/test/buildenv.py
config.status: creating qa/pull-tester/tests_config.py
config.status: creating contrib/devtools/split-debug.sh
config.status: creating src/config/bitcoin-config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in src/univalue (/Users/respepic/Documents/sand/mastering_bitcoin/chap3/bitcoin/src/univalue)
configure: running /bin/sh ./configure --disable-option-checking '--prefix=/usr/local'  '--disable-shared' '--with-pic' '--with-bignum=no' '--enable-module-recovery' --cache-file=/dev/null --srcdir=.
checking whether make supports nested variables... yes
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... build-aux/install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking build system type... x86_64-apple-darwin17.5.0
checking host system type... x86_64-apple-darwin17.5.0
checking how to print strings... printf
checking whether make supports the include directive... yes (GNU style)
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking dependency style of gcc... gcc3
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /Library/Developer/CommandLineTools/usr/bin/ld
checking if the linker (/Library/Developer/CommandLineTools/usr/bin/ld) is GNU ld... no
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 196608
checking how to convert x86_64-apple-darwin17.5.0 file names to x86_64-apple-darwin17.5.0 format... func_convert_file_noop
checking how to convert x86_64-apple-darwin17.5.0 file names to toolchain format... func_convert_file_noop
checking for /Library/Developer/CommandLineTools/usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ar... ar
checking for archiver @FILE support... no
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /bin/dd
checking how to truncate binary pipes... /bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking for dsymutil... dsymutil
checking for nmedit... nmedit
checking for lipo... lipo
checking for otool... otool
checking for otool64... no
checking for -single_module linker flag... yes
checking for -exported_symbols_list linker flag... yes
checking for -force_load linker flag... yes
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... yes
checking for gcc option to produce PIC... -fno-common -DPIC
checking if gcc PIC flag -fno-common -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin17.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /Library/Developer/CommandLineTools/usr/bin/ld
checking if the linker (/Library/Developer/CommandLineTools/usr/bin/ld) is GNU ld... no
checking whether the g++ linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking for g++ option to produce PIC... -fno-common -DPIC
checking if g++ PIC flag -fno-common -DPIC works... yes
checking if g++ static flag -static works... no
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin17.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating pc/libunivalue.pc
config.status: creating pc/libunivalue-uninstalled.pc
config.status: creating univalue-config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in src/secp256k1 (/Users/respepic/Documents/sand/mastering_bitcoin/chap3/bitcoin/src/secp256k1)
configure: running /bin/sh ./configure --disable-option-checking '--prefix=/usr/local'  '--disable-shared' '--with-pic' '--with-bignum=no' '--enable-module-recovery' --cache-file=/dev/null --srcdir=.
checking build system type... x86_64-apple-darwin17.5.0
checking host system type... x86_64-apple-darwin17.5.0
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... build-aux/install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking how to print strings... printf
checking whether make supports the include directive... yes (GNU style)
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking dependency style of gcc... gcc3
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /Library/Developer/CommandLineTools/usr/bin/ld
checking if the linker (/Library/Developer/CommandLineTools/usr/bin/ld) is GNU ld... no
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 196608
checking how to convert x86_64-apple-darwin17.5.0 file names to x86_64-apple-darwin17.5.0 format... func_convert_file_noop
checking how to convert x86_64-apple-darwin17.5.0 file names to toolchain format... func_convert_file_noop
checking for /Library/Developer/CommandLineTools/usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ar... ar
checking for archiver @FILE support... no
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /bin/dd
checking how to truncate binary pipes... /bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking for dsymutil... dsymutil
checking for nmedit... nmedit
checking for lipo... lipo
checking for otool... otool
checking for otool64... no
checking for -single_module linker flag... yes
checking for -exported_symbols_list linker flag... yes
checking for -force_load linker flag... yes
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... yes
checking for gcc option to produce PIC... -fno-common -DPIC
checking if gcc PIC flag -fno-common -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/Library/Developer/CommandLineTools/usr/bin/ld) supports shared libraries... yes
checking dynamic linker characteristics... darwin17.5.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking whether make supports nested variables... (cached) yes
checking for pkg-config... /usr/local/bin/pkg-config
checking pkg-config is at least version 0.9.0... yes
checking for ar... /usr/bin/ar
checking for ranlib... /usr/bin/ranlib
checking for strip... /usr/bin/strip
checking for gcc... gcc
checking whether we are using the GNU C compiler... (cached) yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... (cached) none needed
checking whether gcc understands -c and -o together... (cached) yes
checking dependency style of gcc... (cached) gcc3
checking how to run the C preprocessor... gcc -E
checking for gcc option to accept ISO C89... (cached) none needed
checking dependency style of gcc... gcc3
checking for brew... /usr/local/bin/brew
checking if gcc supports -std=c89 -pedantic -Wall -Wextra -Wcast-align -Wnested-externs -Wshadow -Wstrict-prototypes -Wno-unused-function -Wno-long-long -Wno-overlength-strings... yes
checking if gcc supports -fvisibility=hidden... yes
checking for __int128... yes
checking for __builtin_expect... yes
checking native compiler: gcc... ok
checking for x86_64 assembly availability... yes
checking for libcrypto... yes
checking for main in -lcrypto... yes
checking for EC functions in libcrypto... no
checking for javac... /usr/bin/javac
checking symlink for /usr/bin/javac... /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/javac
checking jni headers... /System/Library/Frameworks/JavaVM.framework/Versions/Current/Headers
configure: WARNING: jni headers/dependencies not found. jni support disabled
checking whether byte ordering is bigendian... no
configure: Using static precomputation: yes
configure: Using assembly optimizations: x86_64
configure: Using field implementation: 64bit
configure: Using bignum implementation: no
configure: Using scalar implementation: 64bit
configure: Using endomorphism optimizations: no
configure: Building ECDH module: no
configure: Building ECDSA pubkey recovery module: yes
configure: Using jni: no
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating libsecp256k1.pc
config.status: creating src/libsecp256k1-config.h
config.status: executing depfiles commands
config.status: executing libtool commands

Options used to compile and link:
  with wallet   = yes
  with gui / qt = yes
    qt version  = 5
    with qr     = yes
  with zmq      = no
  with test     = yes
  with bench    = yes
  with upnp     = yes
  debug enabled = no
  werror        = no

  target os     = darwin
  build os      = darwin

  CC            = gcc
  CFLAGS        = -g -O2
  CPPFLAGS      =  -DHAVE_BUILD_INFO -D__STDC_FORMAT_MACROS -I/usr/local/opt/berkeley-db@4/include -DMAC_OSX
  CXX           = g++ -std=c++11
  CXXFLAGS      = -g -O2 -Wall -Wextra -Wformat -Wvla -Wformat-security -Wno-unused-parameter -Wno-self-assign -Wno-unused-local-typedef -Wno-deprecated-register
  LDFLAGS       =  -Wl,-headerpad_max_install_names -Wl,-dead_strip
  ```











































