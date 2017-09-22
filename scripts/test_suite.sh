#!/bin/bash

if [[ "$1" == "pylint" ]]
then for dir in `find google/cloud/security/ -type d`
    do pylint --rcfile=pylintrc google/cloud/security/common $dir
    done
fi