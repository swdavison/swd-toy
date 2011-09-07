README.txt for the misc/ directory in Subversion

This directory contains miscellaneous utilities.  Eventually, most
of them should be moved to functionally-oriented directories.

Do not create subdirectories in here.  If you need to create a
subdirectory it means that you have enough files and the structure
has become clear enough so that you can create a proper functional
hierarchy in the repository.

Here is a directory of the files in this directory.  Try to keep
it up to date.

File Name		Installation directory or comment.  Where the
			installation directory path is relative, it 
			is relative to $SWENV_PROGS

backUpRepository.sh	local/bin/
backupTrac.py		local/bin/
crontab.swenv		Install as crontab for user swenv
handbook.hudson		"Execute shell" for Hudson build of Handbook
httpd.conf		conf/
httpd.swenv		/etc/rc.d/init.d
hudson.swenv		/etc/rc.d/init.d
README.txt		This file.  Does not get installed.
rotateHttpdLogFiles.py	local/bin/
rotateHudsonLogFiles.py	local/bin/
startHudson.sh		local/bin/
stopHudson.sh		local/bin/
svn-access-file		conf/

