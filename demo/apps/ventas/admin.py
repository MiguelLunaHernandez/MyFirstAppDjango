from django.contrib import admin
from demo.apps.ventas.models import cliente,producto,categoriaProducto


class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail', 'precio','stock') # muestra mas campos
	list_filter = ('nombre','precio') # realiza filtros por no mbre y precio
	search_fields = ['nombre', 'precio'] #realiza busquedas 
	fields = ('nombre', 'descripcion',('precio','stock'),'imagen','categoria','status') # solo muestra los campos indicados

admin.site.register(cliente)
admin.site.register(producto, productoAdmin)
admin.site.register(categoriaProducto)
