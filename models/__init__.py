#!/usr/bin/python3
""" creates a unique instance of filestorage """
from engine.filestorage import FileStorage


storage = FileStorage()
storage.reload()
