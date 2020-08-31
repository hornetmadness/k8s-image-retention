import os
from pathlib import Path
from box import Box

class Config:
    def __init__(self, file=None):
        if not file:
            self.file = "config.yaml"
        else:
            self.file = file
    def read_config(self):
        return Box.from_yaml(filename="config.yaml", default_box=True)

cfg = Config()
config = cfg.read_config()


if 'file_path' not in config.storage:
    assert("config.storage.file_path in not defined in the config")
