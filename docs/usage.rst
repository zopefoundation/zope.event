.. _usage-docs:

=========================
 Using :mod:`zope.event`
=========================

.. py:module:: zope.event

At its core, :mod:`zope.event` simply consists of two things: a list
of subscribers (callable objects), and an API function
(:func:`~.zope.event.notify`) that invokes those subscribers in order.

.. testsetup::

  import zope.event
  old_subscribers = zope.event.subscribers[:]
  del zope.event.subscribers[:]

Notifications
=============

Alerting subscribers that an event has occurred is referred to as
"notifying them", or sometimes "sending them the event."

The package provides a :func:`~.zope.event.notify` function, which is used to
notify subscribers that something has happened:

.. doctest::

  >>> class MyEvent(object):
  ...     pass

  >>> event = MyEvent()
  >>> zope.event.notify(event)

The notify function is called with a single object, which we call an
event. Any object will do:

.. doctest::

  >>> zope.event.notify(None)
  >>> zope.event.notify(42)

Our subscriber list is currently empty, so nothing happened in
response to these notifications.

Subscribers
===========

A *subscriber* is a callable object that takes one argument, an object
that we call the *event*.

Application code can manage subscriptions by manipulating the list
that ``zope.event`` maintains. This list starts out empty.

.. doctest::

  >>> import zope.event
  >>> zope.event.subscribers
  []


.. note:: Users of higher-level event frameworks will not typically
   need to modify *this* subscriber list directly. Generally, such event
   (or application) frameworks will provide more sophisticated
   subscription mechanisms that build on this simple mechanism. The
   frameworks will install subscribers that then distribute the event to other
   subscribers based on event types or data.

   A simple framework that is based on the class hierarchy is
   distributed with this package and described in :doc:`classhandler`.

   A higher-level event framework is distributed with
   :mod:`zope.component`. For information on using :mod:`zope.event`
   together with :mod:`zope.component`, see `zope.component's
   documentation
   <http://zopecomponent.readthedocs.io/en/latest/event.html>`_.


Trivial Subscribers
-------------------

As mentioned above, subscribers are simply callable objects that are
added to the subscriptions list:

.. doctest::

  >>> def f(event):
  ...     print('got:', event)
  >>> zope.event.subscribers.append(f)

  >>> zope.event.notify(42)
  got: 42

  >>> def g(event):
  ...     print('also got:', event)

  >>> zope.event.subscribers.append(g)

  >>> zope.event.notify(42)
  got: 42
  also got: 42

To unsubscribe, simply remove a subscriber from the list:

.. doctest::

  >>> zope.event.subscribers.remove(f)
  >>> zope.event.notify(42)
  also got: 42

  >>> zope.event.subscribers.remove(g)
  >>> zope.event.notify(42)

.. testcleanup::

  zope.event.subscribers[:] = old_subscribers

.. note:: The :func:`~.zope.event.notify` is synchronous, meaning it calls the
   subscribers in sequential order (and not in parallel). This also means that the
   process will not continue until all subscribers are done handling the event.
