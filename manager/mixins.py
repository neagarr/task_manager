from manager.forms import SearchForm


class ContextMixin:
    def get_context_data_mixin(self, context):
        title = self.request.GET.get("title", "")
        context["title"] = title
        context["search_form"] = SearchForm(
            initial={"title": title}
        )
        return context


class QuerysetMixin:
    def get_queryset_mixin(self, queryset):
        title = self.request.GET.get("title")
        if title:
            if "username" in self.model.__dict__.keys():
                return queryset.filter(username__icontains=title)
            elif "name" in self.model.__dict__.keys():
                return queryset.filter(name__icontains=title)
        return queryset
