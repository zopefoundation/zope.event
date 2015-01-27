``zope.event`` README
=====================

.. image:: https://pypip.in/version/zope.event/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/zope.event/
    :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.event.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.event

The ``zope.event`` package provides a simple event system, including:

- An event publishing API, intended for use by applications which are
  unaware of any subscribers to their events.

- A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on ``zope.event`` can be found in
  ``zope.component``.

Please see http://docs.zope.org/zope.event/ for the documentation.
