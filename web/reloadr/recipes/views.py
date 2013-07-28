from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from recipes.models import Powder,Recipe,Hull,Wad,Primer,Gauge

import operator

def intmap( list ):
	return [ int(x) for x in list ]

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'recipes/index.html'
	context_object_name = 'table'

	def get_queryset(self):
		"""Get everything needed for index page"""
		retn={}

		gaugefilter  = intmap( self.request.GET.getlist('gauge') )
		wadfilter    = intmap( self.request.GET.getlist('wad') )
		hullfilter   = intmap( self.request.GET.getlist('hull') )
		primerfilter = intmap( self.request.GET.getlist('primer') )
		powderfilter = intmap( self.request.GET.getlist('powder') )

		if len(gaugefilter) > 0:
			retn['Gauge'] = Gauge.objects.filter(id__in=gaugefilter).order_by('size')
		else:
			retn['Gauge'] = Gauge.objects.order_by('size')

		if len(gaugefilter) > 0:
			retn['Hull']   = Hull.objects.filter(gauge__in=gaugefilter).order_by('manufacturer','gauge')
		else:
			retn['Hull']   = Hull.objects.order_by('manufacturer','gauge')

		retn['Primer'] = Primer.objects.order_by('manufacturer')
		retn['Powder'] = Powder.objects.order_by('manufacturer','name')
		retn['Wad']    = Wad.objects.order_by('manufacturer','name')

		if len(wadfilter)>0:
			retn['Recipe'] = Recipe.objects.filter(wad__in=wadfilter).order_by('gauge','powder')
		else:
			retn['Recipe'] = Recipe.objects.order_by('gauge','powder')

		return retn;

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipe.objects
#        return .objects.filter(pub_date__lte=timezone.now())
