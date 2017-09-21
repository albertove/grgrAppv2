from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
#from django.utils.safestring import mark_safe

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Choose a username',max_length=10,min_length=5,error_messages={'required':'Please enter a username'})
    name = forms.CharField(label='Your first name',max_length=20,error_messages={'required':'Please enter your first name'})
    lastname = forms.CharField(label='Your last name',max_length=20,error_messages={'required':'Please enter your last name'})

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=10,min_length=5,error_messages={'required': 'Please enter a valid username'})
    name = forms.CharField(label='First name',max_length=20,error_messages={'required': 'Please enter your first name'})

class Project(models.Model):
    user = models.ForeignKey(User)
    prname = models.CharField("Project name",max_length=200)
    pradress = models.CharField("Project adress",max_length=200,blank=True)
    prdesigner = models.CharField("Project designer",max_length=200,blank=True)
    #contrib_catchment = models.BooleanField("Contributing catchment")
    #dist_bott_water = models.FloatField("Distance the bottom of the structure and the groundwater table (m)")

    def __unicode__(self):
        return self.prname

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        #self.fields['dist_bott_water'].widget.attrs.update({'class' : 'inputshort'})
        #self.fields['dist_bott_water'] = forms.FloatField(label="Distance the bottom of the structure and the groundwater table (m)",min_value=0)
        #self.fields['slope_perbeable_block'].widget.attrs.update({'class' : 'inputshort'})
        #self.fields['contrib_catchment'].widget.attrs.update({'class' : 'choose'})
        #self.fields['prname'].required = True

class ProjectParameter(models.Model):

    project = models.ForeignKey(Project)
    application = models.IntegerField()
    type_of_paving = models.IntegerField("Type of paving block")
    conc_paving_joint = models.IntegerField("Concrete paving blocks with openings/with widened joint")
    riven_paving = models.IntegerField("Riven paving set")
    conv_paving = models.IntegerField("Conventional paving")

class ParameterForm(forms.ModelForm):
    #application = forms.ChoiceField(choices=APPLICATION,widget=forms.RadioSelect)
    #type_of_paving = forms.ChoiceField(choices=TYPE_PAVING,widget=forms.RadioSelect)

    class Meta:
        model = ProjectParameter
        exclude = ['project']

    def __init__(self,*args,**kwargs):
        APPLICATION = (
                (1,'Square'),
                (2,'Zone 30 km/h'),
                (3,'Parking'),
        )
        TYPE_PAVING = (
        (1,'Asphalt or concrete paving blocks'),
        (2,'Permeable concrete paving blocks'),
        (3,'Riven paving'),
        )
        super(ParameterForm,self).__init__(*args,**kwargs)
        self.fields['application'] = forms.ChoiceField(choices=APPLICATION,widget=forms.RadioSelect)
        self.fields['application'].widget.attrs.update({'class':'radio'})
        self.fields['type_of_paving'] = forms.ChoiceField(label="Type of paving", choices=TYPE_PAVING,widget=forms.RadioSelect)
        self.fields['type_of_paving'].widget.attrs.update({'class':'radio'})
        self.fields['conv_paving'] = forms.DecimalField(label="Conventional paving",initial=2.5,min_value=0,max_value=5,required=False)
        self.fields['conv_paving'].widget.attrs.update({'class':'labelshort'})
        self.fields['conc_paving_joint'] = forms.FloatField(label="Concrete paving blocks with openings/with widened joint",initial=20,min_value=20,max_value=30,required=False)
        self.fields['conc_paving_joint'].widget.attrs.update({'class':'labelshort'})
        self.fields['riven_paving'] = forms.FloatField(label="Riven paving set",initial=15,min_value=15,max_value=20,required=False)
        self.fields['riven_paving'].widget.attrs.update({'class':'labelshort'})


class ProjectTraffic(models.Model):
    project = models.ForeignKey(Project)
    traffic_category = models.IntegerField("Choose traffic category")
    thickness_base_layer = models.IntegerField("Thickness base layer")
    fraction_base_layer = models.CharField("Fraction base layer",max_length=4,default="0/32")
    thickness_surface_course = models.IntegerField("Thickness surface course")
    thickness_bedding_layer = models.IntegerField("Thickness bedding layer")
    fraction_bedding_layer = models.CharField("Fraction bedding layer",max_length=4,default="2/4")
    subgrade_material = models.IntegerField("Choose perpared sub-grade material")
    climatic_zone = models.IntegerField("Climatic zone")
    frost_suceptibility_class = models.IntegerField("Frost suceptibility class")
    subbase_material = models.IntegerField("Sub-base material")
    thickness_subbase_layer = models.IntegerField("Thickness subbase layer")
    fraction_subbase_layer = models.CharField("Fraction subbase layer",max_length=4,default="",blank=True)

class TrafficForm(forms.ModelForm):

    #traffic_type = forms.ChoiceField(choices=TRAFFIC,widget=forms.RadioSelect)
    #base_material = forms.ChoiceField(choices=BASE_MAT,widget=forms.RadioSelect)
    #tickn_concrete = forms.ChoiceField(choices=TICK_CONCRETE, widget=forms.RadioSelect)
    class Meta:
        model = ProjectTraffic
        exclude = ['project']
    def __init__(self,*args,**kwargs):
        TRAFFIC = (
            ('','----------'),
            (1,'G/C'),
            (2,'0 Sub-grade material 1'),
            (3,'0 Sub-grade material 2-5'),
            (4,'1'),
            (5,'2'),
        )
        GRAD_MATERIAL = (
            ('','----------'),
            (1,'Material 1'),
            (2,'Material 2'),
            (3,'Material 3'),
            (4,'Material 4'),
            (5,'Material 5'),
        )
        CLIMATIC_ZONE = (
            ('','----------'),
            (1,'Zone 1'),
            (2,'Zone 2'),
            (3,'Zone 3'),
            (4,'Zone 4'),
            (5,'Zone 5'),
        )
        FROST_CLASS = (
            ('','----------'),
            (1,'3'),
            (2,'4'),
        )
        BASE_MATERIAL = (
            ('','---------'),
            (1,'Crushed rock'),
            (2,'Other than crushed rock'),
        )

        super(TrafficForm,self).__init__(*args,**kwargs)
        self.fields['traffic_category'] = forms.ChoiceField(label="Choose traffic category",choices=TRAFFIC)
        self.fields['thickness_base_layer'] = forms.FloatField("Thickness base layer")
        self.fields['thickness_base_layer'].widget.attrs.update({'class':'labelshort'})
        self.fields['fraction_base_layer'].widget.attrs.update({'class':'disabled'})
        self.fields['thickness_surface_course'] = forms.FloatField("Thickness surface course")
        self.fields['thickness_surface_course'].widget.attrs.update({'class':'labelshort'})
        self.fields['thickness_bedding_layer'] = forms.FloatField("Thickness bedding layer")
        self.fields['thickness_bedding_layer'].widget.attrs.update({'class':'labelshort'})
        self.fields['fraction_bedding_layer'].widget.attrs.update({'class':'disabled'})
        self.fields['subgrade_material'] = forms.ChoiceField(label="Choose prepared sub-grade material",choices=GRAD_MATERIAL)
        self.fields['climatic_zone'] = forms.ChoiceField(label="Climatic zone",choices=CLIMATIC_ZONE)
        self.fields['frost_suceptibility_class'] = forms.ChoiceField(label="Frost suceptibility class",choices=FROST_CLASS)
        self.fields['subbase_material'] = forms.ChoiceField(label="Sub-base material",choices=BASE_MATERIAL)
        self.fields['thickness_subbase_layer'] = forms.FloatField("Thickness subbase layer",initial=0.0,required=False)
        self.fields['thickness_subbase_layer'].widget.attrs.update({'class':'labelshort'})
        self.fields['fraction_subbase_layer'] = forms.CharField(label="Fraction subbase layer",max_length=4,required=False)
        self.fields['fraction_subbase_layer'].widget.attrs.update({'class':'disabled'})

    def update_values(self,val1,val2):
        self.fields['thickness_subbase_layer'].widget.attrs.update({'class':'labelshort'})
        self.fields['fraction_subbase_layer'].widget.attrs.update({'class':'labelshort'})

class ProjectStormwater(models.Model):
    project = models.ForeignKey(Project)
    pavement_area = models.IntegerField("Pavement area")
    #permeable_surface = models.IntegerField("Permeable surface")
    num_draining_pipes = models.IntegerField("Number of draining pipes under permeable surface")
    depth_draining_pipe = models.IntegerField("Depth draining pipe",help_text="Please write a value and then clic in Update value")
    ground_water_level = models.IntegerField("Ground water level",help_text="Please write a value and then clic in Update value")
    construction_type = models.IntegerField("Construction type")
    #ditch_type = models.IntegerField("Ditch type")
    #biofilter_type = models.IntegerField("Biofilter type")
    height_open_volume = models.IntegerField("Height open volume")
    distance_overflow = models.IntegerField("Distance to overflow gully")
    thickness_vegetation_layer = models.IntegerField("Thickness vegetation layer")
    thickness_coarse_sand = models.IntegerField("Thickness coarse sand")
    thickness_coarse_aggregate_26 = models.IntegerField("Thickness coarse aggregate")
    thickness_coarse_aggregate_416 = models.IntegerField("Thickness coarse aggregate")
    #thickness_coarse_aggregate_1632 = models.IntegerField("Thickness coarse aggregate")
    #thickness_skeletal_soil = models.IntegerField("Thickness skeletal soil")
    depth_draining_pipe_bio = models.IntegerField("Depth draining pipe")
    # ground_water_level_bio = models.IntegerField("Ground water level")
    area_stormwater_cons = models.IntegerField("Area storm water construction in relation to permeable surface")
    num_draining_pipes_stormwater = models.IntegerField("Number of draining pipes in storm water construction")
    is_ground_contaminated = models.IntegerField("Is ground contaminated?")
    is_bottom_impermeable = models.IntegerField("Is the bottom of the storm water construction impermeable?")

class StormwaterForm(forms.ModelForm):
    class Meta:
        model = ProjectStormwater
        exclude = ['project']
    def __init__(self,*args,**kwargs):
        BIO_TYPE = (
            ('','-------'),
            (1,'with plants'),
            (2,'with trees'),
        )
        CONS_TYPE = (
            ('','-------'),
            (1,'None'),
            (2,'Biofilter with plants'),
            (3,'Biofilter with tree'),
            (4,'Infiltration ditch with macadam'),
            (5,'Open ditch'),
        )
        DITCH_TYPE = (
            (1,"Biofilter"),
            (2,"Infiltration dith with macadam"),
            (3,"Open ditch"),
            (4,"Pavement"),
        )
        YES_NO = (
            ('','---'),
            (1,"Yes"),
            (2,"No"),
        )
        super(StormwaterForm,self).__init__(*args,**kwargs)
        self.fields['pavement_area'] = forms.FloatField(label="Pavement area",initial=0.0,required=False,max_value=10000,error_messages={'invalid':'The value must be less than 10 000.'})
        self.fields['pavement_area'].widget.attrs.update({'class':'disabled','disabled':'True'})
        #self.fields['permeable_surface'] = forms.IntegerField(min_value=0,max_value=10000,initial=0.0)
        #self.fields['permeable_surface'].widget.attrs.update({'class':'disabled','disabled':'True'})
        self.fields['num_draining_pipes'] = forms.IntegerField(label="Number of draining pipes under permeable surface",initial=0,required=False)
        self.fields['num_draining_pipes'].widget.attrs.update({'class':'disabled','disabled':'True'})
        self.fields['depth_draining_pipe'] = forms.FloatField(label="Depth draining pipe",initial=0.0,required=False,help_text="Please write a value and then clic in Update value")
        self.fields['depth_draining_pipe'].widget.attrs.update({'class':'disabled','disabled':'True'})
        self.fields['ground_water_level'] = forms.FloatField(label="Ground water level",initial=0.0,required=False,help_text="Please write a value and then clic in Update value")
        self.fields['ground_water_level'].widget.attrs.update({'class':'disabled','disabled':'True'})

        self.fields['construction_type'] = forms.ChoiceField(label="Construction type",choices=CONS_TYPE)
        #self.fields['ditch_type'] = forms.ChoiceField(label="Ditch type",choices=DITCH_TYPE)
        #self.fields['biofilter_type'] = forms.ChoiceField(label="Biofilter type",choices=BIO_TYPE)
        #self.fields['biofilter_type'].widget.attrs.update({'disabled':'True'})

        self.fields['height_open_volume'] = forms.FloatField(label="Height open volume (h7)",initial=0.0,required=False)
        self.fields['height_open_volume'].widget.attrs.update({'class':'labelshort','disabled':'false'})
        self.fields['distance_overflow'] = forms.FloatField(label="Distance to overflow gully (h7b)",initial=0.0,required=False)
        self.fields['distance_overflow'].widget.attrs.update({'class':'labelshort'})
        self.fields['thickness_vegetation_layer'] = forms.FloatField(label="Thickness vegetation layer (h8)",initial=0.0,required=False)
        self.fields['thickness_vegetation_layer'].widget.attrs.update({'class':'labelshort','disabled':'false'})
        self.fields['thickness_coarse_sand'] = forms.FloatField(label="Thickness coarse sand (h9)",initial=0.0,required=False)
        self.fields['thickness_coarse_sand'].widget.attrs.update({'class':'labelshort','disabled':'false'})
        self.fields['thickness_coarse_aggregate_26'] = forms.FloatField(label="Thickness coarse aggregate 2/6 (h10)",initial=0.0,required=False)
        self.fields['thickness_coarse_aggregate_26'].widget.attrs.update({'class':'labelshort','disabled':'false'})
        self.fields['thickness_coarse_aggregate_416'] = forms.FloatField(label="Thickness coarse aggregate 4/16 (h11)",initial=0.0,required=False)
        self.fields['thickness_coarse_aggregate_416'].widget.attrs.update({'class':'labelshort'})
        # self.fields['thickness_coarse_aggregate_1632'] = forms.FloatField(label="Thickness coarse aggregate 16/32 (h12)",initial=0.0,required=False)
        # self.fields['thickness_coarse_aggregate_1632'].widget.attrs.update({'class':'labelshort'})
        # self.fields['thickness_skeletal_soil'] = forms.FloatField(label="Thickness skeletal soil (h13)",initial=0.0,required=False)
        # self.fields['thickness_skeletal_soil'].widget.attrs.update({'class':'labelshort'})
        self.fields['depth_draining_pipe_bio'] = forms.FloatField(label="Depth draining pipe (h15)",initial=0.0,required=False)
        self.fields['depth_draining_pipe_bio'].widget.attrs.update({'class':'labelshort','disabled':'false'})
        # self.fields['ground_water_level_bio'] = forms.FloatField(label="Ground water level (h14)",initial=0.0,required=False)
        # self.fields['ground_water_level_bio'].widget.attrs.update({'class':'labelshort'})
        self.fields['area_stormwater_cons'] = forms.DecimalField(label="Area storm water construction in relation to permeable surface",initial=2.5,required=False)
        self.fields['area_stormwater_cons'].widget.attrs.update({'class':'labelshort'})
        self.fields['num_draining_pipes_stormwater'] = forms.FloatField(label="Number of draining pipes in storm water construction",initial=0.0,required=False)
        self.fields['num_draining_pipes_stormwater'].widget.attrs.update({'class':'labelshort'})
        self.fields['is_ground_contaminated'] = forms.ChoiceField(label="Is ground contaminated?",choices=YES_NO,required=False)
        self.fields['is_bottom_impermeable'] = forms.ChoiceField(label="Is the bottom of the storm water construction impermeable?",choices=YES_NO,required=False)

class ProjectSummary(models.Model):
    project = models.ForeignKey(Project)
    sum_type_paving = models.CharField("Surface course",max_length=32) #h1
    sum_bedding_layer = models.CharField("Bedding layer",max_length=32,default="2/4") #h2
    sum_unbound_base_layer = models.CharField("Unbound base layer",max_length=32,default="0/32") #h3
    sum_sub_base_layer = models.CharField("Sub base layer",max_length=32) #h4
    sum_thickness_subbase_layer = models.CharField("Thickness in sub base layer available for storm water detention",max_length=32) #h4a
    sum_position_draining_pipe = models.CharField("Position draining pipe",max_length=32) #h4b
    sum_ground_water_level = models.CharField("Distance to ground water level",max_length=32) #h5

    sum_traffic_class = models.CharField("Traffic class",max_length=32)
    sum_prepared_subgrade_material = models.CharField("Prepared subgrade material",max_length=32)
    sum_climatic_zone = models.CharField("Climatic zone",max_length=32)
    sum_frost_suceptibility_class = models.CharField("Frost suceptibility class",max_length=32)
    sum_design_duration_rain = models.CharField("Design duration rain fall",max_length=32)
    sum_design_intensity_rain = models.CharField("Design intensity rain fall",max_length=32)
    sum_available_volume = models.CharField("Available volume for storm water retention",max_length=32)
    sum_required_volume = models.CharField("Required volume for storm water retention",max_length=32)
    sum_veredict = models.TextField("Veredict 1")

    sum_construction_type = models.CharField("Construction type",max_length=120)
    sum_height_open_volume = models.CharField("Height open volume",max_length=32) #h7
    sum_distance_overflow = models.CharField("Distance to overflow gully",max_length=32) #h7b
    sum_thickness_vegetation_layer = models.CharField("Thickness vegetation layer",max_length=32) #h8
    sum_thickness_coarse_sand = models.CharField("Thickness coarse sand",max_length=32) #h9
    sum_thickness_coarse_aggregate_26 = models.CharField("Thickness coarse aggregate 2/6",max_length=32) #h10
    sum_thickness_coarse_aggregate_416 =  models.CharField("Thickness coarse aggregate 4/16",max_length=32) #h11
    #sum_thickness_coarse_aggregate_1632 =  models.IntegerField("Thickness coarse aggregate 16/32 (h12)")
    sum_thickness_skeletal_soil = models.CharField("Thickness skeletal soil",max_length=32) #h13
    sum_position_draining_pipe_ditch = models.CharField("Position draining pipe (ditch)",max_length=32) #h14
    sum_ground_water_level_ditch = models.CharField("Distance to ground water level (ditch)",max_length=32)

    sum_design_duration_rain_ditch = models.CharField("Design duration rain fall (ditch)",max_length=32)
    sum_design_intensity_rain_ditch = models.CharField("Design intensity rain fall (ditch)",max_length=32)
    sum_available_volume_ditch = models.CharField("Available volume for storm water retention (ditch)",max_length=32)
    sum_required_volume_ditch = models.CharField("Required volume for storm water retention (ditch)",max_length=32)
    sum_veredict_ditch = models.TextField("Veredict 2")

class SummaryForm(forms.ModelForm):
    class Meta:
        model = ProjectSummary
        exclude = ['project']

    def __init__(self,*args,**kwargs):
        super(SummaryForm,self).__init__(*args,**kwargs)
        #self.fields['sum_type_paving'] = forms.CharField(label="Surface course",max_length=32,required=False)
        self.fields['sum_type_paving'].widget.attrs.update({'class':'summary_surface'})
        self.fields['sum_bedding_layer'].widget.attrs.update({'class':'summary'})
        self.fields['sum_unbound_base_layer'].widget.attrs.update({'class':'summary'})
        self.fields['sum_type_paving'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_sub_base_layer'] = forms.CharField(label="Sub base layer (h4)",required=False)
        self.fields['sum_sub_base_layer'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_subbase_layer'] = forms.FloatField(label="Thickness in sub base layer available for storm water detention (h4a)",required=False)
        self.fields['sum_thickness_subbase_layer'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_position_draining_pipe'] = forms.FloatField(label="Position draining pipe (h4b)",required=False)
        self.fields['sum_position_draining_pipe'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_ground_water_level'] = forms.FloatField(label="Distance to ground water level (h5)",required=False)
        self.fields['sum_ground_water_level'].widget.attrs.update({'class':'summary'})

        self.fields['sum_traffic_class'].widget.attrs.update({'class':'summary'})
        self.fields['sum_prepared_subgrade_material'].widget.attrs.update({'class':'summary'})
        self.fields['sum_climatic_zone'].widget.attrs.update({'class':'summary'})
        self.fields['sum_frost_suceptibility_class'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_design_duration_rain'] = forms.FloatField(label="Design duration rain fall",required=False)
        self.fields['sum_design_duration_rain'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_design_intensity_rain'] = forms.FloatField(label="Design intensity rain fall",required=False)
        self.fields['sum_design_intensity_rain'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_available_volume'] = forms.FloatField(label="Available volume for storm water retention",required=False)
        self.fields['sum_available_volume'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_required_volume'] = forms.FloatField(label="Required volume for storm water retention",required=False)
        self.fields['sum_required_volume'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_veredict'].widget.attrs.update({'class':'labelshort'})

        self.fields['sum_construction_type'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_height_open_volume'] = forms.FloatField(label="Height open volume (h7)",required=False)
        self.fields['sum_height_open_volume'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_distance_overflow'] = forms.FloatField(label="Distance to overflow gully (h7b)",required=False)
        self.fields['sum_distance_overflow'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_vegetation_layer'] = forms.FloatField(label="Thickness vegetation layer (h8)",required=False)
        self.fields['sum_thickness_vegetation_layer'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_coarse_sand'] = forms.FloatField(label="Thickness coarse sand (h9)",required=False)
        self.fields['sum_thickness_coarse_sand'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_coarse_aggregate_26'] = forms.FloatField(label="Thickness coarse aggregate 2/6 (h10)",required=False)
        self.fields['sum_thickness_coarse_aggregate_26'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_coarse_aggregate_416'] = forms.FloatField(label="Thickness coarse aggregate 4/16 (h11)",required=False)
        self.fields['sum_thickness_coarse_aggregate_416'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_coarse_aggregate_1632'] = forms.FloatField(label="Thickness coarse aggregate 16/32 (h12)",required=False)
        #self.fields['sum_thickness_coarse_aggregate_1632'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_thickness_skeletal_soil'] = forms.FloatField(label="Thickness skeletal soil (h13)",required=False)
        self.fields['sum_thickness_skeletal_soil'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_position_draining_pipe_ditch'] = forms.FloatField(label="Position draining pipe (h15)",required=False)
        self.fields['sum_position_draining_pipe_ditch'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_ground_water_level_ditch'] = forms.FloatField(label="Distance to ground water level (h14)",required=False)
        self.fields['sum_ground_water_level_ditch'].widget.attrs.update({'class':'summary'})

        #self.fields['sum_design_duration_rain_ditch'] = forms.FloatField(label="Design duration rain fall (ditch)",required=False)
        self.fields['sum_design_duration_rain_ditch'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_design_intensity_rain_ditch'] = forms.FloatField(label="Design intensity rain fall (ditch)",required=False)
        self.fields['sum_design_intensity_rain_ditch'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_available_volume_ditch'] = forms.FloatField(label="Available volume for storm water retention (ditch)",required=False)
        self.fields['sum_available_volume_ditch'].widget.attrs.update({'class':'summary'})
        #self.fields['sum_required_volume_ditch'] = forms.FloatField(label="Required volume for storm water retention (ditch)",required=False)
        self.fields['sum_required_volume_ditch'].widget.attrs.update({'class':'summary'})

"""
class Project(models.Model):
    user = models.ForeignKey(User)
    prname = models.CharField("Project's name",max_length=200)
    prdesigner = models.CharField("Project's designer",max_length=200)

class InfoInput(models.Model):
    project = models.ForeignKey(Project)
    inwidth = models.IntegerField("Width",default=0)
    indepth = models.IntegerField("Depth",default=0)

                    (4,'Walking path'),
                (5,'Bicycle lane'),
                (6,'Street on new allotment'),
"""

