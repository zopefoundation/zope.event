Hacking on :mod:`zope.event`
============================


Getting the Code
-----------------

The main repository for :mod:`zope.event` is in the Zope Subversion
repository:

http://svn.zope.org/zope.event

You can get a read-only Subversion checkout from there:

.. code-block:: sh

   $ svn checkout svn://svn.zope.org/repos/main/zope.event/trunk zope.event

The project also mirrors the trunk from the Subversion repository as a
Bazaar branch on Launchpad:

https://code.launchpad.net/zope.event

You can branch the trunk from there using Bazaar:

.. code-block:: sh

   $ bzr branch lp:zope.event


Running the tests in a ``virtualenv``
-------------------------------------

If you use the ``virtualenv`` package to create lightweight Python
development environments, you can run the tests using nothing more
than the ``python`` binary in a virtualenv.  First, create a scratch
environment:

.. code-block:: sh

   $ /path/to/virtualenv --no-site-packages /tmp/hack-zope.event

Next, get this package registered as a "development egg" in the
environment:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/python setup.py develop

Finally, run the tests using the build-in ``setuptools`` testrunner:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/python setup.py test
   running test
   ...
   test_empty (zope.event.tests.Test_notify) ... ok
   test_not_empty (zope.event.tests.Test_notify) ... ok

   ----------------------------------------------------------------------
   Ran 2 tests in 0.000s

   OK

If you have the :mod:`nose` package installed in the virtualenv, you can
use its testrunner too:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/easy_install nose
   ...
   $ /tmp/hack-zope.event/bin/python setup.py nosetests
   running nosetests
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.011s

   OK

or:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/nosetests
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.011s

   OK

If you have the :mod:`coverage` pacakge installed in the virtualenv,
you can see how well the tests cover the code:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/easy_install nose coverage
   ...
   $ /tmp/hack-zope.event/bin/python setup.py nosetests \
       --with coverage --cover-package=zope.event
   running nosetests
   ...
   Name         Stmts   Exec  Cover   Missing
   ------------------------------------------
   zope.event       5      5   100%   
   ----------------------------------------------------------------------
   Ran 3 tests in 0.019s

   OK


Building the documentation in a ``virtualenv``
----------------------------------------------

:mod:`zope.event` uses the nifty :mod:`Sphinx` documentation system
for building its docs.  Using the same virtualenv you set up to run the
tests, you can build the docs:

.. code-block:: sh

   $ /tmp/hack-zope.event/bin/easy_install Sphinx
   ...
   $ cd docs
   $ PATH=/tmp/hack-zope.event/bin:$PATH make html
   sphinx-build -b html -d _build/doctrees   . _build/html
   ...
   build succeeded.

   Build finished. The HTML pages are in _build/html.

You can also test the code snippets in the documentation:

.. code-block:: sh

   $ PATH=/tmp/hack-zope.event/bin:$PATH make doctest
   sphinx-build -b doctest -d _build/doctrees   . _build/doctest
   ...
   running tests...

   Document: index
   ---------------
   1 items passed all tests:
     17 tests in default
   17 tests in 1 items.
   17 passed and 0 failed.
   Test passed.

   Doctest summary
   ===============
      17 tests
       0 failures in tests
       0 failures in setup code
   build succeeded.
   Testing of doctests in the sources finished, look at the  \
       results in _build/doctest/output.txt.


Running the tests using  :mod:`zc.buildout`
-------------------------------------------

:mod:`zope.event` ships with its own :file:`buildout.cfg` file and
:file:`bootstrap.py` for setting up a development buildout:

.. code-block:: sh

   $ /path/to/python2.6 bootstrap.py
   ...
   Generated script '.../bin/buildout'
   $ bin/buildout
   Develop: '/home/tseaver/projects/Zope/BTK/event/.'
   ...
   Generated script '.../bin/sphinx-quickstart'.
   Generated script '.../bin/sphinx-build'.

You can now run the tests:

.. code-block:: sh

   $ bin/test --all
   Running zope.testing.testrunner.layer.UnitTests tests:
     Set up zope.testing.testrunner.layer.UnitTests in 0.000 seconds.
     Ran 2 tests with 0 failures and 0 errors in 0.000 seconds.
   Tearing down left over layers:
     Tear down zope.testing.testrunner.layer.UnitTests in 0.000 seconds.


Building the documentation using :mod:`zc.buildout`
---------------------------------------------------

The :mod:`zope.event` buildout installs the Sphinx scripts required to build
the documentation, including testing its code snippets:

.. code-block:: sh

   $ cd docs
   $ PATH=../bin:$PATH make doctest html
   .../bin/sphinx-build -b doctest -d .../docs/_build/doctrees   .../docs .../docs/_build/doctest
   running tests...

   Document: index
   ---------------
   1 items passed all tests:
     17 tests in default
   17 tests in 1 items.
   17 passed and 0 failed.
   Test passed.

   Doctest summary
   ===============
      17 tests
       0 failures in tests
       0 failures in setup code
   build succeeded.
   Testing of doctests in the sources finished, look at the  results in .../docs/_build/doctest/output.txt.
   .../bin/sphinx-build -b html -d .../docs/_build/doctrees   .../docs .../docs/_build/html
   ...
   build succeeded.

   Build finished. The HTML pages are in .../docs/_build/html.


Running Tests on Multiple Python Versions via :mod:`tox`
--------------------------------------------------------

`tox <http://tox.testrun.org/latest/>`_ is a Python-based test automation
tool designed to run tests against multiple Python versions.  It creates
a ``virtualenv`` for each configured version, installs the current package
and configured dependencies into each ``virtualenv``, and then runs the
configured commands.
   
:mod:`zope.event` configures the following :mod:`tox` environments via
its ``tox.ini`` file:

- The ``py26`` environment builds a ``virtualenv`` with ``python2.6``,
  installs :mod:`zope.event`, and runs the tests
  via ``python setup.py test -q``.

- The ``py27`` environment builds a ``virtualenv`` with ``python2.7``,
  installs :mod:`zope.event`, and runs the tests
  via ``python setup.py test -q``.

- The ``py32`` environment builds a ``virtualenv`` with ``python3.2``,
  installs :mod:`zope.event` and dependencies, and runs the tests
  via ``python setup.py test -q``.

- The ``pypy`` environment builds a ``virtualenv`` with ``pypy``,
  installs :mod:`zope.event`, and runs the tests
  via ``python setup.py test -q``.

- The ``coverage`` environment builds a ``virtualenv`` with ``python2.6``,
  installs :mod:`zope.event`, installs
  :mod:`nose` and :mod:`coverage`, and runs ``nosetests`` with statement
  coverage.

- The ``docs`` environment builds a virtualenv with ``python2.6``, installs
  :mod:`zope.event`, installs ``Sphinx`` and
  dependencies, and then builds the docs and exercises the doctest snippets.

This example requires that you have a working ``python2.6`` on your path,
as well as installing ``tox``:

.. code-block:: sh

   $ tox -e py26
   GLOB sdist-make: .../zope.interface/setup.py
   py26 sdist-reinst: .../zope.interface/.tox/dist/zope.interface-4.0.2dev.zip
   py26 runtests: commands[0]
   ...
   ----------------------------------------------------------------------
   Ran 2 tests in 0.000s

   OK
   ___________________________________ summary ____________________________________
   py26: commands succeeded
   congratulations :)

Running ``tox`` with no arguments runs all the configured environments,
including building the docs and testing their snippets:

.. code-block:: sh

   $ tox
   GLOB sdist-make: .../zope.interface/setup.py
   py26 sdist-reinst: .../zope.interface/.tox/dist/zope.interface-4.0.2dev.zip
   py26 runtests: commands[0]
   ...
   Doctest summary
   ===============
    17 tests
      0 failures in tests
      0 failures in setup code
      0 failures in cleanup code
   build succeeded.
   ___________________________________ summary ____________________________________
   py26: commands succeeded
   py27: commands succeeded
   py32: commands succeeded
   pypy: commands succeeded
   coverage: commands succeeded
   docs: commands succeeded
   congratulations :)


Submitting a Bug Report
-----------------------

:mod:`zope.event` tracks its bugs on Launchpad:

https://bugs.launchpad.net/zope.event

Please submit bug reports and feature requests there.


Sharing Your Changes
--------------------

.. note::

   Please ensure that all tests are passing before you submit your code.
   If possible, your submission should include new tests for new features
   or bug fixes, although it is possible that you may have tested your
   new code by updating existing tests.

If you got a read-only checkout from the Subversion repository, and you
have made a change you would like to share, the best route is to let
Subversion help you make a patch file:

.. code-block:: sh

   $ svn diff > zope.event-cool_feature.patch

You can then upload that patch file as an attachment to a Launchpad bug
report.

If you branched the code from Launchpad using Bazaar, you have another
option:  you can "push" your branch to Launchpad:

.. code-block:: sh

   $ bzr push lp:~tseaver/zope.event/cool_feature

After pushing your branch, you can link it to a bug report on Launchpad,
or request that the maintainers merge your branch using the Launchpad
"merge request" feature.
