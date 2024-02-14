"""CRUD functions for sessions table"""

from core.memory_db import SESSIONS


def list_sessions():
    """ Returns a list of sessions """
    return list(SESSIONS.values())
