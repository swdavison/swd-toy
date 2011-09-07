#!/bin/bash
# +++ fetchwiki.sh: Fetch wiki pages as wiki-formatted text
#
#
#    This script fetches text pages containing wiki formatting.
#    To use it:
#    1.  Create a workarea directory.
#    2.  Check out the repository version of the wiki files and
#        set your CWD to the checked-out directory:
#          cd workarea
#          svn checkout $SDO/asdtwiki/branches/davison asdtwiki
#          cd asdtwiki
#    3.  In that directory create a file called curl.args.  That file
#        should have two lines:
#            insecure
#            user = user.name:passwordForUserName
#    4.  Edit the definitions of WIKI and WP in this script as necessary.
#    5.  Run the script.
#            ./fetchwiki.sh
#        The files in your workarea will be overwritten by the wiki's
#        current files.
#    6.  Do a checkpoint checkin to ensure that the Subversion repository
#            reflects the current stage of the wiki files.
#    7.  Edit the wiki files.
#    8.  Update the wiki.
#    9.  Update the repository (checkin).  Be sure to update the wiki
#        before updating the repository.
#    
# --- =====================================================

export WIKI=https://collaborate.nws.noaa.gov/trac/asdt/wiki/

WP=''
WP="$WP AiiHb"
WP="$WP AiiHbDevEnv "
WP="$WP AiiHbDevEnvUse "
WP="$WP AiiHbDevEnvUseSu "
WP="$WP AiiHbDevEnvUseDb "
WP="$WP AiiHbDevEnvUseUb "
WP="$WP AiiHbDevEnvUseDc "
WP="$WP AiiHbDevEnvAdminRd "
WP="$WP AiiHbDevEnvInst "
WP="$WP AiiHbDevEnvInstHsw "
WP="$WP AiiHbDevEnvInstSysadFirst "
WP="$WP AiiHbDevEnvInstApache "
WP="$WP AiiHbDevEnvInstSvn "
WP="$WP AiiHbDevEnvInstRepo "
WP="$WP AiiHbDevEnvInstRepoBkp "
WP="$WP AiiHbDevEnvInstEcl "
WP="$WP AiiHbDevEnvInstHud "
WP="$WP AiiHbDevEnvInstSvnac "
WP="$WP AiiHbDevEnvInstTrac "
WP="$WP AiiHbDevEnvInstSysadLast "
WP="$WP AiiHbTools "
WP="$WP AiiHbToolsEclipse "
WP="$WP AiiHbToolsAnt "
WP="$WP AiiHbToolsTest "
WP="$WP AiiHbArch"
WP="$WP AiiHbRes"
WP="$WP AiiHbTopicList"

export WP

for wp in $WP
do
    url="${WIKI}/${wp}?format=txt"
    curl --config ./curl.args --output ${wp}.wiki --url $url
    echo $wp
done





