from django.forms import ModelChoiceField
from django.utils.safestring import mark_safe

class InputWithPlusButton(ModelChoiceField):
    def render(self, name, value, attrs=None):
        output = []
        output.append(super(ModelChoiceField, self).render(name, value, attrs))
        output.append(u'<i class="fa fa-plus" onclick="{}" aria-hidden="true"></i>'.format(attrs))
        return mark_safe(u''.join(output))
