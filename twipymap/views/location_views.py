from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from twipymap.models import Location


class LocationView(object):
    model = Location

    def get_template_names(self):
        """Nest templates within location directory."""
        tpl = super(LocationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'location'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class LocationDateView(LocationView):
    date_field = 'created_at'
    month_format = '%m'


class LocationBaseListView(LocationView):
    paginate_by = 10


class LocationArchiveIndexView(
    LocationDateView, LocationBaseListView, ArchiveIndexView):
    pass


class LocationCreateView(LocationView, CreateView):
    pass


class LocationDateDetailView(LocationDateView, DateDetailView):
    pass


class LocationDayArchiveView(
    LocationDateView, LocationBaseListView, DayArchiveView):
    pass


class LocationDeleteView(LocationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('twipymap_location_list')


class LocationDetailView(LocationView, DetailView):
    pass


class LocationListView(LocationBaseListView, ListView):
    pass


class LocationMonthArchiveView(
    LocationDateView, LocationBaseListView, MonthArchiveView):
    pass


class LocationTodayArchiveView(
    LocationDateView, LocationBaseListView, TodayArchiveView):
    pass


class LocationUpdateView(LocationView, UpdateView):
    pass


class LocationWeekArchiveView(
    LocationDateView, LocationBaseListView, WeekArchiveView):
    pass


class LocationYearArchiveView(
    LocationDateView, LocationBaseListView, YearArchiveView):
    make_object_list = True



