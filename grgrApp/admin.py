from django.contrib import admin
from .models import Project,ProjectParameter,ProjectTraffic,ProjectStormwater,ProjectSummary

admin.site.register(Project)
admin.site.register(ProjectParameter)
admin.site.register(ProjectTraffic)
admin.site.register(ProjectStormwater)
admin.site.register(ProjectSummary)
