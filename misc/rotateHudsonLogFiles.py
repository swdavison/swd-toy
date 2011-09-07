#!/usr/bin/python
import sys
import os.path

# *****************************************************************
# +++ rotateHudsonLogFiles.py: Rotate, compress, purge hudson log files.
#
#  Runs by cron.  Make no assumptions about PATH or other environment
#  variables.
#  
# --- *************************************************************

print "Rotating Hudson logs."

# ----- Set variables for log directory and log basename.
# -----    They must be consistent with environment variables
# -----    in effect at hudson startup.  See startHudson.sh.
swenvprogs = "/home/swenv/swenv_progs"
logdir = os.path.expandvars (swenvprogs + "/logs")
lb = "hudson.log"

bindir = os.path.expandvars (swenvprogs + "/local/bin")
stophudson = bindir + "/stopHudson.sh"
starthudson = bindir + "/startHudson.sh"

# ----- Exit with error message if cmd line doesn't look right.
lenSysArgv = len (sys.argv)
if lenSysArgv != 2:
    print ("Wrong number of arguments.")
    print ("Usage:  rotateHudsonLogFiles.py <numberToRetain>")
    sys.exit (1)

# ----- Get number of log files to retain from command line.
numToRetain = int (sys.argv[1])

# ----- If there is no log file, or if it is zero length, exit.
nothingToRotate = True
currentLog = logdir + "/" + lb
if os.path.exists (currentLog):
    if os.path.getsize(currentLog) > 0:
        nothingToRotate = False
if nothingToRotate:
    print "No files to rotate.  Exiting."
    sys.exit (0)

# ----- Stop hudson, compress the current log file, start hudson.
shellStatus = os.system (stophudson)
shellStatus = os.system ("/bin/gzip " + currentLog)
shellStatus = os.system (starthudson)

# ----- If we have a log file with index number at the
# -----    retention number, remove it.
purgeIndex = numToRetain
logToPurge = logdir + "/" + lb + "." + str(purgeIndex) + ".gz"
if os.path.exists (logToPurge):
    os.unlink (logToPurge)

# ----- Rotate the files.  Move each file to a name containing the
# -----    next higher index.  Start from the highest number and 
# -----    work down.
targetIndex = numToRetain + 1
while targetIndex > 1:
    sourceIndex = targetIndex - 1
    logSrc = logdir + "/" + lb + "." + str(sourceIndex) + ".gz"
    logTgt = logdir + "/" + lb + "." + str(targetIndex) + ".gz"
    if os.path.exists (logSrc):
        os.rename (logSrc, logTgt)
    targetIndex = sourceIndex

# ----- Move the file we just compressed to index 1.
logSrc = logdir + "/" + lb + ".gz"
logTgt = logdir + "/" + lb + ".1.gz"
os.rename (logSrc, logTgt)

    


