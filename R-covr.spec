#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-covr
Version  : 3.6.4
Release  : 40
URL      : https://cran.r-project.org/src/contrib/covr_3.6.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/covr_3.6.4.tar.gz
Summary  : Test Coverage for Packages
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-covr-lib = %{version}-%{release}
Requires: R-covr-license = %{version}-%{release}
Requires: R-crayon
Requires: R-digest
Requires: R-httr
Requires: R-jsonlite
Requires: R-rex
Requires: R-withr
Requires: R-yaml
BuildRequires : R-crayon
BuildRequires : R-digest
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-rex
BuildRequires : R-withr
BuildRequires : R-yaml
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# covr <img src="man/figures/logo.png" align="right" />
<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/covr/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/covr/actions/workflows/R-CMD-check.yaml)
[![Codecov test coverage](https://codecov.io/gh/r-lib/covr/branch/master/graph/badge.svg)](https://app.codecov.io/gh/r-lib/covr?branch=master)
[![CRAN version](http://www.r-pkg.org/badges/version/covr)](https://cran.r-project.org/package=covr)
<!-- badges: end -->

%package lib
Summary: lib components for the R-covr package.
Group: Libraries
Requires: R-covr-license = %{version}-%{release}

%description lib
lib components for the R-covr package.


%package license
Summary: license components for the R-covr package.
Group: Default

%description license
license components for the R-covr package.


%prep
%setup -q -n covr
pushd ..
cp -a covr buildavx2
popd
pushd ..
cp -a covr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737138289

%install
export SOURCE_DATE_EPOCH=1737138289
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-covr
cp %{_builddir}/covr/inst/www/shared/highlight.js/LICENSE %{buildroot}/usr/share/package-licenses/R-covr/998ba4f9efa902a7f49406a879497625be26ba64 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/covr/DESCRIPTION
/usr/lib64/R/library/covr/INDEX
/usr/lib64/R/library/covr/LICENSE
/usr/lib64/R/library/covr/Meta/Rd.rds
/usr/lib64/R/library/covr/Meta/features.rds
/usr/lib64/R/library/covr/Meta/hsearch.rds
/usr/lib64/R/library/covr/Meta/links.rds
/usr/lib64/R/library/covr/Meta/nsInfo.rds
/usr/lib64/R/library/covr/Meta/package.rds
/usr/lib64/R/library/covr/Meta/vignette.rds
/usr/lib64/R/library/covr/NAMESPACE
/usr/lib64/R/library/covr/NEWS.md
/usr/lib64/R/library/covr/R/covr
/usr/lib64/R/library/covr/R/covr.rdb
/usr/lib64/R/library/covr/R/covr.rdx
/usr/lib64/R/library/covr/doc/how_it_works.R
/usr/lib64/R/library/covr/doc/how_it_works.Rmd
/usr/lib64/R/library/covr/doc/how_it_works.html
/usr/lib64/R/library/covr/doc/index.html
/usr/lib64/R/library/covr/help/AnIndex
/usr/lib64/R/library/covr/help/aliases.rds
/usr/lib64/R/library/covr/help/covr.rdb
/usr/lib64/R/library/covr/help/covr.rdx
/usr/lib64/R/library/covr/help/figures/logo.png
/usr/lib64/R/library/covr/help/paths.rds
/usr/lib64/R/library/covr/html/00Index.html
/usr/lib64/R/library/covr/html/R.css
/usr/lib64/R/library/covr/rstudio/addins.dcf
/usr/lib64/R/library/covr/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/R/TestCompiled.R
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/man/simple.Rd
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/src/simple.cc
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/Test+Char/TestCompiled/tests/testthat/test-TestCompiled.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/R/TestCompiled.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/man/simple.Rd
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/src/simple-header.h
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/src/simple.cc
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/src/simple4.cc
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiled/tests/testthat/test-TestCompiled.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/R/TestCompiledSubdir.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/man/simple.Rd
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/src/Makevars
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/src/lib/simple.c
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestCompiledSubdir/tests/testthat/test-TestCompiledSubdir.R
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/R/TestExclusion.R
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/man/test_me.Rd
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestExclusion/tests/testthat/test-TestExclusion.R
/usr/lib64/R/library/covr/tests/testthat/TestFunctional/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestFunctional/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestFunctional/R/a.R
/usr/lib64/R/library/covr/tests/testthat/TestFunctional/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestFunctional/tests/testthat/test-a.R
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/R/a.R
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/tests/testthat/nested_tests/test-a.R
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/tests/testthat/test-a.R
/usr/lib64/R/library/covr/tests/testthat/TestNestedTestDirs/tests/testthat/test-nested-dir.R
/usr/lib64/R/library/covr/tests/testthat/TestParallel/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestParallel/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestParallel/R/TestParallel.R
/usr/lib64/R/library/covr/tests/testthat/TestParallel/man/test_me.Rd
/usr/lib64/R/library/covr/tests/testthat/TestParallel/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestParallel/tests/testthat/test-TestParallel.R
/usr/lib64/R/library/covr/tests/testthat/TestPrint/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestPrint/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestPrint/R/TestPrint.R
/usr/lib64/R/library/covr/tests/testthat/TestPrint/man/test_me.Rd
/usr/lib64/R/library/covr/tests/testthat/TestPrint/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestPrint/tests/testthat/test-TestSummary.R
/usr/lib64/R/library/covr/tests/testthat/TestR6/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestR6/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestR6/R/TestR6.R
/usr/lib64/R/library/covr/tests/testthat/TestR6/man/a.Rd
/usr/lib64/R/library/covr/tests/testthat/TestR6/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestR6/tests/testthat/test-TestR6.R
/usr/lib64/R/library/covr/tests/testthat/TestRC/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestRC/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestRC/R/TestRC.R
/usr/lib64/R/library/covr/tests/testthat/TestRC/man/a.Rd
/usr/lib64/R/library/covr/tests/testthat/TestRC/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestRC/tests/testthat/test-TestRC.R
/usr/lib64/R/library/covr/tests/testthat/TestS4/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestS4/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestS4/R/TestS4.R
/usr/lib64/R/library/covr/tests/testthat/TestS4/codecov.yml
/usr/lib64/R/library/covr/tests/testthat/TestS4/man/a.Rd
/usr/lib64/R/library/covr/tests/testthat/TestS4/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestS4/tests/testthat/test-TestS4.R
/usr/lib64/R/library/covr/tests/testthat/TestSummary/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestSummary/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestSummary/R/TestSummary.R
/usr/lib64/R/library/covr/tests/testthat/TestSummary/man/test_me.Rd
/usr/lib64/R/library/covr/tests/testthat/TestSummary/tests/testthat.R
/usr/lib64/R/library/covr/tests/testthat/TestSummary/tests/testthat/test-TestSummary.R
/usr/lib64/R/library/covr/tests/testthat/TestUseTry/DESCRIPTION
/usr/lib64/R/library/covr/tests/testthat/TestUseTry/NAMESPACE
/usr/lib64/R/library/covr/tests/testthat/TestUseTry/R/notry.R
/usr/lib64/R/library/covr/tests/testthat/TestUseTry/tests/tests.R
/usr/lib64/R/library/covr/tests/testthat/TestUseTry/tests/testthat/test-notry.R
/usr/lib64/R/library/covr/tests/testthat/a
/usr/lib64/R/library/covr/tests/testthat/b
/usr/lib64/R/library/covr/tests/testthat/cobertura.xml
/usr/lib64/R/library/covr/tests/testthat/corner-cases-test.R
/usr/lib64/R/library/covr/tests/testthat/corner-cases.R
/usr/lib64/R/library/covr/tests/testthat/corner-cases.Rds
/usr/lib64/R/library/covr/tests/testthat/helper.R
/usr/lib64/R/library/covr/tests/testthat/sonarqube.xml
/usr/lib64/R/library/covr/tests/testthat/test-Compiled.R
/usr/lib64/R/library/covr/tests/testthat/test-R6.R
/usr/lib64/R/library/covr/tests/testthat/test-RC.R
/usr/lib64/R/library/covr/tests/testthat/test-S4.R
/usr/lib64/R/library/covr/tests/testthat/test-azure.R
/usr/lib64/R/library/covr/tests/testthat/test-braceless.R
/usr/lib64/R/library/covr/tests/testthat/test-cobertura.R
/usr/lib64/R/library/covr/tests/testthat/test-codecov.R
/usr/lib64/R/library/covr/tests/testthat/test-corner-cases.R
/usr/lib64/R/library/covr/tests/testthat/test-coveralls.R
/usr/lib64/R/library/covr/tests/testthat/test-covr.R
/usr/lib64/R/library/covr/tests/testthat/test-exclusions.R
/usr/lib64/R/library/covr/tests/testthat/test-file_coverage.R
/usr/lib64/R/library/covr/tests/testthat/test-functions.R
/usr/lib64/R/library/covr/tests/testthat/test-gcov.R
/usr/lib64/R/library/covr/tests/testthat/test-gitlab.R
/usr/lib64/R/library/covr/tests/testthat/test-memoised.R
/usr/lib64/R/library/covr/tests/testthat/test-null.R
/usr/lib64/R/library/covr/tests/testthat/test-package_coverage.R
/usr/lib64/R/library/covr/tests/testthat/test-parallel.R
/usr/lib64/R/library/covr/tests/testthat/test-print.R
/usr/lib64/R/library/covr/tests/testthat/test-record_tests.R
/usr/lib64/R/library/covr/tests/testthat/test-report.R
/usr/lib64/R/library/covr/tests/testthat/test-report.htm
/usr/lib64/R/library/covr/tests/testthat/test-sonarqube.R
/usr/lib64/R/library/covr/tests/testthat/test-summary.R
/usr/lib64/R/library/covr/tests/testthat/test-tally_coverage.R
/usr/lib64/R/library/covr/tests/testthat/test-trace_calls.R
/usr/lib64/R/library/covr/tests/testthat/test-utils.R
/usr/lib64/R/library/covr/tests/testthat/test-vectorized.R
/usr/lib64/R/library/covr/www/report.css
/usr/lib64/R/library/covr/www/shared/bootstrap/css/bootstrap-theme.min.css
/usr/lib64/R/library/covr/www/shared/bootstrap/css/bootstrap.min.css
/usr/lib64/R/library/covr/www/shared/bootstrap/js/bootstrap.min.js
/usr/lib64/R/library/covr/www/shared/bootstrap/shim/html5shiv.min.js
/usr/lib64/R/library/covr/www/shared/bootstrap/shim/respond.min.js
/usr/lib64/R/library/covr/www/shared/highlight.js/LICENSE
/usr/lib64/R/library/covr/www/shared/highlight.js/highlight.pack.js
/usr/lib64/R/library/covr/www/shared/highlight.js/rstudio.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/covr/libs/covr.so
/V4/usr/lib64/R/library/covr/libs/covr.so
/usr/lib64/R/library/covr/libs/covr.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-covr/998ba4f9efa902a7f49406a879497625be26ba64
