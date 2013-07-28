from django.contrib import admin
import recipes.models

admin.site.register(recipes.models.Gauge)
admin.site.register(recipes.models.Length)
admin.site.register(recipes.models.Hull)
admin.site.register(recipes.models.Manufacturer)
admin.site.register(recipes.models.Powder)
admin.site.register(recipes.models.Primer)
admin.site.register(recipes.models.Recipe)
admin.site.register(recipes.models.ShotType)
admin.site.register(recipes.models.ShotWeight)
admin.site.register(recipes.models.Wad)

