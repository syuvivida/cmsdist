### RPM external xrootd-toolfile 1.0
Requires: xrootd
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/xrootd.xml
<tool name="xrootd" version="@TOOL_VERSION@">
  <lib name="XrdUtils"/>
  <lib name="XrdClient"/>
  <client>
    <environment name="XROOTD_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE" default="$XROOTD_BASE/include/xrootd"/>
    <environment name="INCLUDE" default="$XROOTD_BASE/include/xrootd/private"/>
    <environment name="LIBDIR" default="$XROOTD_BASE/lib64"/>
  </client>
  <runtime name="PATH" value="$XROOTD_BASE/bin" type="path"/>
  <runtime name="PYTHONPATH" value="$XROOTD_BASE/lib/python@PYTHONV@/site-packages" type="path"/>
  <runtime name="ROOT_INCLUDE_PATH" value="$INCLUDE" type="path"/>
  <use name="root_cxxdefaults"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
