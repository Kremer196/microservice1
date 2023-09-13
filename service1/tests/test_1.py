import hashlib
import subprocess
import os

def test_valid():
    entrypoint_path = os.path.join('..', 'entrypoint.py')
    process = subprocess.Popen(["python2", entrypoint_path], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                text=True)


    input_data = "md5\nHello Avl\n"
    expected = hashlib.md5(b"Hello Avl").hexdigest()

    stdout, stderr = process.communicate(input_data)
    assert stdout.strip() == expected

