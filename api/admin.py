from django.contrib import admin

# Register your models here.
from .models import User, Project, ProjectMember, Task, Comment

admin.site.register(User,)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Comment)
