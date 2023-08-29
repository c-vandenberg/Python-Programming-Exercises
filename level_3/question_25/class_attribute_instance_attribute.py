#!/usr/bin/env python3


class ClassAttributeInstanceAttribute:

    _test_class_instance_attribute: str = 'Initial value'

    def __init__(self, test_class_instance_attribute: str):
        self._test_class_instance_attribute = test_class_instance_attribute

    @property
    def test_class_instance_attribute(self) -> str:
        return self._test_class_instance_attribute

    @test_class_instance_attribute.setter
    def test_class_instance_attribute(self, new_test_class_instance_attribute: str) -> None:
        if new_test_class_instance_attribute != str:
            raise TypeError('New value for test class instance attribute must be of type str')

        self._test_class_instance_attribute = new_test_class_instance_attribute
