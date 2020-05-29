from ATE.org.actions_on.product.NewProductWizard import NewProductWizard
from ATE.org.actions_on.product.ViewProductWizard import ViewProductWizard
import re
import os


class EditProductWizard(NewProductWizard):
    def __init__(self, project_info, name):
        super().__init__(project_info, read_only=True)
        self.ProductName.setEnabled(False)
        self.setWindowTitle(' '.join(re.findall('.[^A-Z]*', os.path.basename(__file__).replace('.py', ''))))
        ViewProductWizard._setup_dialog_fields(self, name)

    def OKButtonPressed(self):
        configuration = self._get_actual_defintion()
        self.project_info.update_product(configuration['name'], configuration['device'],
                                         configuration['hardware'])
        self.accept()


def edit_product_dialog(project_info, name):
    edit = EditProductWizard(project_info, name)
    edit.exec_()
    del(edit)
