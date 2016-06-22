#!/usr/bin/env python3
import subprocess
from datetime import datetime

CASES = [
    ("Dash", "", "dash src/hello.bash"),
    ("Bash", "", "bash src/hello.bash"),
    ("TCC", "tcc src/hello.c -o hello.tcc", "./hello.tcc"),
    ("Python2", "", "python2 src/hello.py"),
    ("Python3", "", "python3 src/hello.py"),
    ("GCC", "gcc src/hello.c -o hello.gcc", "./hello.gcc"),
    #("cparser", "cparser src/hello.c -o hello.cparser", "./hello.cparser"),
    ("Go", "", "go run src/hello.go"),
    ("Rust", "rustc src/hello.rs -o hello.rustc", "./hello.rustc"),
    ("RDMD", "", "rdmd --force src/hello.d"),
    ("Haskell", "ghc -fforce-recomp src/hello.hs -o hello.ghc", "./hello.ghc"),
    ("DMD", "dmd src/hello.d -ofhello.dmd", "./hello.dmd"),
    ("Java", "javac src/Hello.java", "java -classpath src/ Hello"),
    ("Scala", "scalac src/Hello.scala", "java -classpath src/ Hello"),
    ("SML/mlton", "mlton -output hello.mlton src/hello.sml", "./hello.mlton"),
    ("X10 Java", "x10c src/Hello.x10", "java -classpath src/ Hello"),
    ("X10 C++", "x10c++ src/Hello.x10 -o hello.x10cpp", "./hello.x10cpp"),
    #("X10 Firm", "x10firm src/Hello.x10 -o hello.x10firm", "./hello.x10firm"),
]

def measure(cmd_compile, cmd_exec):
    start = datetime.now()
    hide = subprocess.check_output(cmd_compile, shell=True)
    out = subprocess.check_output(cmd_exec, shell=True)
    end = datetime.now()
    assert out == b"Hello World!\n", out
    return end - start

for name,cmp,exe in CASES:
    try:
        t = measure(cmp, exe)
        print("%-12s %s" % (name,t))
    except subprocess.CalledProcessError:
        #print("skipped "+name+" due to error")
        pass
