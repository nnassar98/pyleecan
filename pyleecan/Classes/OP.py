# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/OP.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/OP
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.OP.get_machine_from_parent import get_machine_from_parent
except ImportError as error:
    get_machine_from_parent = error


from ._check import InitUnKnowClassError


class OP(FrozenClass):
    """Define the Operating Point of the simulation"""

    VERSION = 1

    # cf Methods.Simulation.OP.get_machine_from_parent
    if isinstance(get_machine_from_parent, ImportError):
        get_machine_from_parent = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OP method get_machine_from_parent: "
                    + str(get_machine_from_parent)
                )
            )
        )
    else:
        get_machine_from_parent = get_machine_from_parent
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        N0=None,
        felec=None,
        Tem_av_ref=None,
        Pem_av_ref=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.N0 = N0
        self.felec = felec
        self.Tem_av_ref = Tem_av_ref
        self.Pem_av_ref = Pem_av_ref

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OP_str = ""
        if self.parent is None:
            OP_str += "parent = None " + linesep
        else:
            OP_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OP_str += "N0 = " + str(self.N0) + linesep
        OP_str += "felec = " + str(self.felec) + linesep
        OP_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        OP_str += "Pem_av_ref = " + str(self.Pem_av_ref) + linesep
        return OP_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.N0 != self.N0:
            return False
        if other.felec != self.felec:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Pem_av_ref != self.Pem_av_ref:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._N0 != self._N0:
            diff_list.append(name + ".N0")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if other._Tem_av_ref != self._Tem_av_ref:
            diff_list.append(name + ".Tem_av_ref")
        if other._Pem_av_ref != self._Pem_av_ref:
            diff_list.append(name + ".Pem_av_ref")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.N0)
        S += getsizeof(self.felec)
        S += getsizeof(self.Tem_av_ref)
        S += getsizeof(self.Pem_av_ref)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        OP_dict = dict()
        OP_dict["N0"] = self.N0
        OP_dict["felec"] = self.felec
        OP_dict["Tem_av_ref"] = self.Tem_av_ref
        OP_dict["Pem_av_ref"] = self.Pem_av_ref
        # The class name is added to the dict for deserialisation purpose
        OP_dict["__class__"] = "OP"
        return OP_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N0 = None
        self.felec = None
        self.Tem_av_ref = None
        self.Pem_av_ref = None

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "float")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: float
        """,
    )

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "float")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""Electrical Frequency

        :Type: float
        """,
    )

    def _get_Tem_av_ref(self):
        """getter of Tem_av_ref"""
        return self._Tem_av_ref

    def _set_Tem_av_ref(self, value):
        """setter of Tem_av_ref"""
        check_var("Tem_av_ref", value, "float")
        self._Tem_av_ref = value

    Tem_av_ref = property(
        fget=_get_Tem_av_ref,
        fset=_set_Tem_av_ref,
        doc=u"""Theorical Average Electromagnetic torque

        :Type: float
        """,
    )

    def _get_Pem_av_ref(self):
        """getter of Pem_av_ref"""
        return self._Pem_av_ref

    def _set_Pem_av_ref(self, value):
        """setter of Pem_av_ref"""
        check_var("Pem_av_ref", value, "float")
        self._Pem_av_ref = value

    Pem_av_ref = property(
        fget=_get_Pem_av_ref,
        fset=_set_Pem_av_ref,
        doc=u"""Theorical Average Electromagnetic Power

        :Type: float
        """,
    )
