from api.models import  Jobs, Contact, DropMail, JobCategory, JobType #SosialLink
from rest_framework import serializers

class ContactSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class JobTypeSerializerArray(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ('id' ,'name',)


#class SosialLinkJobsArray(serializers.ModelSerializer):
    #class Meta:
      #  model = SosialLink
     #   fields = '__all__'

class JobsSerializerList(serializers.ModelSerializer):
    jobcategory = CategorySerializer(read_only=True)
    #sosialid = SosialLinkJobsArray(many=True)
    jobtype = JobTypeSerializerArray(read_only=True)
    class Meta:
        model = Jobs
        fields = '__all__'



class JobsSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
#('photo','companyname','jobname','jobdesj','position','experience','adress','email','website','number','salary','jobresponsibilities','jobskillrequirement','endtime','jobsqualification','jobtype','jobcategory',)



class DropMailSerializerList(serializers.ModelSerializer):
    class Meta:
        model = DropMail
        fields = '__all__'


class JobCategorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class JobTypeSerializerList(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'

#class SosialLinkSerializerList(serializers.ModelSerializer):
 #   class Meta:
  #      model = SosialLink
   #     fields = '__all__'


