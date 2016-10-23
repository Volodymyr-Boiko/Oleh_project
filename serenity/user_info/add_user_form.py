from django.forms import ModelForm
from models import User_info


class AddUserForm(ModelForm):
    class Meta:
        model = User_info
        fields = ['name', 'second_name', 'last_name', 'age', 'sex', 'picture']