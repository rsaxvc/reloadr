from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from recipes.models import Powder,Recipe,Hull,Length,Wad,Primer,Gauge

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'recipes/index.html'
	context_object_name = 'table'

	def intmap( self, name, table ):
		list = [ int(x) for x in self.request.GET.getlist( name ) ]
		if( len( list ) > 0 ):
			return list
		return [ int(x.id) for x in table.objects.all() ]


	def get_queryset(self):
		"""Get everything needed for index page"""
		retn={}

		gaugefilter  = self.intmap( 'gauge',  Gauge )
		wadfilter    = self.intmap( 'wad',    Wad )
		hullfilter   = self.intmap( 'hull',   Hull )
		lengthfilter = self.intmap( 'length', Length )
		primerfilter = self.intmap( 'primer', Primer )
		powderfilter = self.intmap( 'powder', Powder )

		retn['Gauge']  = Gauge.objects.filter(gauge__in=gaugefilter).order_by('gauge')
		retn['Hull']   = Hull.objects.filter(gauge__in=gaugefilter).order_by('manufacturer','gauge')
		retn['Length'] = Length.objects.all()
		retn['Primer'] = Primer.objects.order_by('manufacturer')
		retn['Powder'] = Powder.objects.order_by('manufacturer','name')
		retn['Wad']    = Wad.objects.filter(gauge__in=gaugefilter).order_by('manufacturer','name')
		retn['Recipe'] = Recipe.objects.filter(
			hull__gauge__in=gaugefilter,
			hull__in=hullfilter,
			length__in=lengthfilter,
			primer__in=primerfilter,
			powder__in=powderfilter,
			wad__in=wadfilter
			).order_by('gauge','powder')

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
