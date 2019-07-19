from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name = 'dc_management'
urlpatterns = [
    # index showing dashboard of high priority items:
    path('', views.IndexView.as_view(), name='index'),

    # autocomplete functions:
    path('autocomplete-person', 
        views.PersonAutocomplete.as_view(), 
        name='autocomplete-person',
        ),
    path('autocomplete-dept', 
        views.DeptAutocomplete.as_view(), 
        name='autocomplete-user',
        ),
    path('autocomplete-org', 
        views.OrgAutocomplete.as_view(),
        name='autocomplete-project',
        ),
    path('autocomplete-role', 
        views.RoleAutocomplete.as_view(),
        name='autocomplete-node',
        ),

    # index views of person, department and organization:
    path('person', views.IndexPersonView.as_view(), name='person-index'),
    path('department', views.IndexDeptView.as_view(), name='dept-index'),
    path('organization', views.IndexOrgView.as_view(), name='org-index'),
    path('role', views.IndexRoleView.as_view(), name='role-index'),
    
    # create new entries for person, department and organization:
    path('person/create', views.CreatePersonView.as_view(), name='person-create'),
    path('department/create', views.CreateDeptView.as_view(), name='dept-create'),
    path('organization/create', views.CreateOrgView.as_view(), name='org-create'),
    path('role/create', views.CreateRoleView.as_view(), name='role-create'),

    # view existing entries for person, department and organization:
    path('person/<int:pk>', views.DetailPersonView.as_view(), name='person-view'),
    path('department/<int:pk>', views.DetailDeptView.as_view(), name='dept-view'),
    path('organization/<int:pk>', views.DetailOrgView.as_view(), name='org-view'),
    path('role/<int:pk>', views.DetailRoleView.as_view(), name='role-view'),

    # edit existing entries for person, department and organization:
    path('person/<int:pk>/edit', views.EditPersonView.as_view(), name='person-edit'),
    path('department/<int:pk>/edit', views.EditDeptView.as_view(), name='dept-edit'),
    path('organization/<int:pk>/edit', views.EditOrgView.as_view(), name='org-edit'),
    path('role/<int:pk>/edit', views.EditRoleView.as_view(), name='role-edit'),
    
    # search view:
    path('search/all', views.FullSearch.as_view(), name="full-search"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)