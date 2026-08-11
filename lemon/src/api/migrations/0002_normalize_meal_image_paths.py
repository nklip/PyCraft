from django.db import migrations


def normalize_meal_image_paths(apps, schema_editor):
    meal_model = apps.get_model('api', 'Meal')

    for meal in meal_model.objects.filter(image__startswith='/'):
        meal.image = meal.image.lstrip('/')
        meal.save(update_fields=['image'])


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            normalize_meal_image_paths,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
