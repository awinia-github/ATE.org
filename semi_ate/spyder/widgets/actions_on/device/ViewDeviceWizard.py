from ATE.org.actions_on.device.NewDeviceWizard import NewDeviceWizard

import os
import re


class ViewDeviceWizard(NewDeviceWizard):
    def __init__(self, name, project_info):
        super().__init__(project_info)
        self._setup_view(name)
        ViewDeviceWizard._setup_dialog_fields(self, name)

    def _setup_view(self, name):
        self.setWindowTitle(' '.join(re.findall('.[^A-Z]*', os.path.basename(__file__).replace('.py', ''))))

        self.hardware.setEnabled(False)
        self.deviceName.setEnabled(False)
        self.package.setEnabled(False)
        self.availableDies.setEnabled(False)
        self.diesInDevice.setEnabled(False)
        self.listWidget.setEnabled(False)
        self.pinsTable.setEnabled(False)
        self.addPin.setEnabled(False)
        self.removePin.setEnabled(False)
        self.pinUp.setEnabled(False)
        self.pinDown.setEnabled(False)

        self.removeDie.setEnabled(False)
        self.addDie.setEnabled(False)

        self.CancelButton.setEnabled(True)
        self.CancelButton.clicked.connect(self.accept)

    @staticmethod
    def _setup_dialog_fields(dialog, name):
        configuration = dialog.project_info.get_device(name)

        dialog.deviceName.setText(name)
        dialog.hardware.setCurrentText(configuration['hardware'])
        dialog.package.setCurrentText(configuration['package'])
        definition = configuration['definition']
        dialog.diesInDevice.addItems(definition['dies_in_package'])

        dialog.feedback.setText("")
        dialog.OKButton.setEnabled(True)

    def _connect_event_handler(self):
        pass


def display_device_settings_dialog(name, project_info):
    view = ViewDeviceWizard(name, project_info)
    view.exec_()
    del(view)
