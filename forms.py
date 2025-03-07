class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'description', author]

  def __init__(self, *args, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'input'})  #adding css atributes ex.  <input class="..."></input>
  
