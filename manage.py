#!/usr/bin/env python
import os
import sys
import signal


def sighandler(signum, frame):
    """
    Speed up exit under Docker.
    http://blog.lotech.org/fix-djangos-runserver-when-run-under-docker-or-pycharm.html
    """
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tallessa_backend.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
