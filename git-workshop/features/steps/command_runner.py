import subprocess


class CommandRunner:
    def run(self, dirpath, command):
        self.subprocess = subprocess.Popen(command, cwd=dirpath, stdout=subprocess.PIPE, text=True)
        self.subprocess.wait()

    def capture_output_from_commands(self, dirpath, command) -> str:
        self.run(dirpath, command)
        stdout, stderr = self.subprocess.communicate()
        log_output = stdout.strip()
        if self.subprocess.returncode != 0:
            raise RuntimeError(f"Command failed: {command}, stderr: {stderr}")
        return log_output
