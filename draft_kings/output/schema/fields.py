from datetime import datetime

from marshmallow import fields


class CustomAwareDateTime(fields.AwareDateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        """
        https://github.com/marshmallow-code/marshmallow/issues/656#issuecomment-318587611
        """
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise self.make_error(
                    "invalid", input=value, obj_type=self.OBJ_TYPE
                )
            return value
        return super()._deserialize(value, attr, data)

    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise self.make_error(
                    "invalid", input=value, obj_type=self.OBJ_TYPE
                )
        return super()._serialize(value, attr, obj, **kwargs)


class CustomDateTime(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data)
