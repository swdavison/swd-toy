#!/bin/bash
# ----- Execute this script via cron.  For example, create a file
# -----    /etc/cron.d/backUpRepository and put a line like the
# -----    following into it:
# 12 02,10,13,17 * * * swenv /home/swenv/swenv_progs/bin/backUpRepository.sh
#
# ----- That will make this backup script run four times each day: once
# -----    at two in the morning and then at 1000, 1300, and 1700.
# ----- Will those be local times or UTC times?  That depends on how
# -----    you have your root account configured.
# ----- Note that the number of backups that get preserved is set by
# -----    the "--num-backups" option.
export SWENV_PROGS=/home/swenv/swenv_progs
export HBP=$SWENV_PROGS/tools/backup/hot-backup.py
export REPODIR=/home/swenv/repositories/awips2_repo
export BKPDIR=/mnt/bkp/repo_bkp
exec $HBP --num-backups=40 $REPODIR $BKPDIR >& \
    $SWENV_PROGS/logs/backUpRepository.log


