from django.contrib import admin

# customize the individual model views:
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('preferred_name',
                    'first_name', 
                    'last_name',
                    'cwid', 
                    'email_primary',
                    )
    search_fields = ('preferred_name',
                    'first_name', 
                    'last_name',
                    'cwid',
                    )

@admin.register(Department)
class DeptAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )
    search_fields = ('name',
                    )   
                    
@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('short_name',
                    'name'
                    )
    search_fields = ('name',
                    )   
                    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )
    search_fields = ('name',
                    )   