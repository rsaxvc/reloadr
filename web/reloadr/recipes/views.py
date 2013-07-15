from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from recipes.models import Recipe

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'recipes/index.html'
	context_object_name = 'recipe_list'

	def get_queryset(self):
		"""Return the last five published recipes."""
		return Recipe.objects
#		return Recipe.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipe.objects
#        return .objects.filter(pub_date__lte=timezone.now())
