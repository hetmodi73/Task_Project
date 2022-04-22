from django.contrib import admin
from .models import canada_pr

# Register your models here.

class showcanada_pr(admin.ModelAdmin):
    list_display = ['SKILLED_EMPLOYMENT',
                    'WORK_EXPERIENCE',
                    'QUALIFICATIONS',
                    'AGE_20TO55_YEARS',
                    'Skilled_employment_2',
                    'Work_experience_2',
                    'Additional_Bonus_Points',
                    'Qualifications',
                    'Partner_Qualifications',
                    'client',
                    'text',
                    'city',
                    'resume'
                    ]

admin.site.register(canada_pr,showcanada_pr)
