from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ('id',)


class StudentCreateSerializer(serializers.ModelSerializer):

    '''

    ###### Validators ###################
    def start_with_r(val):
        if val[0].lower()!='r':
            raise serializers.ValidationError("Name Should Start with R or r")
        return val

    '''
    # name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model=Student
        fields = ('id', 'name', 'roll', 'city')





    '''
    ####### Field Level Validation #######

    def validate_roll(self, val):
        if val >= 200:
            raise serializers.ValidationError("Seats are Full!!!!!!!!")
        return val
    '''



    '''

    ####### Object Level Validation #########

    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower()=='dummy' and city.lower()!='amritsar':
            raise serializers.ValidationError('City Must be Amritsar!!!!!!')
        return data

    '''

