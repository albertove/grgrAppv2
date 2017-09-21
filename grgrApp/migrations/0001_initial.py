# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prname', models.CharField(max_length=200, verbose_name='Project name')),
                ('pradress', models.CharField(blank=True, max_length=200, verbose_name='Project adress')),
                ('prdesigner', models.CharField(blank=True, max_length=200, verbose_name='Project designer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.IntegerField()),
                ('type_of_paving', models.IntegerField(verbose_name='Type of paving block')),
                ('conc_paving_joint', models.IntegerField(verbose_name='Concrete paving blocks with openings/with widened joint')),
                ('riven_paving', models.IntegerField(verbose_name='Riven paving set')),
                ('conv_paving', models.IntegerField(verbose_name='Conventional paving')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grgrApp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStormwater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavement_area', models.IntegerField(verbose_name='Pavement area')),
                ('num_draining_pipes', models.IntegerField(verbose_name='Number of draining pipes under permeable surface')),
                ('depth_draining_pipe', models.IntegerField(help_text='Please write a value and then clic in Update value', verbose_name='Depth draining pipe')),
                ('ground_water_level', models.IntegerField(help_text='Please write a value and then clic in Update value', verbose_name='Ground water level')),
                ('construction_type', models.IntegerField(verbose_name='Construction type')),
                ('height_open_volume', models.IntegerField(verbose_name='Height open volume')),
                ('distance_overflow', models.IntegerField(verbose_name='Distance to overflow gully')),
                ('thickness_vegetation_layer', models.IntegerField(verbose_name='Thickness vegetation layer')),
                ('thickness_coarse_sand', models.IntegerField(verbose_name='Thickness coarse sand')),
                ('thickness_coarse_aggregate_26', models.IntegerField(verbose_name='Thickness coarse aggregate')),
                ('thickness_coarse_aggregate_416', models.IntegerField(verbose_name='Thickness coarse aggregate')),
                ('depth_draining_pipe_bio', models.IntegerField(verbose_name='Depth draining pipe')),
                ('area_stormwater_cons', models.IntegerField(verbose_name='Area storm water construction in relation to permeable surface')),
                ('num_draining_pipes_stormwater', models.IntegerField(verbose_name='Number of draining pipes in storm water construction')),
                ('is_ground_contaminated', models.IntegerField(verbose_name='Is ground contaminated?')),
                ('is_bottom_impermeable', models.IntegerField(verbose_name='Is the bottom of the storm water construction impermeable?')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grgrApp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_type_paving', models.CharField(max_length=32, verbose_name='Surface course')),
                ('sum_bedding_layer', models.CharField(default='2/4', max_length=32, verbose_name='Bedding layer')),
                ('sum_unbound_base_layer', models.CharField(default='0/32', max_length=32, verbose_name='Unbound base layer')),
                ('sum_sub_base_layer', models.CharField(max_length=32, verbose_name='Sub base layer')),
                ('sum_thickness_subbase_layer', models.CharField(max_length=32, verbose_name='Thickness in sub base layer available for storm water detention')),
                ('sum_position_draining_pipe', models.CharField(max_length=32, verbose_name='Position draining pipe')),
                ('sum_ground_water_level', models.CharField(max_length=32, verbose_name='Distance to ground water level')),
                ('sum_traffic_class', models.CharField(max_length=32, verbose_name='Traffic class')),
                ('sum_prepared_subgrade_material', models.CharField(max_length=32, verbose_name='Prepared subgrade material')),
                ('sum_climatic_zone', models.CharField(max_length=32, verbose_name='Climatic zone')),
                ('sum_frost_suceptibility_class', models.CharField(max_length=32, verbose_name='Frost suceptibility class')),
                ('sum_design_duration_rain', models.CharField(max_length=32, verbose_name='Design duration rain fall')),
                ('sum_design_intensity_rain', models.CharField(max_length=32, verbose_name='Design intensity rain fall')),
                ('sum_available_volume', models.CharField(max_length=32, verbose_name='Available volume for storm water retention')),
                ('sum_required_volume', models.CharField(max_length=32, verbose_name='Required volume for storm water retention')),
                ('sum_veredict', models.TextField(verbose_name='Veredict 1')),
                ('sum_construction_type', models.CharField(max_length=120, verbose_name='Construction type')),
                ('sum_height_open_volume', models.CharField(max_length=32, verbose_name='Height open volume')),
                ('sum_distance_overflow', models.CharField(max_length=32, verbose_name='Distance to overflow gully')),
                ('sum_thickness_vegetation_layer', models.CharField(max_length=32, verbose_name='Thickness vegetation layer')),
                ('sum_thickness_coarse_sand', models.CharField(max_length=32, verbose_name='Thickness coarse sand')),
                ('sum_thickness_coarse_aggregate_26', models.CharField(max_length=32, verbose_name='Thickness coarse aggregate 2/6')),
                ('sum_thickness_coarse_aggregate_416', models.CharField(max_length=32, verbose_name='Thickness coarse aggregate 4/16')),
                ('sum_thickness_skeletal_soil', models.CharField(max_length=32, verbose_name='Thickness skeletal soil')),
                ('sum_position_draining_pipe_ditch', models.CharField(max_length=32, verbose_name='Position draining pipe (ditch)')),
                ('sum_ground_water_level_ditch', models.CharField(max_length=32, verbose_name='Distance to ground water level (ditch)')),
                ('sum_design_duration_rain_ditch', models.CharField(max_length=32, verbose_name='Design duration rain fall (ditch)')),
                ('sum_design_intensity_rain_ditch', models.CharField(max_length=32, verbose_name='Design intensity rain fall (ditch)')),
                ('sum_available_volume_ditch', models.CharField(max_length=32, verbose_name='Available volume for storm water retention (ditch)')),
                ('sum_required_volume_ditch', models.CharField(max_length=32, verbose_name='Required volume for storm water retention (ditch)')),
                ('sum_veredict_ditch', models.TextField(verbose_name='Veredict 2')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grgrApp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTraffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traffic_category', models.IntegerField(verbose_name='Choose traffic category')),
                ('thickness_base_layer', models.IntegerField(verbose_name='Thickness base layer')),
                ('fraction_base_layer', models.CharField(default='0/32', max_length=4, verbose_name='Fraction base layer')),
                ('thickness_surface_course', models.IntegerField(verbose_name='Thickness surface course')),
                ('thickness_bedding_layer', models.IntegerField(verbose_name='Thickness bedding layer')),
                ('fraction_bedding_layer', models.CharField(default='2/4', max_length=4, verbose_name='Fraction bedding layer')),
                ('subgrade_material', models.IntegerField(verbose_name='Choose perpared sub-grade material')),
                ('climatic_zone', models.IntegerField(verbose_name='Climatic zone')),
                ('frost_suceptibility_class', models.IntegerField(verbose_name='Frost suceptibility class')),
                ('subbase_material', models.IntegerField(verbose_name='Sub-base material')),
                ('thickness_subbase_layer', models.IntegerField(verbose_name='Thickness subbase layer')),
                ('fraction_subbase_layer', models.CharField(blank=True, default='', max_length=4, verbose_name='Fraction subbase layer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grgrApp.Project')),
            ],
        ),
    ]