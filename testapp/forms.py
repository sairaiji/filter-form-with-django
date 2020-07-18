from django import forms
from .models import GENDER_CHOICES, AGE, HEIGHT, BODY_SHAPE,JOB, YEARLY_INCOME, HOLIDAYS, EDUCATION, LIVING_IN, ALCOHOL, CIGARETTE

GENDER_CHOICES =  [('', 'こだわらない')] + GENDER_CHOICES
AGE = [('', 'こだわらない')] + AGE
HEIGHT = [('', 'こだわらない')] + HEIGHT
BODY_SHAPE = [('', 'こだわらない')] + BODY_SHAPE 
JOB = [('', 'こだわらない')] + JOB
YEARLY_INCOME = [('', 'こだわらない')] + YEARLY_INCOME
HOLIDAYS = [('', 'こだわらない')] + HOLIDAYS
EDUCATION = [('', 'こだわらない')] + EDUCATION
LIVING_IN = [('', 'こだわらない')] + LIVING_IN
ALCOHOL = [('', 'こだわらない')] + ALCOHOL
CIGARETTE = [('', 'こだわらない')] + CIGARETTE

class ProfileSearchForm(forms.Form):
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=False)
    from_age = forms.ChoiceField(label='年齢', choices=AGE, required=False)
    to_age = forms.ChoiceField(label='~', choices=AGE, required=False)
    from_height = forms.ChoiceField(label='身長', choices=HEIGHT, required=False)
    to_height = forms.ChoiceField(label='~', choices=HEIGHT, required=False)
    from_shape = forms.ChoiceField(label='体型', choices=BODY_SHAPE, required=False)
    to_shape = forms.ChoiceField(label='~', choices=BODY_SHAPE, required=False)
    job = forms.ChoiceField(label='職業', choices=JOB, required=False)
    from_income = forms.ChoiceField(label='年収', choices=YEARLY_INCOME, required=False)
    to_income = forms.ChoiceField(label='~', choices=YEARLY_INCOME, required=False)
    holidays = forms.ChoiceField(label='休日', choices=HOLIDAYS, required=False)
    education = forms.ChoiceField(label='学歴', choices=EDUCATION, required=False)
    living_in = forms.ChoiceField(label='居住地', choices=LIVING_IN, required=False)
    alcohol = forms.ChoiceField(label='お酒', choices=ALCOHOL, required=False)
    cigarette = forms.ChoiceField(label='たばこ', choices=CIGARETTE, required=False)


ProfileSearchFormSet = forms.formset_factory(ProfileSearchForm, extra=1)