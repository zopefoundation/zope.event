==========================
 ``zope.event`` Changelog
==========================


6.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.

5.1.1 (2025-07-22)
==================

- Require ``setuptools >= 75.8.2`` to prevent problems with the new packaging
  standard.
  (`#30 <https://github.com/zopefoundation/zope.event/issues/30>`_)


5.1 (2025-06-26)
================

- Add support for Python 3.12 and 3.13.

- Drop support for Python 3.7 and 3.8.


5.0 (2023-06-23)
================

- Drop support for Python 2.7, 3.5, 3.6.


4.6 (2022-12-15)
================

- Port documentation to Python 3.

- Add support for Python 3.10, 3.11.


4.5.0 (2020-09-18)
==================

- Add support for Python 3.8 and 3.9.

- Remove support for Python 3.4.


4.4 (2018-10-05)
================

- Add support for Python 3.7


4.3.0 (2017-07-25)
==================

- Add support for Python 3.6.

- Drop support for Python 3.3.


4.2.0 (2016-02-17)
==================

- Add support for Python 3.5.

- Drop support for Python 2.6 and 3.2.


4.1.0 (2015-10-18)
==================

- Require 100% branch (as well as statement) coverage.

- Add a simple class-based handler implementation.


4.0.3 (2014-03-19)
==================

- Add support for Python 3.4.

- Update ``boostrap.py`` to version 2.2.


4.0.2 (2012-12-31)
==================

- Flesh out PyPI Trove classifiers.

- Add support for jython 2.7.


4.0.1 (2012-11-21)
==================

- Add support for Python 3.3.


4.0.0 (2012-05-16)
==================

- Automate build of Sphinx HTML docs and running doctest snippets via tox.

- Drop explicit support for Python 2.4 / 2.5 / 3.1.

- Add support for PyPy.


3.5.2 (2012-03-30)
==================

- This release is the last which will maintain support for Python 2.4 /
  Python 2.5.

- Add support for continuous integration using ``tox`` and ``jenkins``.

- Add 'setup.py dev' alias (runs ``setup.py develop`` plus installs
  ``nose`` and ``coverage``).

- Add 'setup.py docs' alias (installs ``Sphinx`` and dependencies).


3.5.1 (2011-08-04)
==================

- Add Sphinx documentation.


3.5.0 (2010-05-01)
==================

- Add change log to ``long-description``.

- Add support for Python 3.x.


3.4.1 (2009-03-03)
==================

- A few minor cleanups.


3.4.0 (2007-07-14)
==================

- Initial release as a separate project.
