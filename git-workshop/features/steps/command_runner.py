import subprocess


class CommandRunner:
    def capture_output_from_command(self, dirpath, command, *args) -> str:
        self.subprocess = subprocess.Popen([command, *args], cwd=dirpath, stdout=subprocess.PIPE, text=True)
        self.subprocess.wait()

        stdout, stderr = self.subprocess.communicate()
        self.output = stdout.strip()
        self.returncode = self.subprocess.returncode

        return self.output
