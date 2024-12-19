import subprocess


class CommandRunner:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def run(self, commands):
        self.subprocess = subprocess.Popen(commands, cwd=self.dirpath, stdout=subprocess.PIPE, text=True)
        self.subprocess.wait()

    def capture_output_from_commands(self, commands) -> str:
        self.run(commands)
        stdout, stderr = self.subprocess.communicate()
        log_output = stdout.strip()
        if self.subprocess.returncode != 0:
            raise RuntimeError(f"Command failed: {commands}, stderr: {stderr}")
        return log_output
