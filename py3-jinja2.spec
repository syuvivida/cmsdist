### RPM external py3-jinja2 3.1.2
## IMPORT build-with-pip3
Requires: py3-markupsafe
%define pip_name Jinja2
%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*
