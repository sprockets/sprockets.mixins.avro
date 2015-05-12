sprockets.mixins.avro
=====================
Mixins that make working with `Avro`_ data easier.

|Version| |Downloads| |Status| |Coverage| |License|

Documentation
-------------
https://sprocketsmixinsavro.readthedocs.org

Requirements
------------
-  `avro`_

Contributing
------------
This project follows the standard fork and pull request model of development.
If you want to contribute changes, then fork the project and start hacking.
The development environment is pretty simple to set up::

    virtualenv env
    source env/bin/activate
    pip install -r dev-requirements.txt
    pip install -e .

The last step is necessary to account for packages that have different names
for their python 2 and python 3 distributions(e.g., ``avro`` and ``avro-python3``.
Once you have a fork, add tests in *tests.py* and run then with *nosetests*,
implement your feature, add some docs, and issue a pull request against master.
If you add documentation, and you should, you can generate it locally with
**setup.py build_sphinx** -- the output will be in *build/sphinx/html*.

Version History
---------------
See https://github.com/sprockets/sprockets.mixins.avro/blob/master/HISTORY.rst


.. _Avro: http://hadoop.apache.org/avro

.. |Version| image:: https://badge.fury.io/py/sprockets.mixins.avro.svg?
   :target: http://badge.fury.io/py/sprockets.mixins.avro

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.mixins.avro.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.mixins.avro

.. |Coverage| image:: http://codecov.io/github/sprockets/sprockets.mixins.avro/coverage.svg?branch=master
   :target: https://codecov.io/github/sprockets/sprockets.mixins.avro?branch=master

.. |Downloads| image:: https://pypip.in/d/sprockets.mixins.avro/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.mixins.avro

.. |License| image:: https://pypip.in/license/sprockets.mixins.avro/badge.svg?
   :target: https://sprocketsmixinsavro.readthedocs.org
