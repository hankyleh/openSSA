import subprocess
import shutil
import sysconfig
from pathlib import Path
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class MakeBuildExt(build_ext):
    def build_extensions(self):
        # Run make in the source directory, which produces the .so there
        subprocess.check_call(["make", "-C", "src/openSSA"])

        # Determine the .so filename make produced (e.g. _openSSA.cpython-314-...)
        suffix = sysconfig.get_config_var("EXT_SUFFIX")
        built = Path("src/openSSA") / f"_openSSA{suffix}"

        # Setuptools expects the .so at a path inside its build-lib temp dir.
        # get_ext_fullpath gives us that expected path; we copy there so
        # setuptools can then install it normally.
        dest = Path(self.get_ext_fullpath("openSSA._openSSA"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(built, dest)


setup(
    ext_modules=[Extension("openSSA._openSSA", sources=[])],
    cmdclass={"build_ext": MakeBuildExt},
)
