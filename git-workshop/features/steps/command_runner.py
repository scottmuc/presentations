import subprocess


class CommandRunner:
    def capture_output_from_command(self, dirpath, command, *args) -> str:
        self.subprocess = subprocess.Popen([command, *args], cwd=dirpath, stdout=subprocess.PIPE, text=True)
        self.subprocess.wait()
        stdout, stderr = self.subprocess.communicate()
        log_output = stdout.strip()
        if self.subprocess.returncode != 0:
            raise RuntimeError(f"Command failed: {command}, stderr: {stderr}")
        return log_output
