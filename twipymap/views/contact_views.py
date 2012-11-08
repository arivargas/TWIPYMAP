from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from twipymap.models import Contact


class ContactView(object):
    model = Contact

    def get_template_names(self):
        """Nest templates within contact directory."""
        tpl = super(ContactView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'contact'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ContactDateView(ContactView):
    date_field = 'created_at'
    month_format = '%m'


class ContactBaseListView(ContactView):
    paginate_by = 10


class ContactArchiveIndexView(
    ContactDateView, ContactBaseListView, ArchiveIndexView):
    pass


class ContactCreateView(ContactView, CreateView):
    pass


class ContactDateDetailView(ContactDateView, DateDetailView):
    pass


class ContactDayArchiveView(
    ContactDateView, ContactBaseListView, DayArchiveView):
    pass


class ContactDeleteView(ContactView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('twipymap_contact_list')


class ContactDetailView(ContactView, DetailView):
    pass


class ContactListView(ContactBaseListView, ListView):
    pass


class ContactMonthArchiveView(
    ContactDateView, ContactBaseListView, MonthArchiveView):
    pass


class ContactTodayArchiveView(
    ContactDateView, ContactBaseListView, TodayArchiveView):
    pass


class ContactUpdateView(ContactView, UpdateView):
    pass


class ContactWeekArchiveView(
    ContactDateView, ContactBaseListView, WeekArchiveView):
    pass


class ContactYearArchiveView(
    ContactDateView, ContactBaseListView, YearArchiveView):
    make_object_list = True



