Summary: Outputs "hello world" on execution.
Name: hello
Version: 1.0.0
Release: 1
License: public domain
BuildRoot: /var/tmp/%{name}-buildroot
#Source: /home/chris/source/hello

%description
Hello world.

%pre
 echo "this is the pre-install sh commands"
 mkdir -p /opt/hello/

%post
 echo "this is the post-install sh commans"

%files
%dir /opt
%dir /opt/hello

%defattr(700,root,root)
/opt/hello/hello

%preun
 echo "the pre-uninstall sh commands"

%postun
 echo "the post-uninstall sh commands"

%define _binary_payload w9.bzdio

%prep
rm -rf *
git clone /home/chris/source/hello hello
mv hello/* .
rm -rf hello

%build
make 
mkdir -p opt/hello
cp hello opt/hello
pwd
ls -R

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cp -r opt $RPM_BUILD_ROOT
