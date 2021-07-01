from spatstat_interface.interface import SpatstatInterface


def test_install_spatstat():
    spatstat = SpatstatInterface(update=True)
    assert True
