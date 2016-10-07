#!/usr/bin/env python
# -*- coding utf-8 -*-
""" this is a docstring """


import datetime


CURDATE = None


def get_current_date():
    """gets the current date.

    Args:
        This does not need any parameters.

    Returns:
        Date: Return current date.

    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
