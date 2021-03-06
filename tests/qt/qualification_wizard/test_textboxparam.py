from PyQt5 import QtCore, QtGui, QtWidgets, uic
from pytestqt.qt_compat import qt_api  # debug prints inside unittests
import ATE.org.actions_on.flow.qualificationwizardbase.wizardbase
import ATE.org.actions_on.flow.qualificationwizardbase
import ATE.org.actions_on.flow.qualificationwizardbase.intparam
from  ATE.org.actions_on.flow.qualificationwizardbase import * 


class TextParamWizard(wizardbase.wizardbase):
    def __init__(self):
        # self.parent = parent
        # Note: The init call needs to come after we setup this variable, in order for
        # it to exist when init calls _get_wizard_params
        self.theParam = textboxparam.TextBoxParam("Parameter1")
        super().__init__({}, None)

    def _get_wizard_parameters(self) -> list:
        return [self.theParam]
        
    def _get_wizard_testprogram_slots(self) -> dict:
        return []


def setup_method():
    def setup(test_func):
        def wrap(qtbot):
            window = TextParamWizard()
            qtbot.addWidget(window)
            return test_func(window, qtbot)
        return wrap
    return setup


@setup_method()
def test_textbox_param_can_find_line_edit(window, qtbot=None):
    paramField = window.findChild(QtWidgets.QLineEdit, "txtParameter1")
    assert paramField is not None


@setup_method()
def test_textbox_param_line_edit_is_populated_with_default_value(window, qtbot=None):
    window.theParam.load_values(dict())
    paramField = window.findChild(QtWidgets.QLineEdit, "txtParameter1")
    assert(paramField.text() == "")


@setup_method()
def test_textbox_param_line_edit_is_populated_from_inserted_data(window, qtbot):
    window.theParam.load_values({"Parameter1": "Foobar"})
    paramField = window.findChild(QtWidgets.QLineEdit, "txtParameter1")
    assert(paramField.text() == "Foobar")

@setup_method()
def test_textbox_param_empty_disables_save_button(window, qtbot):
    paramField = window.findChild(QtWidgets.QLineEdit, "txtParameter1")
    paramField.setText("")
    saveButton = window.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
    assert(saveButton.isEnabled() == False)


@setup_method()
def test_textbox_param_set_param_to_valid_value_enables_button(window, qtbot):
    paramField = window.findChild(QtWidgets.QLineEdit, "txtParameter1")
    paramField.setText("")
    saveButton = window.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
    assert(saveButton.isEnabled() == False)
    qtbot.keyClicks(paramField, "Some Random Value")
    assert(saveButton.isEnabled() == True)


@setup_method()
def test_textbox_param_save_values_stores_value(window, qtbot):
    testParam = ATE.org.actions_on.flow.qualificationwizardbase.textboxparam.TextBoxParam("Parameter32")
    d = {"Parameter32" : "Some Value"}
    testParam.load_values(d)
    d2 = dict()
    testParam.store_values(d2)
    assert(d2["Parameter32"] == "Some Value")