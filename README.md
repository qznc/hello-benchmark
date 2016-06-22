# Hello Benchmark

Measure time for compile+execute of Hello World in various languages.
The goal is get a sense of speed of iteration for the languages.

Here is the current output on my machine,
but please test yourself:

```
Dash         0:00:00.002366
Bash         0:00:00.002474
TCC          0:00:00.007044
Python2      0:00:00.009881
Python3      0:00:00.015547
GCC          0:00:00.028578
Go           0:00:00.149691
Rust         0:00:00.212053
RDMD         0:00:00.275884
Haskell      0:00:00.310539
DMD          0:00:00.311102
Java         0:00:00.596517
Scala        0:00:01.917606
X10 Java     0:00:02.484673
X10 C++      0:00:03.887826
```

Hello World is not representative.
Ideas for different programs are welcome.
Requirements:

* Don't really measure run time.
  The reason I include the execution time is that you cannot
  separate it for languages like Python or Java.

* Code should be "canonical" and "idiomatic" for each language.
  For example, don't use "puts" to make C compile faster.

* Task should be easy and straightforward,
  so we don't need language experts to write the programs.

Another objection could be that some languages provide continuous compilation,
where you don't have to recompile the whole program,
but only parts that changed.
I believe Lisp invented this.
Any idea how to measure this?
I don't want to require Eclipse to test Java.
We could even go one step further
and not even stop the program.
This more of a feature than a benchmark, though.
