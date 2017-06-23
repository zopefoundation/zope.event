=================================
 :mod:`zope.event` Documentation
=================================

This package provides a simple event system on which
application-specific event systems can be built. For example, a
type-based event dispatching system that builds on `zope.interface
<https://zopeinterface.readthedocs.io/en/latest/>`_ can be found in
`zope.component <https://zopecomponent.readthedocs.io/en/latest>`_. A
simpler system is distributed with this package and is described in :doc:`classhandler`.

Application code can generate events without being concerned about the
event-processing frameworks that might handle the events.

Events are objects that represent something happening in a system.
They are used to extend processing by providing processing plug
points.

Contents:

.. toctree::
   :maxdepth: 2

   usage
   theory
   api
   classhandler
   hacking

====================
 Indices and tables
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
