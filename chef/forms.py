from django import forms

class recipeform(forms.Form):
    recipe_message = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'placeholder':'Ask Your Recipe'}))