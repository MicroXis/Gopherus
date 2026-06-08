import subprocess
import difflib

USERNAME = "root"
QUERY = "SELECT 1;"

stdin_data = f"{USERNAME}\n{QUERY}\n".encode()

#
# PYTHON 2 (docker)
#
docker_cmd = [
    "docker",
    "run",
    "--rm",
    "-i",
    "gopherus:latest",
    "python",
    "gopherus.py",
    "--exploit",
    "mysql",
]

py2_output = subprocess.check_output(docker_cmd, input=stdin_data)
print(py2_output)

#
# PYTHON 3 (local)
#
stdin_data = f"{USERNAME}\n{QUERY}\n".encode()
py3_cmd = ["python3", "gopherus.py", "--exploit", "mysql"]

py3_output = subprocess.check_output(py3_cmd, input=stdin_data)

#
# COMPARAISON BINAIRE
#
if py2_output == py3_output:
    print("[OK] Payloads identiques")
else:
    print("[FAIL] Payloads différents")

    #
    # Diff lisible
    #
    py2_text = py2_output.decode(errors="replace").splitlines()
    py3_text = py3_output.decode(errors="replace").splitlines()

    diff = difflib.unified_diff(
        py2_text, py3_text, fromfile="python2", tofile="python3", lineterm=""
    )

    print("\n".join(diff))

    #
    # Hexdump utile pour str/bytes
    #
    print("\n=== PY2 HEX ===")
    print(py2_output.hex())

    print("\n=== PY3 HEX ===")
    print(py3_output.hex())
