### RPM external py3-chardet 3.0.4
## IMPORT build-with-pip3

%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*