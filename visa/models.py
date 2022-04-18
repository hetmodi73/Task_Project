from django.db import models
from django.urls import reverse
# Create your models here.

class canada(models.Model):
    choice1=(
        ('17 or less', '17 or less'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47 or older', '47 or older')
    )
    root_age=models.IntegerField(choices=choice1)
    choice2=(
        ('less than secondary','less than secondary'),
        ('secondary school credential', 'secondary school credential'),
        ('one-year post-secondary credential', 'one-year post-secondary credential'),
        ('two-year post-secondary credential', 'two-year post-secondary credential'),
        ('three-year or more post-secondary credential', 'three-year or more post-secondary credential'),
        ('two or more post-secondary credentials with at least one being 3+ years', 'two or more post-secondary credentials with at least one being 3+ years'),
        ('masters or entry-to-practice professional degree', 'masters or entry-to-practice professional degree'),
        ('PHD/doctoral certificate', 'PHD/doctoral certificate'),
    )
    root_education_level=models.CharField(max_length=100, choices=choice2)
    choice3=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_studied_in_canada=models.CharField(max_length=100, choices=choice3)
    choice4=(
        ('Less than high basic (CLB3-, IELTS 2.5-3)', 'Less than high basic (CLB3-, IELTS 2.5-3)'),
        ('High basic (CLB4, IELTS 3.5)', 'High basic (CLB4, IELTS 3.5)'),
        ('Initial intermediate (CLB5, IELTS 4-4.5)', 'Initial intermediate (CLB5, IELTS 4-4.5)'),
        ('Developing intermediate (CLB6, IELTS 5-5.5)', 'Developing intermediate (CLB6, IELTS 5-5.5)'),
        ('Adequate intermediate (CLB7, IELTS 6)', 'Adequate intermediate (CLB7, IELTS 6)'),
        ('High intermediate (CLB8, IELTS 6.5)', 'High intermediate (CLB8, IELTS 6.5)'),
        ('Initial advanced (CLB9, IELTS 7)', 'Initial advanced (CLB9, IELTS 7)'),
        ('Advanced (CLB10+, IELTS 8+)', 'Advanced (CLB10+, IELTS 8+)')
    )
    root_english_reading=models.CharField(max_length=100, choices=choice4)
    choice5=(
        ('Less than high basic (CLB3-, IELTS 3-3.5)', 'Less than high basic (CLB3-, IELTS 3-3.5)'),
        ('High basic (CLB4, IELTS 4-4.5)', 'High basic (CLB4, IELTS 4-4.5)'),
        ('Initial intermediate (CLB5, IELTS 5)', 'Initial intermediate (CLB5, IELTS 5)'),
        ('Developing intermediate (CLB6, IELTS 5.5)', 'Developing intermediate (CLB6, IELTS 5.5)'),
        ('Adequate intermediate (CLB7, IELTS 6)', 'Adequate intermediate (CLB7, IELTS 6)'),
        ('High intermediate (CLB8, IELTS 6.5)', 'High intermediate (CLB8, IELTS 6.5)'),
        ('Initial advanced (CLB9, IELTS 7)', 'Initial advanced (CLB9, IELTS 7)'),
        ('Advanced (CLB10+, IELTS 7.5+)', 'Advanced (CLB10+, IELTS 7.5+)')
    )
    root_english_speaking=models.CharField(max_length=100, choices=choice5)
    choice6=(
        ('Less than high basic (CLB3-, IELTS 3.5-4)', 'Less than high basic (CLB3-, IELTS 3.5-4)'),
        ('High basic (CLB4, IELTS 4.5)', 'High basic (CLB4, IELTS 4.5)'),
        ('Initial intermediate (CLB5, IELTS 5)', 'Initial intermediate (CLB5, IELTS 5)'),
        ('Developing intermediate (CLB6, IELTS 5.5)', 'Developing intermediate (CLB6, IELTS 5.5)'),
        ('Adequate intermediate (CLB7, IELTS 6-7)', 'Adequate intermediate (CLB7, IELTS 6-7)'),
        ('High intermediate (CLB8, IELTS 7.5)', 'High intermediate (CLB8, IELTS 7.5)'),
        ('Initial advanced (CLB9, IELTS 8)', 'Initial advanced (CLB9, IELTS 8)'),
        ('Advanced (CLB10+, IELTS 8.5+)', 'Advanced (CLB10+, IELTS 8.5+)')
    )
    root_english_listening=models.CharField(max_length=100, choices=choice6)
    choice7=(
        ('Less than high basic (CLB3-, IELTS 3-3.5)', 'Less than high basic (CLB3-, IELTS 3-3.5)'),
        ('High basic (CLB4, IELTS 4-4.5)', 'High basic (CLB4, IELTS 4-4.5)'),
        ('Initial intermediate (CLB5, IELTS 5)', 'Initial intermediate (CLB5, IELTS 5)'),
        ('Developing intermediate (CLB6, IELTS 5.5)', 'Developing intermediate (CLB6, IELTS 5.5)'),
        ('Adequate intermediate (CLB7, IELTS 6)', 'Adequate intermediate (CLB7, IELTS 6)'),
        ('High intermediate (CLB8, IELTS 6.5)', 'High intermediate (CLB8, IELTS 6.5)'),
        ('Initial advanced (CLB9, IELTS 7)', 'Initial advanced (CLB9, IELTS 7)'),
        ('Advanced (CLB10+, IELTS 7.5+)', 'Advanced (CLB10+, IELTS 7.5+)')
    )
    root_english_writing=models.CharField(max_length=100, choices=choice7)
    choice8=(
        ('Less than high basic (CLB3-, TEF N/A)', 'Less than high basic (CLB3-, TEF N/A)'),
        ('High basic (CLB4, TEF 121-150)', 'High basic (CLB4, TEF 121-150)'),
        ('Initial intermediate (CLB5, TEF 151-180)', 'Initial intermediate (CLB5, TEF 151-180)'),
        ('Developing intermediate (CLB6, TEF 181-206)', 'Developing intermediate (CLB6, TEF 181-206)'),
        ('Adequate intermediate  (CLB7, TEF 207-232)', 'Adequate intermediate  (CLB7, TEF 207-232)'),
        ('High intermediate (CLB8, TEF 233-247)', 'High intermediate (CLB8, TEF 233-247)'),
        ('Initial advanced (CLB9, TEF 248-262)', 'Initial advanced (CLB9, TEF 248-262)'),
        ('Advanced (CLB10+, TEF 263-277+)', 'Advanced (CLB10+, TEF 263-277+)')
    )
    root_french_reading=models.CharField(max_length=100, choices=choice8, blank=True,null=True)
    choice9=(
        ('Less than high basic (CLB3-, TEF N/A)', 'Less than high basic (CLB3-, TEF N/A)'),
        ('High basic (CLB4, TEF 181-225)', 'High basic (CLB4, TEF 181-225)'),
        ('Initial intermediate (CLB5, TEF 226-270)', 'Initial intermediate (CLB5, TEF 226-270)'),
        ('Developing intermediate (CLB6, TEF 271-309)', 'Developing intermediate (CLB6, TEF 271-309)'),
        ('Adequate intermediate (CLB7, TEF 310-348)', 'Adequate intermediate (CLB7, TEF 310-348)'),
        ('High intermediate (CLB8, TEF 349-370)', 'High intermediate (CLB8, TEF 349-370)'),
        ('Initial advanced (CLB9, TEF 371-392)', 'Initial advanced (CLB9, TEF 371-392)'),
        ('Advanced (CLB10+, TEF 393-415+)', 'Advanced (CLB10+, TEF 393-415+)')
    )
    root_french_speaking=models.CharField(max_length=100, choices=choice9, blank=True,null=True)
    choice10=(
        ('Less than high basic (CLB3-, TEF N/A)', 'Less than high basic (CLB3-, TEF N/A)'),
        ('High basic (CLB4, TEF 145-180)', 'High basic (CLB4, TEF 145-180)'),
        ('Initial intermediate (CLB5, TEF 181-216)', 'Initial intermediate (CLB5, TEF 181-216)'),
        ('Developing intermediate (CLB6, TEF 217-248)', 'Developing intermediate (CLB6, TEF 217-248)'),
        ('Adequate intermediate (CLB7, TEF 249-279)', 'Adequate intermediate (CLB7, TEF 249-279)'),
        ('High intermediate (CLB8, TEF 280-297)', 'High intermediate (CLB8, TEF 280-297)'),
        ('Initial advanced (CLB9, TEF 298-315)', 'Initial advanced (CLB9, TEF 298-315)'),
        ('Advanced (CLB10+, TEF 316-333)', 'Advanced (CLB10+, TEF 316-333)')
    )
    root_french_listening=models.CharField(max_length=100, choices=choice10, blank=True,null=True)
    choice11=(
        ('Less than high basic (CLB3-, TEF N/A)', 'Less than high basic (CLB3-, TEF N/A)'),
        ('High basic (CLB4, TEF 181-225)', 'High basic (CLB4, TEF 181-225)'),
        ('Initial intermediate (CLB5, TEF 226-270)', 'Initial intermediate (CLB5, TEF 226-270)'),
        ('Developing intermediate (CLB6, TEF 271-309)', 'Developing intermediate (CLB6, TEF 271-309)'),
        ('Adequate intermediate (CLB7, TEF 310-348)', 'Adequate intermediate (CLB7, TEF 310-348)'),
        ('High intermediate (CLB8, TEF 349-370)', 'High intermediate (CLB8, TEF 349-370)'),
        ('Initial advanced (CLB9, TEF 371-392)', 'Initial advanced (CLB9, TEF 371-392)'),
        ('Advanced (CLB10+, TEF 393-415+)', 'Advanced (CLB10+, TEF 393-415+)')
    )
    root_french_writing=models.CharField(max_length=100, choices=choice11, blank=True,null=True)
    choice12=(
        ('None', 'None'),
        ('less than one year', 'less than one year'),
        ('one year', 'one year'),
        ('two years', 'two years'),
        ('three years', 'three years'),
        ('four years', 'four years'),
        ('five years', 'five years'),
        ('six years or more', 'six years or more')
    )
    root_work_foreign_skilled_work_years=models.CharField(max_length=100, choices=choice12)
    choice13=(
        ('None', 'None'),
        ('less than one year', 'less than one year'),
        ('one year', 'one year'),
        ('two years', 'two years'),
        ('three years', 'three years'),
        ('four years', 'four years'),
        ('five years', 'five years'),
        ('six years or more', 'six years or more')
    )
    root_work_canadian_skilled_work_years=models.CharField(max_length=100, choices=choice13)
    choice14=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_maratial_status=models.CharField(max_length=100, choices=choice14)
    choice15=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_spouse_siblings=models.CharField(max_length=100, choices=choice15)
    choice16=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_trades_certificate=models.CharField(max_length=100, choices=choice16)
    choice17=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_nomination_certificate=models.CharField(max_length=100, choices=choice17)
    choice18=(
        ('YES','YES'),
        ('NO', 'NO')
    )
    root_skilled_job_offer=models.CharField(max_length=100, choices=choice18)
    root_contact_details_residence_country=models.CharField(max_length=100, blank=True,null=True)
    root_contact_details_name=models.CharField(max_length=100, blank=True,null=True)
    root_contact_details_email=models.EmailField(max_length=100, blank=True,null=True)
    root_contact_details_telephone=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.root_age}"

    def get_absolute_url(self):
        return reverse('canada-view')
