# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, python_files_for_commit


def python3():
    "Check to see if python files are py3 compatible"
    py_files = str(python_files_for_commit())
    errors = []
    for py_file in py_files.splitlines():
        b = bash('python3 -m py_compile {0}'.format(py_file))
        if b.err:
            errors.append(b.err)
    return "\n".join(errors)
