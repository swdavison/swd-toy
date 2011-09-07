#!/usr/bin/python
import os.path
import shutil
import sys

# *****************************************************************
# +++ backupTrac.py: Back up trac.  Rotate and compress backups.
#
#  This script runs by cron.  Make no assumptions about PATH, other
#  environment variables.
#  
# --- *************************************************************

print "Backing up awips2trac project."

# ----- Set variables for project directory and backup directory.
swenvprogs = "/home/swenv/swenv_progs"
projectdir = os.path.expandvars (swenvprogs + "/tracprojects/awips2trac")
backupdirdir = "/mnt/bkp/trac_bkp"
backupdirbasename = "awips2trac"

# ----- Exit with error message if cmd line doesn't look right.
lenSysArgv = len (sys.argv)
if lenSysArgv != 2:
    print "Bad command line.  Usage: backupTrac.py <numberOfBackupsToRetain>"
    sys.exit (1)

# ----- Get number of backups to retain from command line.
numToRetain = int (sys.argv[1])

# ----- If we have a backup file with index number at the
# -----    retention number, remove it.
purgeIndex = numToRetain
bkpToPurge = \
    backupdirdir + "/" + backupdirbasename + "." + str(purgeIndex) + ".tgz"
if os.path.exists (bkpToPurge):
    os.unlink (bkpToPurge)

# ----- Rotate the files.  Move each file to a name containing the
# -----    next higher index.  Start from the highest number and 
# -----    work down.
targetIndex = numToRetain + 1
while targetIndex > 1:
    sourceIndex = targetIndex - 1
    bkpSrc = \
        backupdirdir + "/" + backupdirbasename + "." + str(sourceIndex) + ".tgz"
    bkpTgt = \
        backupdirdir + "/" + backupdirbasename + "." + str(targetIndex) + ".tgz"
    if os.path.exists (bkpSrc):
        os.rename (bkpSrc, bkpTgt)
    targetIndex = sourceIndex

# ----- Move the previous backup to index 1.
bkpSrc = backupdirdir + "/" + backupdirbasename + ".tgz"
bkpTgt = backupdirdir + "/" + backupdirbasename + ".1.tgz"
if os.path.exists (bkpSrc):
    os.rename (bkpSrc, bkpTgt)

# ----- Make a new backup.
backuppathname = backupdirdir + "/" + backupdirbasename
tracadminCmd = \
    swenvprogs + "/bin/trac-admin " + projectdir + " hotcopy " + backuppathname
shellStatus = os.system (tracadminCmd)
if shellStatus != 0:
    errormsg = "Command \"" + tracadminCmd + \
        "\" returned nonzero status: " + str(shellStatus)
    print errormsg

# ----- Tar and compress it.
os.chdir (backupdirdir)
tarballname = backupdirbasename + ".tgz"
tarzCmd = "/bin/tar zcf " + tarballname + " " + backupdirbasename
shellStatus = os.system (tarzCmd)
if shellStatus != 0:
    errormsg = "Command \"" + tarzCmd + \
        "\" returned nonzero status: " + str(shellStatus)
    print errormsg


# ----- Remove the backup directory.
shutil.rmtree (backupdirbasename)

