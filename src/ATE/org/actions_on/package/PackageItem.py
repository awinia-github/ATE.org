from ATE.org.actions_on.package.NewPackageWizard import new_package_dialog
from ATE.org.actions_on.package.ViewPackageWizard import display_package_settings_dialog
from ATE.org.actions_on.package.EditPackageWizard import edit_package_dialog

from ATE.org.actions_on.model.Constants import MenuActionTypes
from ATE.org.actions_on.model.BaseItem import BaseItem
from ATE.org.actions_on.utils.StateItem import StateItem


class PackageItem(BaseItem):
    def __init__(self, project_info, name, parent=None):
        super().__init__(project_info, name, parent=parent)
        self.child_set = self._get_children_names()

    def _get_children_names(self):
        return self.project_info.get_packages()

    def _create_child(self, name, parent):
        return PackageItemChild(self.project_info, name, parent)

    def _get_menu_items(self):
        return [MenuActionTypes.Add()]

    def new_item(self):
        new_package_dialog(self.project_info)


class PackageItemChild(StateItem):
    def __init__(self, project_info, name, parent=None):
        super().__init__(project_info, name, parent=parent)

    def edit_item(self):
        edit_package_dialog(self.project_info, self.text())

    def display_item(self):
        display_package_settings_dialog(self.text(), self.project_info)

    def _update_item_state(self, enabled):
        self.project_info.update_package_state(self.text(), enabled)
        return enabled

    def is_enabled(self):
        return self.project_info.get_package_state(self.text())

    @property
    def type(self):
        return 'packages'

    @property
    def dependency_list(self):
        return self.project_info.get_dependant_objects_for_package(self.text())
