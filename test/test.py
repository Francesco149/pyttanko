#!/usr/bin/env python

'''
test suite for pyttanko.

this is free and unencumbered software released into the public
domain. check the attached UNLICENSE or http://unlicense.org/
'''

import traceback
import sys
import pyttanko
from . import suite

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

def print_score(s):
    pyttanko.info(
        "%d +%s %dx %dx300 %dx100 %dx50 %dxmiss %gpp\n" % (
            s.id, pyttanko.mods_str(s.mods), s.max_combo, s.n300,
            s.n100, s.n50, s.nmiss, s.pp
        )
    )


def run():
    ERROR_MARGIN = 0.06
    '''pp can be off by +- 6%
    margin is actually 3x for < 100pp, 2x for 100-200,
    1.5x for 200-300'''

    p = pyttanko.parser()
    bmap = pyttanko.beatmap()
    stars = pyttanko.diff_calc()

    try:
        for s in suite.suite:
            print_score(s)

            with open("test/test_suite/%d.osu" % (s.id), "r") as f:
                p.map(f, bmap=bmap)

            stars.calc(bmap, s.mods)
            pp, _, _, _, _ = pyttanko.ppv2(
                stars.aim, stars.speed, bmap=bmap, mods=s.mods,
                n300=s.n300, n100=s.n100, n50=s.n50, nmiss=s.nmiss,
                combo=s.max_combo
            )

            margin = s.pp * ERROR_MARGIN

            if s.pp < 100:
                margin *= 3
            elif s.pp < 200:
                margin *= 2
            elif s.pp < 300:
                margin *= 1.5

            if abs(pp - s.pp) >= margin:
                pyttanko.info(
                    "failed test: got %gpp, expected %g\n" % (
                        pp, s.pp
                    )
                )

                exit(1)

    except KeyboardInterrupt:
        pass

    except FileNotFoundError:
        pyttanko.info(
            "please download the test suite by running " +
            "./download_suite\n"
        )
        sys.exit(1)

    except Exception as e:
        if p.done:
            raise
        else:
            pyttanko.info(
                "%s\n%s\n" % (traceback.format_exc(), str(p))
            )

        sys.exit(1)

