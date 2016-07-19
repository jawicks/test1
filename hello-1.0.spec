Summary: Outputs "hello world" on execution.
Name: hello
Version: 1.0.0
Release: 1
License: public domain
BuildRoot: /var/tmp/%{name}-buildroot

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

%build
make 
