``zope.event`` README
=====================

.. image:: https://img.shields.io/pypi/v/zope.event.svg
        :target: https://pypi.python.org/pypi/zope.event/
        :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.event.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.event

.. image:: https://readthedocs.org/projects/zopeevent/badge/?version=latest
        :target: http://zopeevent.readthedocs.org/en/latest/
        :alt: Documentation Status

The ``zope.event`` package provides a simple event system, including:

- An event publishing API, intended for use by applications which are
  unaware of any subscribers to their events.

- A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on ``zope.event`` can be found in
  ``zope.component``.

Please see http://zopeevent.rtfd.org/ for the documentation.
