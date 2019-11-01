.. image:: https://travis-ci.org/Francesco149/pyttanko.svg?branch=master
    :target: https://travis-ci.org/Francesco149/pyttanko

osu! pp and difficulty calculator. pure python implementation of
https://github.com/Francesco149/oppai-ng

this is meant to be a standalone single-file module that's as
portable as possible using only python 2.6+ builtins with no
extra dependencies

if you need a command line interface, check out
`oppai-ng <https://github.com/Francesco149/oppai-ng>`_

if you need a more object oriented implementation, check out
`oppadc <https://github.com/The-CJ/oppadc.py>`_

usage
===========
pyttanko is a single-file module, so the simplest way to use it
is to simply drop it in your project's folder:

.. code-block:: sh

    cd my/project
    curl https://raw.githubusercontent.com/Francesco149/pyttanko/master/pyttanko.py > pyttanko.py

this way, anyone who clones your project won't have to install
pyttanko as it will be bundled

if you prefer, it's also available on pip

.. code-block:: sh

    pip install pyttanko

or you can also manually install like so:

.. code-block:: sh

    curl -L https://github.com/Francesco149/pyttanko/archive/HEAD.tar.gz -o HEAD.tar.gz
    cd pyttanko-*
    python setup.py install --user

check out

.. code-block:: sh

    pydoc pyttanko

or

.. code-block:: sh

    python -c "help('pyttanko')"

for the full documentation

minimal example:

.. code-block:: python

    #!/usr/bin/env python

    import sys
    import pyttanko as osu

    p = osu.parser()
    bmap = p.map(sys.stdin)

    stars = osu.diff_calc().calc(bmap)
    print("%g stars" % stars.total)

    pp, _, _, _, _ = osu.ppv2(stars.aim, stars.speed, bmap=bmap)
    print("%g pp" % pp)


which you can run with:

.. code-block:: sh

    cat /path/to/file.osu | ./example.py


performance
===========
pyttanko runs the test suite over 10 times slower than the original
C implementation and uses ~8 times more memory, so if you need
to batch process thousands of scores, you should consider writing
native bindings for the C version.

tests were performed on linux 4.9.38, python 2.7.10 on a i7-4790k

this is still a pretty respectable speed considering python is
interpreted

.. code-block:: sh

    $ cd ~/src/pyttanko/
    $ time -v ./run_test
    ...
        Command being timed: "./run_test"
        User time (seconds): 101.68
        System time (seconds): 0.61
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1m 42.34s
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 88688
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 631637
        Voluntary context switches: 1
        Involuntary context switches: 4116
        Swaps: 0
        File system inputs: 0
        File system outputs: 56
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

    $ cd ~/src/oppai-ng/test
    $ ./build
    $ time -v ./oppai_test
    ...
        Command being timed: "./oppai_test"
        User time (seconds): 9.09
        System time (seconds): 0.06
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0m 9.15s
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 11840
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 304
        Voluntary context switches: 1
        Involuntary context switches: 39
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

