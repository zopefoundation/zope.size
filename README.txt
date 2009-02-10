This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the ``getSize``
method that returns size in bytes, however, it won't crash if an object doesn't
have one and will show size as ``not available`` instead.
