# -*- coding: utf-8 -*-

import sys
from random import uniform
from os.path import join
from numpy import pi

from PySide2 import QtWidgets
from PySide2.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.GUI.Dialog.DMachineSetup.SSkew.SSkew import SSkew
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


class TestSSkew(object):
    """Test that the widget SSkew behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Create widget before each test"""
        self.machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
        self.widget = SSkew(machine=self.machine, material_dict=None, is_stator=False)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget init is correct"""
        assert self.widget.machine.rotor.skew is None
        assert self.widget.machine.stator.skew is None
        assert not self.widget.g_activate.isChecked()
        # Check default skew setup
        self.widget.g_activate.setChecked(True)
        assert self.widget.machine.stator.skew is None
        assert self.widget.machine.rotor.skew.rate == 1
        assert self.widget.machine.rotor.skew.is_step
        assert self.widget.machine.rotor.skew.Nstep == 3
        assert self.widget.machine.rotor.skew.type_skew == "linear"
        assert self.widget.machine.rotor.skew.angle_list == [
            -3.75 * pi / 180,
            0,
            3.75 * pi / 180,
        ]

        assert self.widget.cb_type.currentText() == "Linear"
        assert self.widget.cb_step.currentText() == "Step"
        assert self.widget.sb_nslice.value() == 3
        assert self.widget.lf_angle.value() == 7.5
        assert (
            self.widget.in_slot_pitch.text()
            == "Stator slot pitch =7.5 [°] / Skew rate = 100%"
        )
        assert self.widget.tab_angle.rowCount() == 3
        assert (
            self.widget.tab_angle.cellWidget(
                0,
                0,
            ).value()
            == -3.75
        )
        assert (
            self.widget.tab_angle.cellWidget(
                1,
                0,
            ).value()
            == 0
        )
        assert (
            self.widget.tab_angle.cellWidget(
                2,
                0,
            ).value()
            == 3.75
        )

    def test_set_continuous(self):
        """Check that you can set a continuous skew"""
        self.widget.g_activate.setChecked(True)
        self.widget.cb_type.setCurrentIndex(1)
        assert self.widget.machine.rotor.skew.type_skew == "vshape"
        self.widget.cb_step.setCurrentIndex(1)

        assert self.widget.machine.stator.skew is None
        assert self.widget.machine.rotor.skew.rate == 1
        assert not self.widget.machine.rotor.skew.is_step
        assert self.widget.machine.rotor.skew.Nstep == 2
        assert self.widget.machine.rotor.skew.type_skew == "linear"
        assert self.widget.machine.rotor.skew.angle_list == [
            -3.75 * pi / 180,
            3.75 * pi / 180,
        ]

        assert self.widget.cb_type.currentText() == "Linear"
        assert self.widget.cb_step.currentText() == "Continuous"
        assert self.widget.sb_nslice.isHidden()
        assert self.widget.lf_angle.value() == 7.5
        assert (
            self.widget.in_slot_pitch.text()
            == "Stator slot pitch =7.5 [°] / Skew rate = 100%"
        )
        assert self.widget.tab_angle.rowCount() == 2
        assert (
            self.widget.tab_angle.cellWidget(
                0,
                0,
            ).value()
            == -3.75
        )
        assert (
            self.widget.tab_angle.cellWidget(
                1,
                0,
            ).value()
            == 3.75
        )

    def test_set_user_defined(self):
        """Check that you can set a continuous skew"""
        self.widget.g_activate.setChecked(True)
        self.widget.cb_type.setCurrentIndex(3)
        assert self.widget.machine.rotor.skew.type_skew == "user-defined"
        self.widget.sb_nslice.setValue(4)
        self.widget.sb_nslice.editingFinished.emit()

        assert self.widget.tab_angle.rowCount() == 4
        self.widget.tab_angle.cellWidget(
            0,
            0,
        ).setValue(1)
        self.widget.tab_angle.cellWidget(
            1,
            0,
        ).setValue(2)
        self.widget.tab_angle.cellWidget(
            2,
            0,
        ).setValue(3)
        self.widget.tab_angle.cellWidget(
            3,
            0,
        ).setValue(4)
        self.widget.tab_angle.cellWidget(
            3,
            0,
        ).editingFinished.emit()

        assert self.widget.machine.stator.skew is None
        assert self.widget.machine.rotor.skew.is_step
        assert self.widget.machine.rotor.skew.Nstep == 4
        assert self.widget.machine.rotor.skew.angle_list == [
            1 * pi / 180,
            2 * pi / 180,
            3 * pi / 180,
            4 * pi / 180,
        ]


if __name__ == "__main__":
    a = TestSSkew()
    a.setup_class()
    a.setup_method()
    a.test_set_user_defined()
    print("Done")
