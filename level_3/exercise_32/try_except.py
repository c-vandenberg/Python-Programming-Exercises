#!/usr/bin/env python3

import logging


class TryExcept:
    @staticmethod
    def divide_by_zero():
        try:
            return 5/0
        except ZeroDivisionError as e:
            print('Cannot divide by zero')
            logging.error(e)
        finally:
            print(
                'The finally block is where you put code that you want to run even if an exception is raised.'
                'For example, resource cleanups, closing database connections, or logging'
            )
            logging.info('TryExcept.divide_by_zero() was called')

