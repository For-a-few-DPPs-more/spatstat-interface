import rpy2.robjects.packages as rpackages

from spatstat_interface.utils import install_r_package


class SpatstatInterface:
    """Interface the ``spatstat`` R package, subpackages and extensions `github.com/spatstat <https://github.com/spatstat/spatstat>`_ using `rpy2 <https://rpy2.github.io>`_.

    Attributes are associated to the corresponding subpackages and extensions.

    .. code-block:: python

        spatstat = SpatstatInterface()
        # spatstat.core is None
        # spatstat.geom is None
        # ...

    See :py:meth:`~spatstat_interface.interface.SpatstatInterface.import_package` to load/import the corresponding subpackages/extensions.
    """

    SUBPACKAGES = ("core", "data", "geom", "linnet", "sparse", "spatstat", "utils")
    EXTENSIONS = ("gui", "Knet", "local", "sphere")

    def __init__(self, update=False):
        """Initialize the interface with the ``spatstat`` R package `github.com/spatstat <https://github.com/spatstat/spatstat>`_.

        Attributes associated with the corresponding subpackages and extensions and initialized to None.

        .. note::

            The ``update`` argument has no effect, it is just kept for retro-compatibility.
        """
        for pkg in self.SUBPACKAGES + self.EXTENSIONS:
            setattr(self, pkg, None)

    def import_package(self, *names, update=False):
        """Import spatstat subpackages or extensions given by ``names``, made accessible via the corresponding ``.name`` attribute.
        If the package is already present is it updated according to ``update`` otherwise it is installed.

        The list of subpackages and extensions is available

        - via the attributes :py:attr:`~spatstat_interface.interface.SpatstatInterface.SUBPACKAGES` and :py:attr:`~spatstat_interface.interface.SpatstatInterface.EXTENSIONS`
        - at `github.com/spatstat <https://github.com/spatstat/spatstat>`_

        .. code-block:: python

            spatstat = SpatstatInterface()
            spatstat.import_package("core", "geom", update=False)
            spatstat.core  # .your_favorite_function from spatstat.core
            spatstat.geom  # .your_favorite_function from spatstat.geom

        .. seealso::

            :py:meth:`~spatstat_interface.utils.install_r_package`
        """
        self.check_package_name(*names)
        spatstat = "spatstat"
        for name in names:
            pkg = spatstat if name == spatstat else f"{spatstat}.{name}"
            install_r_package(pkg, update=update)
            setattr(self, name, rpackages.importr(pkg))

    def check_package_name(self, *names):
        """Check whether ``names`` are valid ``spatstat`` subpackages or extensions. The list of subpackages and extensions is available

        - via the attributes :py:attr:`~spatstat_interface.interface.SpatstatInterface.SUBPACKAGES` and :py:attr:`~spatstat_interface.interface.SpatstatInterface.EXTENSIONS`
        - at `github.com/spatstat <https://github.com/spatstat/spatstat>`_

        .. code-block:: python

            spatstat = SpatstatInterface()
            spatstat.check_package_name("core", "geom")
        """
        wrong_names = set(names).difference(self.SUBPACKAGES + self.EXTENSIONS)
        if wrong_names:
            raise ValueError(
                f"{wrong_names} are invalid spatstat subpackages {self.SUBPACKAGES} or extensions {self.EXTENSIONS}."
            )
