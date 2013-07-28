from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from recipes.models import Powder,Recipe,Hull,HullLength,Wad,Primer,Gauge

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

		gaugefilter      = self.intmap( 'gauge',      Gauge )
		wadfilter        = self.intmap( 'wad',        Wad )
		hullfilter       = self.intmap( 'hull',       Hull )
		hulllengthfilter = self.intmap( 'hulllength', HullLength )
		primerfilter     = self.intmap( 'primer',     Primer )
		powderfilter     = self.intmap( 'powder',     Powder )

		retn['Gauge']      = Gauge.objects.filter(id__in=gaugefilter).order_by('size')
		retn['Hull']       = Hull.objects.filter(gauge__in=gaugefilter).order_by('manufacturer','gauge')
		retn['HullLength'] = HullLength.objects.all()
		retn['Primer']     = Primer.objects.order_by('manufacturer')
		retn['Powder']     = Powder.objects.order_by('manufacturer','name')
		retn['Wad']        = Wad.objects.order_by('manufacturer','name')
		retn['Recipe']     = Recipe.objects.filter(
			hull__in=hullfilter,
			hullLength__in=hulllengthfilter,
			primer__in=primerfilter,
			powder__in=powderfilter
			wad__in=wadfilter,
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
