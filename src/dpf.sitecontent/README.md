# dpf.sitecontent

## Sitecontent package containing folderish content pages

* `Source code @ GitHub <https://github.com/a25kk/dpf.sitecontent>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/dpf.sitecontent>`_
* `Documentation @ ReadTheDocs <http://dpfsitecontent.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/a25kk/dpf.sitecontent>`_

## How it works

This package provides a Plone addon as an installable Python egg package.

The generated Python package hold the necessary scaffold to add content types
via the 'contenttype' template and to add functionality.

In order to get productive you still need to generate a contenttype

```bash
$ cd dpf.sitecontent/src/dpf/sitecontent/
$ mrbob --config ~/.mrbob.ini -O example_type bobtemplates:contenttype

```


## Installation

To install `dpf.sitecontent` you simply add ``dpf.sitecontent``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `dpf.sitecontent` using the Add-ons control panel.
