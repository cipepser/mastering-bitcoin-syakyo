# Mastering Bitcoinを写経する記録

## 第3章 ビットコインクライアント

2018/04/13時点で安定バージョンの以下を使う。`git tag`で`rc`がないものが安定バージョン。

```sh
❯ git checkout v0.16.0
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
configure.ac:28: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
glibtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
glibtoolize: copying file 'build-aux/ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
glibtoolize: copying file 'build-aux/m4/libtool.m4'
glibtoolize: copying file 'build-aux/m4/ltoptions.m4'
glibtoolize: copying file 'build-aux/m4/ltsugar.m4'
glibtoolize: copying file 'build-aux/m4/ltversion.m4'
glibtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:10: installing 'build-aux/compile'
configure.ac:9: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
glibtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
glibtoolize: copying file 'build-aux/ltmain.sh'
glibtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
glibtoolize: copying file 'build-aux/m4/libtool.m4'
glibtoolize: copying file 'build-aux/m4/ltoptions.m4'
glibtoolize: copying file 'build-aux/m4/ltsugar.m4'
glibtoolize: copying file 'build-aux/m4/ltversion.m4'
glibtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:78: installing 'build-aux/compile'
configure.ac:38: installing 'build-aux/missing'
src/Makefile.am: installing 'build-aux/depcomp'
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
checking whether C++ compiler accepts -Wthread-safety-analysis... yes
checking whether C++ compiler accepts -Wunused-parameter... yes
checking whether C++ compiler accepts -Wself-assign... yes
checking whether C++ compiler accepts -Wunused-local-typedef... yes
checking whether C++ compiler accepts -Wdeprecated-register... yes
checking whether C++ compiler accepts -Wimplicit-fallthrough... yes
checking whether C++ compiler accepts -msse4.2... yes
checking for assembler crc32 support... yes
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
checking whether __builtin_clz is declared... no
checking whether __builtin_clzl is declared... no
checking whether __builtin_clzll is declared... no
checking for MSG_NOSIGNAL... no
checking for MSG_DONTWAIT... yes
checking for getmemoryinfo... no
checking for mallopt M_ARENA_MAX... no
checking for visibility attribute... yes
checking for thread_local support... yes
checking for Linux getrandom syscall... no
checking for getentropy... no
checking for getentropy via random.h... yes
checking for sysctl KERN_ARND... no
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
config.status: creating test/config.ini
config.status: creating contrib/devtools/split-debug.sh
config.status: creating doc/Doxyfile
config.status: creating src/config/bitcoin-config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in src/univalue (/Users/respepic/Documents/sand/mastering_bitcoin/chap3/bitcoin/src/univalue)
configure: running /bin/sh ./configure --disable-option-checking '--prefix=/usr/local'  '--disable-shared' '--with-pic' '--with-bignum=no' '--enable-module-recovery' '--disable-jni' --cache-file=/dev/null --srcdir=.
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
configure: running /bin/sh ./configure --disable-option-checking '--prefix=/usr/local'  '--disable-shared' '--with-pic' '--with-bignum=no' '--enable-module-recovery' '--disable-jni' --cache-file=/dev/null --srcdir=.
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
checking whether byte ordering is bigendian... no
configure: Using static precomputation: yes
configure: Using assembly optimizations: x86_64
configure: Using field implementation: 64bit
configure: Using bignum implementation: no
configure: Using scalar implementation: 64bit
configure: Using endomorphism optimizations: no
configure: Building for coverage analysis: no
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
  use asm       = yes
  debug enabled = no
  werror        = no

  target os     = darwin
  build os      = darwin

  CC            = gcc
  CFLAGS        = -g -O2
  CPPFLAGS      =  -DHAVE_BUILD_INFO -D__STDC_FORMAT_MACROS -I/usr/local/opt/berkeley-db@4/include -DMAC_OSX
  CXX           = g++ -std=c++11
  CXXFLAGS      = -g -O2 -Wall -Wextra -Wformat -Wvla -Wformat-security -Wthread-safety-analysis -Wno-unused-parameter -Wno-self-assign -Wno-unused-local-typedef -Wno-deprecated-register -Wno-implicit-fallthrough
  LDFLAGS       =  -Wl,-headerpad_max_install_names -Wl,-dead_strip
  ARFLAGS       = cr
```

```sh
❯ make
長いので省略
```

```sh
❯ sudo make install
Making install in src
 ../build-aux/install-sh -c -d '/usr/local/lib'
 /bin/sh ../libtool   --mode=install /usr/bin/install -c   libbitcoinconsensus.la '/usr/local/lib'
libtool: install: /usr/bin/install -c .libs/libbitcoinconsensus.0.dylib /usr/local/lib/libbitcoinconsensus.0.dylib
libtool: install: (cd /usr/local/lib && { ln -s -f libbitcoinconsensus.0.dylib libbitcoinconsensus.dylib || { rm -f libbitcoinconsensus.dylib && ln -s libbitcoinconsensus.0.dylib libbitcoinconsensus.dylib; }; })
libtool: install: /usr/bin/install -c .libs/libbitcoinconsensus.lai /usr/local/lib/libbitcoinconsensus.la
libtool: install: /usr/bin/install -c .libs/libbitcoinconsensus.a /usr/local/lib/libbitcoinconsensus.a
libtool: install: chmod 644 /usr/local/lib/libbitcoinconsensus.a
libtool: install: /usr/bin/ranlib /usr/local/lib/libbitcoinconsensus.a
 ../build-aux/install-sh -c -d '/usr/local/bin'
  /bin/sh ../libtool   --mode=install /usr/bin/install -c bitcoind bitcoin-cli bitcoin-tx test/test_bitcoin bench/bench_bitcoin qt/bitcoin-qt qt/test/test_bitcoin-qt '/usr/local/bin'
libtool: install: /usr/bin/install -c bitcoind /usr/local/bin/bitcoind
libtool: install: /usr/bin/install -c bitcoin-cli /usr/local/bin/bitcoin-cli
libtool: install: /usr/bin/install -c bitcoin-tx /usr/local/bin/bitcoin-tx
libtool: install: /usr/bin/install -c test/test_bitcoin /usr/local/bin/test_bitcoin
libtool: install: /usr/bin/install -c bench/bench_bitcoin /usr/local/bin/bench_bitcoin
libtool: install: /usr/bin/install -c qt/bitcoin-qt /usr/local/bin/bitcoin-qt
libtool: install: /usr/bin/install -c qt/test/test_bitcoin-qt /usr/local/bin/test_bitcoin-qt
 ../build-aux/install-sh -c -d '/usr/local/include'
 /usr/bin/install -c -m 644 script/bitcoinconsensus.h '/usr/local/include'
Making install in doc/man
make[2]: Nothing to be done for `install-exec-am'.
 ../../build-aux/install-sh -c -d '/usr/local/share/man/man1'
 /usr/bin/install -c -m 644 bitcoind.1 bitcoin-qt.1 bitcoin-cli.1 bitcoin-tx.1 '/usr/local/share/man/man1'
make[2]: Nothing to be done for `install-exec-am'.
 build-aux/install-sh -c -d '/usr/local/lib/pkgconfig'
 /usr/bin/install -c -m 644 libbitcoinconsensus.pc '/usr/local/lib
```

インストールできたことを確認。

```sh
❯ which bitcoind
/usr/local/bin/bitcoind

❯ which bitcoin-cli
/usr/local/bin/bitcoin-cli
```

`prune`オプションを有効にして、ストレージ容量を節約する。
ただし、一度フルノードになるので時間と通信量は掛かる。
2018/04/15で、1d 4h 55m 12sで168GB程度が実績。

```sh
❯ bitcoind -prune=550
```

上記を起動した状態でJSON-RPC APIを叩く。
Mastering Bitcoinにある`getinfo`は`v0.16.0`で廃止になっている。
新コマンドは以下。

```sh
- getblockchaininfo: blocks, difficulty, chain
- getnetworkinfo: version, protocolversion, timeoffset, connections, proxy, relayfee, warnings
- getwalletinfo: balance, keypoololdest, keypoolsize, paytxfee, unlocked_until, walletversion
```

```sh
❯ bitcoin-cli getblockchaininfo
{
  "chain": "main",
  "blocks": 518319,
  "headers": 518319,
  "bestblockhash": "00000000000000000047a17be67fcd7f79432a9294d509ae168340c524ba1faf",
  "difficulty": 3839316899029.672,
  "mediantime": 1523791727,
  "verificationprogress": 0.9999984999247827,
  "initialblockdownload": false,
  "chainwork": "00000000000000000000000000000000000000000181c1c4478f4d5623bf5810",
  "size_on_disk": 523670429,
  "pruned": true,
  "pruneheight": 517751,
  "automatic_pruning": true,
  "prune_target_size": 576716800,
  "softforks": [
    {
      "id": "bip34",
      "version": 2,
      "reject": {
        "status": true
      }
    },
    {
      "id": "bip66",
      "version": 3,
      "reject": {
        "status": true
      }
    },
    {
      "id": "bip65",
      "version": 4,
      "reject": {
        "status": true
      }
    }
  ],
  "bip9_softforks": {
    "csv": {
      "status": "active",
      "startTime": 1462060800,
      "timeout": 1493596800,
      "since": 419328
    },
    "segwit": {
      "status": "active",
      "startTime": 1479168000,
      "timeout": 1510704000,
      "since": 481824
    }
  },
  "warnings": ""
}
```

```sh
❯ bitcoin-cli getnetworkinfo
{
  "version": 160000,
  "subversion": "/Satoshi:0.16.0/",
  "protocolversion": 70015,
  "localservices": "000000000000040c",
  "localrelay": true,
  "timeoffset": -2,
  "networkactive": true,
  "connections": 8,
  "networks": [
    {
      "name": "ipv4",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "ipv6",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "onion",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    }
  ],
  "relayfee": 0.00001000,
  "incrementalfee": 0.00001000,
  "localaddresses": [
    {
      "address": "省略(IPv6アドレス)",
      "port": 8333,
      "score": 1
    },
    {
      "address": "省略(IPv6アドレス)",
      "port": 8333,
      "score": 1
    },
    {
      "address": "省略(IPv6アドレス)",
      "port": 8333,
      "score": 1
    }
  ],
  "warnings": ""
}
```

```sh
❯ bitcoin-cli getwalletinfo
{
  "walletname": "wallet.dat",
  "walletversion": 159900,
  "balance": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 0.00000000,
  "txcount": 0,
  "keypoololdest": 1523680591,
  "keypoolsize": 1000,
  "keypoolsize_hd_internal": 1000,
  "paytxfee": 0.00000000,
  "hdmasterkeyid": "省略(秘匿の必要あるか不明)"
}
```

walletのセットアップ

```sh
❯ bitcoin-cli encryptwallet <PASSPHRASE>
wallet encrypted; Bitcoin server stopping, restart to run with encrypted wallet. The keypool has been flushed and a new HD seed was generated (if you are using HD). You need to make a new backup.
```

メッセージの通り、`bitcoind -prune=550`で再起動してから以下を確認。

```sh
❯ bitcoin-cli getwalletinfo
{
  "walletname": "wallet.dat",
  "walletversion": 159900,
  "balance": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 0.00000000,
  "txcount": 0,
  "keypoololdest": 1523795208,
  "keypoolsize": 1000,
  "keypoolsize_hd_internal": 1000,
  "unlocked_until": 0,
  "paytxfee": 0.00000000,
  "hdmasterkeyid": "省略(秘匿の必要あるか不明)"
}
```

`unlocked_until`が`0`になっている。この値がメモリ上にPASSPHRASEを保持する時間。
以下のように保持する秒数を指定できる。

```sh
❯ bitcoin-cli walletpassphrase YpCqGcVnUCJa3Dm68BVTcFGTPtizsmqF 360
❯ bitcoin-cli getwalletinfo
{
  "walletname": "wallet.dat",
  "walletversion": 159900,
  "balance": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 0.00000000,
  "txcount": 0,
  "keypoololdest": 1523795208,
  "keypoolsize": 1000,
  "keypoolsize_hd_internal": 1000,
  "unlocked_until": 1523795787,
  "paytxfee": 0.00000000,
  "hdmasterkeyid": "省略(秘匿の必要あるか不明)"
}
```

コマンド打つのがめんどくさいのでalias貼る。

```sh
alias bitd='bitcoind'
alias bitc='bitcoin-cli'
```

バックアップを作る。

```sh
❯ bitc backupwallet ./wallet.backup
```

インポートはpruneモードだとできないらしい。

```sh
❯ bitc importwallet ./wallet.backup
error code: -4
error message:
Importing wallets is disabled in pruned mode
```

ダンプはできる。

```sh
❯ bitc dumpwallet wallet.txt
❯ ls
wallet.backup wallet.txt
```

walletを作ってみる

```sh
❯ bitc getnewaddress
3Arphg8KpPdHYny9LsyZQRchMzTwQKzJvK
```

受け取った量を確認（送ってないので0.00000000)。最後の引数`0`を省略すると`minconf`回承認されないと残高が反映されない。

```sh
❯ bitc getreceivedbyaddress 3Arphg8KpPdHYny9LsyZQRchMzTwQKzJvK 0
0.00000000
```

txの確認

```sh
❯ bitc listtransactions
[
]
```

wallet内のアドレスの確認

```sh
❯ bitc getaddressesbyaccount ""
[
  "3Arphg8KpPdHYny9LsyZQRchMzTwQKzJvK"
]
```

wallet内の残高を確認

```sh
❯ bitc getbalance
0.00000000
```

txの探索。実行時点の適当なtxをbitcon exploreで拾ってきて確認したけど、wallet内のtxじゃないとダメっぽい。  
→`txindex`オプションを有効にしていないとwallet内のtxしか見れないらしい。
設定は`bitcoin.conf`に書く。現行バージョンでのファイルパスは[ここ](https://en.bitcoin.it/wiki/Running_Bitcoin#Bitcoin.conf_Configuration_File)にある。
でも`prune`オプションと共存できないらしい。

```sh
❯ bitc gettransaction d5e6722c3bcc1e4e08fd41302a0f0ca429fbe24e6836226382219e4a17477aaa
error code: -5
error message:
Invalid or non-wallet transaction id
```

`getrawtransaction`でhex形式のtxが見れ、`decoderawtransaction`すれば、json形式で見れる。


ブロック情報を持ってくる。
今回も適当にtxidをbitcoin exploreから持ってきた。
ちなみに`prune`モードなので、古いやつは表示できない可能性が高い。

```sh
❯ bitc getblock 00000000000000000032e49cc0d9605f921d893b75559f49eed107e772754dd5
error code: -1
error message:
Block not available (pruned data)
```

直近のブロックは持っているので、表示できるブロックを持ってくると以下のようになる。

```sh
❯ bitc getblock 00000000000000000029fffaecdb8e360da5434a2cdb2570fc66f93c6455b093
{
  "hash": "00000000000000000029fffaecdb8e360da5434a2cdb2570fc66f93c6455b093",
  "confirmations": 1,
  "strippedsize": 89389,
  "size": 100647,
  "weight": 368814,
  "height": 518549,
  "version": 536870912,
  "versionHex": "20000000",
  "merkleroot": "7244a0db792d38037224457ef10d296ca102eecaf64a569857e8b018e959386c",
  "tx": [
    "5b8b61a0f0ca0c5bd92e5e3f5e59d4baf0ad2d4bb11b0918140bedeb30f48640",
    "d8d2eda6df5a0f7d80f905402aab288004a8fb5ba62537dd98a1f78e77135168",
    ~中略~
    "dda9c54e8fe437065b3bf8bf8c916c169f570972ecb41f918d0746ce11f8a754",
    "65f9e3f4af978a2657c00447891852721c2d5f48c14a7a16212040b207d4760b"
  ],
  "time": 1523927077,
  "mediantime": 1523926513,
  "nonce": 237932355,
  "bits": "1749500d",
  "difficulty": 3839316899029.672,
  "chainwork": "00000000000000000000000000000000000000000184e4e6dc485a07b68e9d1e",
  "previousblockhash": "0000000000000000000667558dda060951bb5e137acbd9a0ceda592600e32e7e"
}
```


































## References
* [bitcoin wiki](https://en.bitcoin.it/wiki/Running_Bitcoin#Bitcoin.conf_Configuration_File)
