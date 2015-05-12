import json
import mock
import StringIO
import unittest

from avro import io, schema

import sprockets.mixins.avro


SIMPLE_SCHEMA = {
    'namespace': 'com.aweber.tests',
    'name': 'SimpleTest',
    'type': 'record',
    'fields': [
        {'name': 'name', 'type': 'string'},
        {'name': 'email', 'type': 'string'},
    ],
}

print('SCHEMA', repr(schema), dir(schema))
schema_obj = schema.parse(json.dumps(SIMPLE_SCHEMA))


class BaseConsumer(object):
    def __init__(self, settings):
        self._message = mock.Mock(body=None)
        self._message.properties = mock.Mock(
            content_encoding=None,
            content_type=None,
            correlation_id='CORRELATION-ID',
            exchange='exchange',
            headers={},
            message_id='MESSAGE-ID',
            routing_key='routing.key',
            type=None,
        )
        self._message_body = None

    def prepare(self):
        pass

    @property
    def content_type(self):
        return self._message.properties.content_type

    @property
    def body(self):
        return self._message_body or self._message.body


class ConcreteConsumer(sprockets.mixins.avro.Decoder, BaseConsumer):

    def __init__(self, message_body, content_type):
        super(ConcreteConsumer, self).__init__({})
        self._message.body = message_body
        self._message.properties.content_type = content_type

    def get_avro_schema(self):
        return schema_obj


class AvroConsumerTests(unittest.TestCase):

    @staticmethod
    def get_avro_binary(name, email):
        buf = StringIO.StringIO()
        encoder = io.BinaryEncoder(buf)
        writer = io.DatumWriter(schema_obj)
        writer.write({'name': name, 'email': email}, encoder)
        return buf.getvalue()

    def test_that_avro_message_is_decoded(self):
        consumer = ConcreteConsumer(self.get_avro_binary('me', 'me@foo.com'),
                                    'application/vnd.apache.avro.datum')
        consumer.prepare()
        self.assertEqual(consumer.body, {'name': 'me', 'email': 'me@foo.com'})

    def test_that_super_is_used_for_other_types(self):
        consumer = ConcreteConsumer(mock.sentinel.body, 'something/else')
        consumer.prepare()
        self.assertEqual(consumer.body, mock.sentinel.body)

    def test_that_body_is_not_decoded_multiple_times(self):
        consumer = ConcreteConsumer(self.get_avro_binary('me', 'me@foo.com'),
                                    'application/vnd.apache.avro.datum')
        consumer.prepare()
        first_body = consumer.body
        consumer._message.body = None
        self.assertTrue(consumer.body is first_body)

    def test_that_unicode_message_works(self):
        consumer = ConcreteConsumer(
            self.get_avro_binary(u'm\u4e35', 'me@foo.com'),
            'application/vnd.apache.avro.datum')
        consumer.prepare()
        self.assertEqual(consumer.body['name'], u'm\u4e35')
