import hashlib
import subprocess
import os


def test_invalid():
    entrypoint_path = os.path.join('..', 'entrypoint.py')
    process = subprocess.Popen(["python2", entrypoint_path], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                text=True)


    input_data = "not hash\nHello Avl\n"

    stdout, stderr = process.communicate(input_data)
    assert "Enter valid hash function" in stdout