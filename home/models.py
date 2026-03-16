from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)

    def __str__(self):
        return self.name


# ── Singleton-style sections (only one row used) ──────────────────────────────

class HeroSection(models.Model):
    name = models.CharField(max_length=100, default='Gerardo Wibmer')
    typed_items = models.CharField(
        max_length=500,
        default='Full-Stack Developer, AI/ML Engineer, Software Engineer, Freelancer',
        help_text='Comma-separated list of items for the typing animation',
    )

    class Meta:
        verbose_name = 'Hero Section'

    def __str__(self):
        return 'Hero Section'


class AboutSection(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=300, help_text='Role headline shown under the photo')
    linkedin_url = models.URLField(blank=True)
    linkedin_label = models.CharField(max_length=100, blank=True, default='linkedin.com/in/gwibmer')
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    degree = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'About Section'

    def __str__(self):
        return 'About Section'


class SkillsSection(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = 'Skills Section'

    def __str__(self):
        return 'Skills Section'


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Languages', 'Languages'),
        ('Frameworks & Libraries', 'Frameworks & Libraries'),
        ('Tools & Platforms', 'Tools & Platforms'),
        ('AI / ML', 'AI / ML'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Languages')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f'{self.name} ({self.category})'


class ResumeSummary(models.Model):
    section_description = models.TextField(
        blank=True,
        help_text='Intro paragraph shown at the top of the Resume section'
    )
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, help_text='e.g. AI & Full-Stack Engineer · Tampa, FL')
    summary_text = models.TextField(help_text='Bio paragraph shown below the header')
    location = models.CharField(max_length=200, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Resume Summary'

    def __str__(self):
        return 'Resume Summary'


class Education(models.Model):
    degree = models.CharField(max_length=300)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    institution = models.CharField(max_length=200)
    details = models.CharField(max_length=100, blank=True, help_text='e.g. GPA 3.83')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.degree


class Experience(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    responsibilities = models.TextField(help_text='One bullet point per line')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} at {self.company}'

    def get_responsibilities(self):
        return [r.strip() for r in self.responsibilities.splitlines() if r.strip()]


class ProjectsSection(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = 'Projects Section'

    def __str__(self):
        return 'Projects Section'


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('filter-django', 'Django'),
        ('filter-ml', 'Machine Learning'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='', help_text='URL identifier, e.g. sal-sentiment-analysis')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image_path = models.CharField(
        max_length=300,
        help_text='Static file path, e.g. img/portfolio/preview/SAL_1_preview.png',
    )
    order = models.IntegerField(default=0)

    # Detail page content
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True, help_text='HTML content for the detail body')

    # Sidebar info
    info_category = models.CharField(max_length=200, blank=True)
    info_client = models.CharField(max_length=200, blank=True)
    info_date = models.CharField(max_length=50, blank=True)
    info_technologies = models.CharField(max_length=300, blank=True)
    info_role = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/projects/{self.slug}/'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image_path = models.CharField(max_length=300, help_text='Static file path, e.g. img/portfolio/slider/SAL_1_slider.png')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.project.title} — image {self.order}'


class ContactSection(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    linkedin_url = models.URLField(blank=True)
    linkedin_label = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Contact Section'

    def __str__(self):
        return 'Contact Section'
