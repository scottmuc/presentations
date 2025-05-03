import subprocess


class CommandRunner:
    def run(self, dirpath, command, *args) -> str:
        process = subprocess.Popen(
                [command, *args],
                cwd=dirpath,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
        )

        process.wait()

        stdout, stderr = process.communicate()
        output = stdout.strip()
        exitcode = process.returncode

        return CommandResult(output, stderr, exitcode)


class CommandResult:
    def __init__(self, output, stderr, exitcode):
        self.output = output
        self.stderr = stderr
        self.exitcode = exitcode
