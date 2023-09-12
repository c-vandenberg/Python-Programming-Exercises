#!/usr/bin/env python3

from class_attribute_instance_attribute import ClassAttributeInstanceAttribute


def main():
    class_attribute_instance_attribute: ClassAttributeInstanceAttribute = ClassAttributeInstanceAttribute(
        'Instance 1 value'
    )
    print(class_attribute_instance_attribute.test_class_instance_attribute)
    print(ClassAttributeInstanceAttribute.test_class_instance_attribute)


if __name__ == '__main__':
    main()
