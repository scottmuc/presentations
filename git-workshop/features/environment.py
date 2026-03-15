import importlib.util
import pathlib


def before_all(context):
    steps_dir = context.config.userdata.get("steps_dir",
                                            "features/steps/baseline_steps")

    for path in pathlib.Path(steps_dir).glob("*.py"):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
