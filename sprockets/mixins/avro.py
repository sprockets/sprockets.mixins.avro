from __future__ import absolute_import

try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO

try:
    import avro.io
except ImportError:  # pragma: no cover
    pass  # valid from setup.py


version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info)


class Decoder(object):
    """
    Mix this in over a rejected Consumer for avro deserialization.

    This mix-in implements the ``body`` property that will automatically
    deserialize avro datum values using a provided schema.  You are
    required to implement the :meth:`.get_avro_schema` method so that
    it returns the appropriate :class:`avro.schema.Schema` instance for
    this message type.

    *See also*: :class:`rejected.consumer.Consumer` and
    :class:`rejected.consumer.SmartConsumer`

    """

    def prepare(self):
        super(Decoder, self).prepare()
        self.__body_dict = None

    def get_avro_schema(self):  # pragma: no cover
        """
        Return the avro schema to use for this message.

        :return: the avro schema instance appropriate to this message
        :rtype: avro.schema.Schema

        """
        raise NotImplementedError

    @property
    def body(self):
        """Return the fully deserialized message body."""
        if self.__body_dict is None:
            body = super(Decoder, self).body
            if self.content_type == 'application/vnd.apache.avro.datum':
                decoder = avro.io.BinaryDecoder(StringIO(body))
                reader = avro.io.DatumReader(self.get_avro_schema())
                self.__body_dict = reader.read(decoder)
            else:
                self.__body_dict = body
        return self.__body_dict
