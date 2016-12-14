#!/bin/bash
source /vols/grid/cms/setup.sh
export CMSSW_BASE=/home/hep/sdb15/CMSSW_8_1_0/
cd ${CMSSW_BASE}/src && eval `scramv1 runtime -sh` && cd - > /dev/null

#Change to directory of setup script
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR
python splash.py
export PYTHONPATH=${PWD}/:${PYTHONPATH}
export PYTHONPATH=${PWD}/Core/:${PYTHONPATH}
export PYTHONPATH=${PWD}/python/:${PYTHONPATH}
export GITBASE=${PWD}
cd - > /dev/null
