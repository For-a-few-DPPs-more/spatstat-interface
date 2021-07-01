from spatstat_interface.interface import SpatstatInterface


def test_smoke_install_spatstat():
    spatstat = SpatstatInterface(update=True)
    assert True
