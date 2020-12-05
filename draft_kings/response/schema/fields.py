# pylint: disable=unused-argument, no-self-use, invalid-name, protected-access

from marshmallow import fields


class DictField(fields.Field):
    """
    https://github.com/marshmallow-code/marshmallow/issues/120#issuecomment-81382070
    """

    def __init__(self, key_field, nested_field, *args, **kwargs):
        fields.Field.__init__(self, *args, **kwargs)
        self.key_field = key_field
        self.nested_field = nested_field

    def _deserialize(self, value, attr, data, **kwargs):
        ret = {}
        for key, val in value.items():
            k = self.key_field.deserialize(key)
            v = self.nested_field.deserialize(val)
            ret[k] = v
        return ret

    def _serialize(self, value, attr, obj, **kwargs):
        ret = {}
        for key, _ in value.items():
            k = self.key_field._serialize(key, attr, obj)
            v = self.nested_field.serialize(key, self.get_value(attr, obj))
            ret[k] = v
        return ret

# pylint: enable=unused-argument, no-self-use, invalid-name, protected-access
