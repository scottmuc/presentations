import subprocess


class CommandRunner:
    def run(self, dirpath, command, *args):
        self.subprocess = subprocess.Popen([command, *args], cwd=dirpath, stdout=subprocess.PIPE, text=True)
        self.subprocess.wait()

    def capture_output_from_command(self, dirpath, command, *args) -> str:
        self.run(dirpath, command, *args)
        stdout, stderr = self.subprocess.communicate()
        log_output = stdout.strip()
        if self.subprocess.returncode != 0:
            raise RuntimeError(f"Command failed: {command}, stderr: {stderr}")
        return log_output
