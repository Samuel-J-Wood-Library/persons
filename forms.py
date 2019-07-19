from dal import autocomplete

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Person, Department, Organization, Role

div_name = Div(
                Div('title',
                    css_class='col-xs-4',
                ),
                Div('first_name',
                    css_class='col-xs-4',
                ),
                Div('last_name',
                    css_class='col-xs-4',
                ),
                css_class="row"
            )
div_preferred = Div(
                    Div('preferred_name',
                        css_class='col-xs-8',
                    ),
                    Div('pronoun',
                        css_class='col-xs-4',
                    ),
                    css_class="row"
                )

class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['pronoun'].label = "Preferred pronoun"
        self.helper = FormHelper()
        self.helper.form_id = 'person-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
                    Fieldset('<div class="alert alert-info">Personal details</div>',
                            div_name,
                            div_preferred,
                            style="font-weight: bold;",
                    ),
                    Fieldset('<div class="alert alert-info">Affiliations</div>',
                            'cwid',
                            'department',
                            'organization',
                            'role',
                            style="font-weight: bold;"
                    ),
                    Fieldset('<div class="alert alert-info">Contact Details</div>',
                            'email_primary',
                            'email_secondary',
                            'phone',
                            'comments',
                            style="font-weight: bold;"
                    ),        
        )
    
    class Meta:
        model = Person
        fields = [  'preferred_name',
                    'title',
                    'first_name', 
                    'last_name', 
                    'pronoun',
                    'cwid', 
                    'department',
                    'organization', 
                    'role', 
                    'email_primary',
                    'email_secondary',
                    'phone',
                    'comments',
                ]

        widgets =  {'department' : autocomplete.ModelSelect2(
                                        url='persons:autocomplete-dept'
                                        ),
                    'organization' : autocomplete.ModelSelect2(
                                        url='persons:autocomplete-org'
                                        ),
                    'role' : autocomplete.ModelSelect2(
                                        url='persons:autocomplete-role'
                                        ),                     
                    }
