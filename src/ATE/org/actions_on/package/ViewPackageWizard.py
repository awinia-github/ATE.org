from ATE.org.actions_on.package.NewPackageWizard import NewPackageWizard
from enum import Enum

import os
import re


class ViewPackageWizard(NewPackageWizard):
    def __init__(self, name, project_info):
        super().__init__(project_info)
        self._setup_view(name)
        ViewPackageWizard._setup_dialog_fields(self, name)

    def _setup_view(self, name):
        self.setWindowTitle(' '.join(re.findall('.[^A-Z]*', os.path.basename(__file__).replace('.py', ''))))

        self.packageName.setEnabled(False)
        self.leads.setEnabled(False)
        self.findOnFilesystem.setEnabled(False)
        self.isNakedDie.setEnabled(False)

    @staticmethod
    def _setup_dialog_fields(dialog, name):
        configuration = dialog.project_info.get_package(name)
        if configuration is None:
            return

        dialog.packageName.setText(name)
        dialog.leads.setValue(configuration[0])
        dialog.feedback.setText("")
        dialog.isNakedDie.setChecked(dialog.project_info.is_package_a_naked_die(name))

        dialog.OKButton.setEnabled(True)
        dialog.OKButton.clicked.connect(dialog.accept)
        dialog.CancelButton.setEnabled(True)
        dialog.CancelButton.clicked.connect(dialog.reject)

    def _connect_event_handler(self):
        pass


def display_package_settings_dialog(name, project_info):
    view = ViewPackageWizard(name, project_info)
    view.exec_()
    del(view)
