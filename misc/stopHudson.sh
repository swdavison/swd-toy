#!/bin/bash
kill `ps -ef | grep hudson.war | grep -v grep | awk '{ print $2 }'`

