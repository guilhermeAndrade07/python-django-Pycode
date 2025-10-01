from django import forms
from cars.models import Car


# mesma coisa do código acima mas resumida usando o ModelForm     
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car # Um form em cima da tabela car
        fields = '__all__' # herda todos os campos do model car


    def clean_value(self): # quando for uma validação tem que ter o clean_
        value = self.cleaned_data.get('value') # capturando o valor informado no formulario do campo VALUE 
        if value < 20000: # caso o valor for menor de 20000 tem um erro
            self.add_error('value', 'Valor mínimo do carro deve ser R$20.0000 !!') # Seleciona o campo do erro, e depois informa a mensagem de erro
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975!')
        return factory_year

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if not photo:
            self.add_error('photo', 'Precisa ser adicionada uma foto do Carro!')
        return photo