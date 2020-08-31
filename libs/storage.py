from libs.config import config
import subprocess
# import os
# import shutil
# # import StringIO
# import tempfile
# import time
import re
import tempfile

def _doit(cmd):
    print(f"Running Command {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode > 0:
        return False
    return True

class Storage:
    def __init__(self):
        self.type = re.split("://", config.storage.source_db, 1)
        self.destination_db = re.split("^sqlite://", config.database.connection,1)[1]
        if not self.destination_db:
            assert ("config.database.connection is not defined as sqlite:///path/to/file")

    def get_db(self):
        tfile = tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
        if "gs" in self.type:
            lock_check_cmd = f"/usr/bin/gsutil ls {config.storage.source_db}.lockfile"
            make_lockfile_cmd = f"/usr/bin/gsutil cp {tfile[1]} {config.storage.source_db}.lockfile"

        assert not _doit(lock_check_cmd),f"Lockfile found {config.storage.source_db}.lockfile"
        assert _doit(make_lockfile_cmd), f"Failed to create lockfile {config.storage.source_db}.lockfile"
        
        return True

    def put_db(self):
        if "gs" in self.type:
            put_cmd = f"gsutil cp {self.destination_db} {config.storage.source_db}"
            remove_lockfile_cmd = f"/usr/bin/gsutil rm {config.storage.source_db}.lockfile"

        assert _doit(put_cmd), f"Failed to put {config.storage.source_db}"
        assert _doit(remove_lockfile_cmd),f"Failed to remove lockfile {config.storage.source_db}.lockfile"

        return True
