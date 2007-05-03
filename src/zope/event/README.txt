Events
======

This package provides a simple event system on which
application-specific event systems can be built.

Application code can generate events without being concerned about the
event-processing frameworks that might handle the events.

Events are objects that represent something happening in a system.
They are used to extend processing by providing processing plug
points.

The package has a list of subscribers.  Application code can manage
subscriptions by manipulating this list.  For the examples here, we'll
save the current contents away and empty the list. We'll restore the
contents when we're done with our examples.

  >>> import zope.event
  >>> old_subscribers = zope.event.subscribers[:]
  >>> del zope.event.subscribers[:]

The package provides a `notify` function, which is used to
notify subscribers that something has happened:

  >>> class MyEvent:
  ...     pass

  >>> event = MyEvent()
  >>> zope.event.notify(event)

The notify function is called with a single object, which we call an
event.  Any object will do:

  >>> zope.event.notify(None)
  >>> zope.event.notify(42)

An extremely trivial subscription mechanism is provided. Subscribers
are simply callback functions:

  >>> def f(event):
  ...     print 'got:', event

that are put into the subscriptions list:

  >>> zope.event.subscribers.append(f)

  >>> zope.event.notify(42)
  got: 42

  >>> def g(event):
  ...     print 'also got:', event

  >>> zope.event.subscribers.append(g)

  >>> zope.event.notify(42)
  got: 42
  also got: 42

To unsubscribe, simply remove a subscriber from the list:

  >>> zope.event.subscribers.remove(f)
  >>> zope.event.notify(42)
  also got: 42

Generally, application frameworks will provide more sophisticated
subscription mechanisms that build on this simple mechanism. The
frameworks will install subscribers that then dispatch to other
subscribers based on event types or data.

We're done, so we'll restore the subscribers:

  >>> zope.event.subscribers[:] = old_subscribers
