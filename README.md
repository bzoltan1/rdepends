# Reverse dependency discovering tool for OpenSUSE

This tool is to list all packages what depend on a given package.

## Requirements

The tool is a python3 script what imports

* subprocess
* os
* sys
* re

and uses zypper

## How to use

$ rdepends [ packagename ] [--details] [--full-tree]
## Simple usecase
To list the packages directly depend on the package
```
$ rdepends [package name]
```
To list the packages with all details directly or indirectly depend on the package
```
$ rdepends [package name] --details --full-tree
```


## Options and parameters

* [packagename]

  + The package for what the tool will find the reverse dependencies

* [--details]

    + Instad of returning the list of packages the tool will return a ll details about the packages. Like status, name, kind, edition, arch, repository.

* [--full-tree]

    + The tool lists only the packages depend on the given package. With this option the tool dives into recursive mode and finds all packages what indirectly depend on the given package. This mode might take extremely long and might lead to infinite recursive loop if there is a circular dependency in the dependency tree.
