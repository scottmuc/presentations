import subprocess

def capture_output_from_commands(commands, context) -> str:
    p = subprocess.Popen(commands, cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    stdout, stderr = p.communicate()
    log_output = stdout.strip()
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {commands}, stderr: {stderr}")
    return log_output
