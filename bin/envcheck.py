#!/usr/bin/env python
#
# utility script to check that the mkenv.bat script (that creates a flask application)
# is run from C:\Users\andrew\Documents\src\python
#
import sys
if len(sys.argv) > 1:
    launchdir = sys.argv[1];
    launchdir = launchdir.split("\\")
    if len(launchdir) == 1:
        sys.exit(-1)
    elif len(launchdir) == 2:
        if (launchdir[0] == 'bin' and launchdir[1] == 'mkenv.bat'):
            sys.exit(0)
        else:
            sys.exit(-1)
    elif len(launchdir) == 3:
        if (launchdir[1] == 'bin' and launchdir[2] == 'mkenv.bat'):
            if launchdir[0] == '.':
                sys.exit(0)
            else:
                sys.exit(-1)
        else:
            sys.exit(-1)
    else:
        sys.exit(-1)
