#!/usr/bin/env bash

if [ $VIRTUAL_ENVIROMENT]
then
    deactivate
fi
. venv_django/Scripts/activate     