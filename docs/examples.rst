Examples
========

Rejected Consumer
-----------------

A `rejected`_ consumer that automatically decodes and validates messages
serialized using Avro.

.. code-block:: python

   from pkg_resources import resource_string

   from avro import schema
   from rejected import consumer
   import sprockets.mixins.avro

   class MyConsumer(sprockets.mixins.avro.Decoder,
                    consumer.PublishingConsumer):

       def __init__(self, *args, **kwargs):
           super(MyConsumer, self).__init__(*args, **kwargs)
           self._schema = None

       def get_avro_schema(self):
           if self._schema is None:
               schema_string = resource_string('mypackage', 'schema.avsc')
               self._schema = schema.parse(schema_string)

       def process(self):
           # self.body refers to the current message *AFTER*
           # decoding and validating it according to the
           # Avro schema!

.. _rejected: https://rejected.readthedocs.org/en/latest/
