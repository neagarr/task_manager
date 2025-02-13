from manager.forms import SearchForm


# class ContextMixin:
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(TaskTypeListView, self).get_context_data(**kwargs)
#         title = self.request.GET.get("title", "")
#         context["title"] = title
#         context["search_form"] = SearchForm(
#             initial={"title": title}
#         )
#         return context


# class QuerysetMixin:
#     def __init__(self, name, queryset):
#         super().__init__(name, queryset)
#
#     @staticmethod
#     def get_queryset():
#         title = super().request.GET.get("title")
#         if title:
#             return queryset.filter(name__icontains=title)
#         return queryset


class QuerysetMixin:
    def get_queryset_mixin(self, queryset):
        title = self.request.GET.get("title")
        if title:
            if "username" in self.model.__dict__.keys():
                return queryset.filter(username__icontains=title)
            elif "name" in self.model.__dict__.keys():
                return queryset.filter(name__icontains=title)
        return queryset
