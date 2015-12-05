Name:           gco
Version:        3.0
Release:        1%{?dist}
Summary:        Optimizing multi-label energies via the α-expansion and α-β-swap algorithms

License:        BSD
URL:            http://vision.csd.uwo.ca/code
Source0:        http://vision.csd.uwo.ca/code/%{name}-v%{version}.zip
Source1:        CMakeLists.txt

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Library is for optimizing multi-label energies via the α-expansion and
α-β-swap algorithms. It supports energies with any combination of
unary, pairwise, and label cost terms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -c
cp %{SOURCE1} .

rm -rf build
mkdir build

%build
pushd build
  %cmake ../
  %make_build
popd

%install
pushd build
  %make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc GCO_README.TXT
%{_libdir}/lib%{name}.so.*

%files devel
%doc example.cpp
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.0-1
- Initial package
