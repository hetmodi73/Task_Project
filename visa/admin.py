from django.contrib import admin
from .models import canada
# Register your models here.

class showcanada(admin.ModelAdmin):
    list_display = ['root_age',
                    'root_education_level',
                    'root_studied_in_canada',
                    'root_english_reading',
                    'root_english_speaking',
                    'root_english_listening',
                    'root_english_writing',
                    'root_french_reading',
                    'root_french_speaking',
                    'root_french_listening',
                    'root_french_writing',
                    'root_work_foreign_skilled_work_years',
                    'root_work_canadian_skilled_work_years',
                    'root_maratial_status',
                    'root_spouse_siblings',
                    'root_trades_certificate',
                    'root_nomination_certificate',
                    'root_skilled_job_offer',
                    # 'root_contact_details_residence_country',
                    'client',
                    'root_contact_details_email',
                    'root_contact_details_telephone']

admin.site.register(canada,showcanada)
