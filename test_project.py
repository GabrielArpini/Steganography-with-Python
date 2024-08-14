import project as p
import pytest
import matplotlib.pyplot as plt
import numpy

def test_get_message():
    img = p.get_img("Zeus.jpeg")
    assert p.get_message("test",img) == "test"

    assert p.get_message("test.txt",img) == "A test!\nLine 2\n"
    with pytest.raises(SystemExit):
        p.get_message("random.txt",img)

def test_get_img():
    with pytest.raises(SystemExit):
        p.get_img("random.png")
    with pytest.raises(SystemExit):
        p.get_img("random.txt")
    img = p.get_img("Zeus.jpeg")
    assert type(img) is numpy.ndarray

def test_get_bin():
    assert p.get_bin("!") == [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert p.get_bin("0") == [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert p.get_bin("") == [0, 0, 0, 0, 0, 0, 0, 0]
    assert p.get_bin("\x00") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_encode():
    img = p.get_img("Zeus.jpeg")
    msg = p.get_message("test.txt",img)
    assert p.encode(img,msg) == 'Message encoded successfully!'
    with pytest.raises(SystemExit):
        p.encode(p.get_img("foo.txt"), p.get_message("This is a test"))

