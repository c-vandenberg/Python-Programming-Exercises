#!/usr/bin/env python3

import math
from helpers.string_helpers import RobotMovementStringDictHelper


class RobotMovement:
    def __init__(
            self,
            robot_movement_string_dict_helper: RobotMovementStringDictHelper,
            x_coordinate: float,
            y_coordinate: float,
    ):
        self.robot_movement_string_dict_helper = robot_movement_string_dict_helper
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    def _get_user_input(self) -> dict[str: float]:
        user_input: str = input(
            'Please enter a movement string with the general format UP W, DOWN X, LEFT Y, RIGHT Z: '
        )

        return self.robot_movement_string_dict_helper.get_validated_robot_movement_string_dict(user_input)

    def execute(self) -> float:
        robot_movement_input = self._get_user_input()

        initial_x_coordinate: float = self.x_coordinate
        initial_y_coordinate: float = self.y_coordinate

        for direction, steps in robot_movement_input.items():
            self.process_movement_input(direction, steps)

        distance_moved: float = math.sqrt(
            pow(self.x_coordinate - initial_x_coordinate, 2) + pow(self.y_coordinate - initial_y_coordinate, 2)
        )

        return round(distance_moved, 2)

    def process_movement_input(self, direction: str, steps: float):
        movement = {
            'UP': lambda: self._move_up(steps),
            'DOWN': lambda: self._move_down(steps),
            'RIGHT': lambda: self._move_right(steps),
            'LEFT': lambda: self._move_left(steps)
        }

        chosen_movement = movement.get(direction, lambda: self._invalid_movement())
        chosen_movement()

    def _move_up(self, steps: float):
        self.y_coordinate = self.y_coordinate + steps

    def _move_down(self, steps: float):
        self.y_coordinate = self.y_coordinate - steps

    def _move_right(self, steps: float):
        self.x_coordinate = self.x_coordinate + steps

    def _move_left(self, steps: float):
        self.x_coordinate = self.x_coordinate - steps

    @staticmethod
    def _invalid_movement():
        raise ValueError('Invalid Movement')

    @property
    def x_coordinate(self) -> float:
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, new_x_coordinate: float):
        self._x_coordinate = new_x_coordinate

    @property
    def y_coordinate(self) -> float:
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, new_y_coordinate: float):
        self._y_coordinate = new_y_coordinate
