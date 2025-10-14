from django.shortcuts import render,redirect
from django.views import View
from chef.forms import recipeform
from chef.langchain import askchef

class home(View):
    def get(self,req):
         #get the session
        ai_recipe = req.session.get('ai_recipe','')
        form= recipeform()
        return render(req,'chef/home.html',{'form':form,'ai_recipe': ai_recipe})
        
    

    def post(self,req):
        form= recipeform(req.POST)
        if form.is_valid():
           
            #extrating a message that we are given in form
            recipe_message=form.cleaned_data['recipe_message']
            ai_res_recipe=askchef(recipe_message)
            #it will the store the session i.e the recipe ask by user
            req.session['ai_recipe']= ai_res_recipe
        form = recipeform()
        return redirect('/')
    


