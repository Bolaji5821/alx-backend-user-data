#!/usr/bin/env python3
"""
Auth class
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication system template
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A public method that returns False"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """A public method that returns None"""
        if request is None and request.headers.get("Authorization") is None:
            return None
        else:
            return request.headers.get("Authorization")

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method that returns None"""
        return None
