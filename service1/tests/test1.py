import hashlib
import subprocess

def test_valid():
    process = subprocess.Popen(["python2", "entrypoint.py"], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                text=True)


    input_data = "md5\nHello Avl\n"
    expected = hashlib.md5(b"Hello Avl").hexdigest()

    stdout, stderr = process.communicate(input_data)
    assert stdout.strip() == expected

