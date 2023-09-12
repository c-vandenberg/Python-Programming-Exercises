#!/usr/bin/env python3

from typing import Union
import time


class StopWatch:
    def __init__(self):
        self._start_time = None
        self._is_running = False

    def start(self) -> None:
        if not self._is_running:
            self._is_running = True
            self._start_time = time.time()

    def stop(self) -> Union[float, None]:
        if self._is_running:
            self._is_running = False
            return time.time() - self._start_time

        return None

    def reset(self) -> None:
        self._is_running = False
        self._start_time = None
