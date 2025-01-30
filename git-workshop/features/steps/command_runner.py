import subprocess


class CommandRunner:
    def run(self, dirpath, command, *args) -> str:
        process = subprocess.Popen([command, *args], cwd=dirpath, stdout=subprocess.PIPE, text=True)
        process.wait()

        stdout, stderr = process.communicate()
        output = stdout.strip()
        returncode = process.returncode

        return {"output": output, "exitcode": returncode }

