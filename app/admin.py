
from django.contrib import admin
from grappelli.forms import GrappelliSortableHiddenMixin

from .models import Invoice, InvoiceItem, TaxRate


class TaxRateAdmin(admin.ModelAdmin):
    model = TaxRate


class InvoiceItemInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = InvoiceItem

    fields = ('quantity', 'description', 'unit_price', 'tax_rate', 'position')

    sortable_field_name = 'position'
    sortable_excludes = ('quantity', 'description', 'unit_price', 'tax_rate', )

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, ]
    fieldsets = (
        (None, {
            'fields': ('client', )
        }),
    )
    search_fields = ('client__username', )
    list_display = (
        'invoice_date',
        'client',
    )
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(TaxRate, TaxRateAdmin)
