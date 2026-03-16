from django.contrib import admin
from home.models import (
    Contact,
    HeroSection,
    AboutSection,
    SkillsSection,
    Skill,
    ResumeSummary,
    Education,
    Experience,
    ProjectsSection,
    Project,
    ProjectImage,
    ContactSection,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillsSection)
class SkillsSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_editable = ('category', 'order')


@admin.register(ResumeSummary)
class ResumeSummaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'order')
    list_editable = ('order',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)


@admin.register(ProjectsSection)
class ProjectsSectionAdmin(admin.ModelAdmin):
    pass


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_editable = ('category', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'category', 'image_path', 'order')}),
        ('Detail Page Content', {'fields': ('short_description', 'full_description')}),
        ('Sidebar Info', {'fields': ('info_category', 'info_client', 'info_date', 'info_technologies', 'info_role')}),
    )


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    pass
