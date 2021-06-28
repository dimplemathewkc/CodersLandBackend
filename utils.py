import subprocess
import sys
import os
from loguru import logger
class RunCode(object):
    def __init__(self, code=None):
        self.code = code
        logger.debug(code)
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_code(self, cmd="code.py"):
        cmd = [sys.executable, cmd]
        logger.debug(cmd)
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
        logger.debug(output)
        result = output.wait()
        out, err = output.communicate()
        self.stderr, self.stdout = err.decode("utf=8"), out.decode("utf-8")
        return result

    def run_code(self, code=None):
        file = '.resource/code.py'
        # /Users/dimplemathew/PycharmProjects/coderLand/coderLand/resource
        if not code:
            code = self.code
        with open(file,"w") as f:
            f.write(code)
        self._run_code(file)
        return self.stderr,self.stdout
