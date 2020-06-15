from ATE.org.actions_on.die.DieWizard import DieWizard
from enum import Enum

import os
import re


class ErrorMessage(Enum):
    NoValidConfiguration = "no valid configuration"
    InvalidConfigurationElements = "configuration does not match the template inside constants.py"

    def __call__(self):
        return self.value


class ViewDieWizard(DieWizard):
    def __init__(self, name, project_info):
        super().__init__(project_info)
        self._setup_view(name)
        ViewDieWizard._setup_dialog_fields(self, name)

    def _setup_view(self, name):
        self.setWindowTitle(' '.join(re.findall('.[^A-Z]*', os.path.basename(__file__).replace('.py', ''))))

        self.withHardware.setEnabled(False)
        self.dieName.setEnabled(False)
        self.fromMaskset.setEnabled(False)
        self.quality.setEnabled(False)
        self.isAGrade.setChecked(True)
        self.isAGrade.setEnabled(False)
        self.referenceGrade.setEnabled(False)
        self.grade.setEnabled(False)
        self.Type.setEnabled(False)
        self.customer.setEnabled(False)

        self.CancelButton.setEnabled(True)
        self.CancelButton.clicked.connect(self.accept)
        self.feedback.setText("")

    @staticmethod
    def _setup_dialog_fields(dialog, name):
        configuration = dialog.project_info.get_die(name)
        if len(configuration) < 8:
            dialog.feedback.setText(ErrorMessage.InvalidConfigurationElements())

        dialog.dieName.setText(name)
        dialog.withHardware.setCurrentText(configuration[0])
        dialog.fromMaskset.setCurrentText(configuration[1])
        if not configuration[2] == 'A':
            dialog.isAGrade.setChecked(False)
            dialog.grade.setHidden(False)
            dialog.gradeLabel.setHidden(False)
            dialog.gradeLabel.setEnabled(True)
            dialog.referenceGrade.setHidden(False)
            dialog.referenceGradeLabel.setHidden(False)
            dialog.referenceGradeLabel.setEnabled(True)

        dialog.grade.setCurrentText(configuration[2])
        dialog.referenceGrade.setCurrentText(configuration[3])
        dialog.quality.setCurrentText(configuration[4])

        if configuration[5] == 'ASSP':
            dialog.Type.setCurrentText('ASSP')
        else:
            dialog.Type.setCurrentText(configuration[5])
            dialog.customer.setText(configuration[6])
            dialog.customer.setHidden(False)
            dialog.customerLabel.setHidden(False)
            dialog.customerLabel.setEnabled(True)

        dialog.feedback.setText('')
        dialog.OKButton.setEnabled(True)
        dialog.isAGrade.setEnabled(False)

    def _connect_event_handler(self):
        pass


def display_die_settings_dialog(name, project_info):
    view_wizard = ViewDieWizard(name, project_info)
    view_wizard.exec_()
    del(view_wizard)
