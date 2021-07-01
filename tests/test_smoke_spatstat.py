from spatstat_interface.interface import SpatstatInterface


def test_smoke_spatstat():
    print("smoke-before")
    spatstat = SpatstatInterface(update=False)
    print("smoke-after")
