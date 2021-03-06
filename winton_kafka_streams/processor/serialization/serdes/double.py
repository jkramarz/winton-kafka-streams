"""
Float Serde

"""
from ..double import DoubleDeserializer, DoubleSerializer
from .wrapper_serde import WrapperSerde


class DoubleSerde(WrapperSerde):
    def __init__(self):
        serializer = DoubleSerializer()
        deserializer = DoubleDeserializer()
        super().__init__(serializer, deserializer)
