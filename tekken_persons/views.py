from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

class PersonsListView(generic.ListView):
    model = models.PersonsGame
    template_name='tekken_game/persons_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return self.model.objects.all()

# def persons_list(request):
#     if request.method == 'GET':
#         persons = models.PersonsGame.objects.all()
#         return render(request, template_name='tekken_game/persons_list.html',
#                       context={'persons' : persons})

class PersonsDetailView(generic.DetailView):
    template_name = 'tekken_game/person_detail.html'
    context_object_name = 'persons_id'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonsGame, id=person_id)

# def persons_detail(request, id):
#     if request.method == 'GET':
#         person_id = get_object_or_404(models.PersonsGame, id=id)
#         return render(request, template_name='tekken_game/person_detail.html',
#                       context={'person_id': person_id})

class CreatePersonView(generic.CreateView):
    template_name = 'tekken_game/crud/create_person.html'
    form_class = forms.TekkenForm
    success_url = '/'
    queryset = models.PersonsGame.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonView, self).form_valid(form=form)

# def create_person_view(request):
#     if request.method == 'POST':
#         form = forms.TekkenForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/">На главную</a>')
#     else:
#         form = forms.TekkenForm()
#     return render(request, template_name='tekken_game/crud/create_person.html',
#                       context={'form':form})


#удаление
class DeletePersonView(generic.DeleteView):
    template_name = 'tekken/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, queryset=None):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonsGame, id=person_id)

# def delete_person_view(id):
#     person_id = get_object_or_404(models.PersonsGame, id=id)
#     person_id.delete()
#     return HttpResponse('Успешно добавлен <a href="/">На главную</a>')

class EditPersonView(generic.UpdateView):
    template_name = 'tekken_game/crud/edit_person.html'
    form_class = forms.TekkenForm
    success_url = '/'
    queryset = models.PersonsGame.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditPersonView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonsGame, id=person_id)

# def edit_person_view(request, id):
#     person_id = get_object_or_404(models.PersonsGame, id=id)
#     if request.method == 'POST':
#         form = forms.TekkenForm(instance=person_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/">На главную</a>')
#     else:
#         form = forms.TekkenForm(instance=person_id)
#     return render(request,
#            template_name='tekken_game/crud/edit_person.html',
#            context={'form': form,
#                     'person_id': person_id})