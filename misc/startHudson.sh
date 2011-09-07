#!/bin/bash
export SWENV_PROGS=$HOME/swenv_progs
export HUDSON_WAR=$SWENV_PROGS/bin/hudson.war
export HUDSON_LOG=$SWENV_PROGS/logs/hudson.log
export HUDSON_HOME=$HOME/hudson_home
export HUDSON_PORT=9080
export JAVA_HOME=/awips2/java
export JAVA=$JAVA_HOME/bin/java
nohup nice $JAVA -jar $HUDSON_WAR --httpPort=$HUDSON_PORT >> \
    $HUDSON_LOG 2>> $HUDSON_LOG &


