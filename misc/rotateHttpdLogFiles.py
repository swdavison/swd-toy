#!/usr/bin/python
import sys
import os.path

# *****************************************************************
# +++ rotateHttpdLogFiles.py: Rotate, compress, purge httpd log files.
#
#  Run by cron.  Make no assumptions about PATH or other environment
#  variables.
#  
# --- *************************************************************

# ----- Set variables for log directory and basenames of access
# -----    and error logs.  They must correspond with the CustomLog
# -----    and ErrorLog settings in httpd.conf.
swenvprogs = "/home/swenv/swenv_progs"
logdir = os.path.expandvars (swenvprogs + "/logs")
elb = "error_log.httpd"
alb = "access_log.httpd"

bindir = os.path.expandvars (swenvprogs + "/bin")
actl = bindir + "/apachectl"

# ----- Exit with error message if cmd line doesn't look right.
lenSysArgv = len (sys.argv)
if lenSysArgv != 2:
    print ("Wrong number of arguments.")
    print ("Usage:  rotateHttpdLogFiles <numberToRetain>")
    sys.exit (1)

# ----- Get number of log files to retain from command line.
numToRetain = int (sys.argv[1])

# ----- If there are no log files, or if both are zero length, exit.
nothingToRotate = True
currentAccessLog = logdir + "/" + alb
currentErrorLog = logdir + "/" + elb
if os.path.exists (currentAccessLog):
    if os.path.getsize(currentAccessLog) > 0:
        nothingToRotate = False
if os.path.exists (currentErrorLog):
    if os.path.getsize(currentErrorLog) > 0:
        nothingToRotate = False
if nothingToRotate:
    print ("Nothing to do.  Exiting.")
    sys.exit (0)

# ----- Stop httpd, compress the current log files, start httpd.
shellStatus = os.system (actl + " stop")
shellStatus = os.system ("/bin/gzip " + currentAccessLog)
shellStatus = os.system ("/bin/gzip " + currentErrorLog)
shellStatus = os.system (actl + " start")

# ----- If we have log files with index numbers at the
# -----    retention number, remove them.
purgeIndex = numToRetain
accessLogToPurge = logdir + "/" + alb + "." + str(purgeIndex) + ".gz"
errorLogToPurge = logdir + "/" + elb + "." + str(purgeIndex) + ".gz"
if os.path.exists (accessLogToPurge):
    os.unlink (accessLogToPurge)
if os.path.exists (errorLogToPurge):
    os.unlink (errorLogToPurge)

# ----- Rotate the files.  Move each file to a name containing the
# -----    next higher index.  Start from the highest number and 
# -----    work down.
targetIndex = numToRetain + 1
while targetIndex > 1:
    sourceIndex = targetIndex - 1
    accessSrc = logdir + "/" + alb + "." + str(sourceIndex) + ".gz"
    accessTgt = logdir + "/" + alb + "." + str(targetIndex) + ".gz"
    errorSrc = logdir + "/" + elb + "." + str(sourceIndex) + ".gz"
    errorTgt = logdir + "/" + elb + "." + str(targetIndex) + ".gz"
    if os.path.exists (accessSrc):
        os.rename (accessSrc, accessTgt)
    if os.path.exists (errorSrc):
        os.rename (errorSrc, errorTgt)
    targetIndex = sourceIndex

# ----- Move the files we just compressed to index 1.
accessSrc = logdir + "/" + alb + ".gz"
accessTgt = logdir + "/" + alb + ".1.gz"
errorSrc = logdir + "/" + elb + ".gz"
errorTgt = logdir + "/" + elb + ".1.gz"
os.rename (accessSrc, accessTgt)
os.rename (errorSrc, errorTgt)

    


