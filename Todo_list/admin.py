from datetime import date, timedelta
from django.contrib import admin
from .models import ToDoItem, Tag
from django.utils.translation import gettext_lazy as _
from .forms import ToDoItemForm

# Register your models here.

class StatusFilter(admin.SimpleListFilter):
    title = _('Status')  # Display name for the filter
    parameter_name = 'status'  # URL parameter name for the filter
    # _ is for rendering filter in default user language
    def lookups(self, request, model_admin):
        return (
            ('open', _('Open')),
            ('working', _('Working')),
            ('done', _('Done')),
            ('overdue', _('Overdue')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'open':
            return queryset.filter(status='OPEN')
        if self.value() == 'working':
            return queryset.filter(status='WORKING')
        if self.value() == 'done':
            return queryset.filter(status='DONE')
        if self.value() == 'overdue':
            return queryset.filter(status='OVERDUE')
        
class DueDateFilter(admin.SimpleListFilter):
    title = _('Due Date')
    parameter_name = 'due_date'

    def lookups(self, request, model_admin):
        return (
            ('any_date', _('Any date')),
            ('today', _('Today')),
            ('past_7_days', _('Past 7 days')),
            ('this_month', _('This month')),
            ('this_year', _('This year')),
            ('no_date', _('No date')),
            ('has_date', _('Has date')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'any_date':
            return queryset
        elif self.value() == 'today':
            return queryset.filter(due_date=date.today())
        elif self.value() == 'past_7_days':
            past_date = date.today() - timedelta(days=7)
            return queryset.filter(due_date__gte=past_date)
        elif self.value() == 'this_month':
            return queryset.filter(due_date__month=date.today().month)
        elif self.value() == 'this_year':
            return queryset.filter(due_date__year=date.today().year)

class ToDoItemAdmin(admin.ModelAdmin):
    form = ToDoItemForm
    list_filter = (StatusFilter, DueDateFilter)
    list_display = ('title', 'timestamp', 'due_date', 'status')
    search_fields = ('title', 'description')
    ordering = ('-timestamp','-due_date')
    list_per_page = 10
    filter_horizontal = ('tags',)
    fieldsets = (
        ('Mandatory Information', {
            'fields': ('title', 'description', 'status')
        }),
        ('Optional Information', {
            'fields': ('due_date', 'tags',)
        }),
    )

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_todo_items')
    search_fields = ('title', 'description')

    def get_todo_items(self, obj):
        todo_items = obj.todoitem_set.all()
        return ', '.join(todo_item.title for todo_item in todo_items)

    get_todo_items.short_description = 'ToDo Items'


admin.site.register(ToDoItem, ToDoItemAdmin)
admin.site.register(Tag, TagAdmin)

