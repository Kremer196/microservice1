import hashlib
import subprocess


def test_invalid():
    process = subprocess.Popen(["python2", "entrypoint.py"], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                text=True)


    input_data = "not hash\nHello Avl\n"

    stdout, stderr = process.communicate(input_data)
    assert "Enter valid hash function" in stdout