from datetime import date, timedelta

from dal import autocomplete

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .models import Person, Department, Organization, Role
from .forms import PersonForm

####################################
######  AUTOCOMPLETE  VIEWS   ######
####################################

class PersonAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(
                            Q(cwid__istartswith=self.q) | 
                            Q(first_name__istartswith=self.q) |
                            Q(last_name__istartswith=self.q) |
                            Q(preferred_name__istartswith=self.q)
                            )
        return qs

class DeptAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Department.objects.all()

        if self.q:
            qs =  qs.filter(name__icontains=self.q)
        return qs

class OrgAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Organization.objects.all()

        if self.q:
            qs =  qs.filter(
                            Q(name__icontains=self.q) | 
                            Q(short_name__icontains=self.q) 
                            )
        return qs

class RoleAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Role.objects.all()

        if self.q:
            qs =  qs.filter(name__icontains=self.q) 
        return qs

#############################
######  CLASS  VIEWS   ######
#############################

# home index view
class IndexView(PermissionRequiredMixin, generic.ListView):
    template_name = 'persons/index_home.html'
    context_object_name = 'new_people'
    permission_required = 'persons.view_person'
    
    def get_queryset(self):
        # retrieve all Person items created/updated in last month:
        last_month = date.today() + timedelta(days=-30)
        new_people = Person.objects.filter(record_update >= last_month
                                  ).order_by('last_name', 'first_name'
                                  )
        return  new_people

    def get_context_data(self, **kwargs):
        # get counts of all classes
        person_count = Person.objects.count()
        dept_count = Department.objects.count()
        org_count = Organization.objects.count()
        role_count = Role.objects.count()
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'person_count'  :person_count,
            'dept_count'    :dept_count,
            'org_count'     :org_count,
            'role_count'    :role_count,
        })
        return context
 
# index views of person, department and organization:
class IndexPersonView(PermissionRequiredMixin, generic.ListView):
    template_name = 'persons/index_person.html'
    context_object_name = 'person_list'
    permission_required = 'persons.view_person'
    
    def get_queryset(self):
        return  Person.objects.all().order_by('last_name', 'first_name')

class IndexDeptView(PermissionRequiredMixin, generic.ListView):
    template_name = 'persons/index_dept.html'
    context_object_name = 'dept_list'
    permission_required = 'persons.view_department'
    
    def get_queryset(self):
        return  Department.objects.all().order_by('name')

class IndexOrgView(PermissionRequiredMixin, generic.ListView):
    template_name = 'persons/index_org.html'
    context_object_name = 'org_list'
    permission_required = 'persons.view_organization'
    
    def get_queryset(self):
        return  Organization.objects.all().order_by('name')

class IndexRoleView(PermissionRequiredMixin, generic.ListView):
    template_name = 'persons/index_role.html'
    context_object_name = 'role_list'
    permission_required = 'persons.view_role'
    
    def get_queryset(self):
        return  Role.objects.all().order_by('name')
    
# create new entries for person, department and organization:
class CreatePersonView(PermissionRequiredMixin, CreateView):
    permission_required = 'persons.view_person'
    model = Person
    form_class = PersonForm
    fields = [  'preferred_name',
                'title',
                'first_name', 
                'last_name', 
                'pronoun',
                'cwid', 
                'department',
                'organization', 
                'role', 
                'email_primary',
                'email_secondary',
                'phone',
                'comments',
    ]
    success_url = reverse_lazy("person:person-index" )
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CreatePersonView, self).form_valid(form)
        
class CreateDeptView(PermissionRequiredMixin, CreateView):
    permission_required = 'persons.view_department'
    model = Department
    fields = [  'name',
                'classification', 
    ]
    success_url = reverse_lazy("person:dept-index" )
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CreateDeptView, self).form_valid(form)

class CreateOrgView(PermissionRequiredMixin, CreateView):
    permission_required = 'persons.view_organization'
    model = Organization
    fields = [  'name',
                'short_name',
                'classification', 
    ]
    success_url = reverse_lazy("person:org-index" )
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CreateOrgView, self).form_valid(form)

class CreateRoleView(PermissionRequiredMixin, CreateView):
    permission_required = 'persons.view_role'
    model = Role
    fields = ['name',]
    success_url = reverse_lazy("person:role-index" )
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CreateRoleView, self).form_valid(form)

# view existing entries for person, department and organization:
class DetailPersonView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persons.view_person'
    model = Person
    template_name = 'persons/detail_person.html'

class DetailDeptView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persons.view_department'
    model = Department
    template_name = 'persons/detail_dept.html'

class DetailOrgView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persons.view_organization'
    model = Organization
    template_name = 'persons/detail_org.html'

class DetailRoleView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persons.view_role'
    model = Role
    template_name = 'persons/detail_role.html'

# edit existing entries for person, department and organization:
class EditPersonView(PermissionRequiredMixin, UpdateView):
    permission_required = 'persons.view_person'
    model = Person
    form_class = PersonForm
    fields = [  'preferred_name',
                'title',
                'first_name', 
                'last_name', 
                'pronoun',
                'cwid', 
                'department',
                'organization', 
                'role', 
                'email_primary',
                'email_secondary',
                'phone',
                'comments',
    ]

class EditDeptView(PermissionRequiredMixin, UpdateView):
    permission_required = 'persons.view_department'
    model = Department
    fields = [  'name',
                'classification', 
    ]

class EditOrgView(PermissionRequiredMixin, UpdateView):
    permission_required = 'persons.view_organization'
    model = Organization
    fields = [  'name',
                'short_name',
                'classification', 
    ]

class EditRoleView(PermissionRequiredMixin, UpdateView):
    permission_required = 'persons.view_role'
    model = Role
    fields = ['name',]

##############################
######  SEARCH  VIEWS   ######
##############################

class FullSearch(PermissionRequiredMixin, generic.TemplateView):
    permission_required = 'persons.view_role'
    template_name = 'persons/search_results.html'
    
    def post(self, request, *args, **kwargs):
        st = request.POST['srch_term']
        qs_p = Person.objects.all()
        qs_p =  qs_p.filter(Q(cwid__icontains=st) | 
                                Q(preferred_name__icontains=st) | 
                                Q(first_name__icontains=st) |
                                Q(last_name__icontains=st)
                     ).filter(published=True
        )
        qs_d = Department.objects.all()
        qs_d = qs_d.filter(name__icontains=st) 
                                
        qs_o = Organization.objects.all()
        qs_o = qs_o.filter( Q(name__icontains=st) |
                            Q(short_name__icontains=st)  
        )
        context = { "search_str" : st,
                    "qs_p": qs_p,
                    "qs_d": qs_d,
                    "qs_o": qs_o,
        }
        return render(request, self.template_name, context)