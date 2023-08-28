#!/usr/bin/env python3

from helpers.string_helpers import RobotMovementStringDictHelper
from robot_movement import RobotMovement


def main():
    robot_movement_string_dict_helper: RobotMovementStringDictHelper = RobotMovementStringDictHelper()
    robot_movement: RobotMovement = RobotMovement(robot_movement_string_dict_helper, 0.00, 0.00)
    print(robot_movement.execute())


if __name__ == '__main__':
    main()
