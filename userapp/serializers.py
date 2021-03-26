from rest_framework import serializers
from userapp.models import User, UserAddress, UserRemark


class UserSerializer(serializers.HyperlinkedModelSerializer):
    model = User
    
    class Meta:
        # fields = '__all__'
        model = User
        fields = ('id', 'name', 'userid', 
            'dob', 'status',
            'created', 'updated',)
        read_only_fields = ('id', 'created', 'updated')
        required_fields = (
            'id', 'name',  'userid'
            )
        extra_kwargs = {field: {'required': True} for field in required_fields}


class UserAddressSerializer(serializers.HyperlinkedModelSerializer):
    model = UserAddress
    
    class Meta:
        # fields = '__all__'
        model = UserAddress
        fields = ('id', 'user', 'address', 
            'created', 'updated',)
        read_only_fields = ('id', 'created', 'updated')
        required_fields = (
            'id', 'user',  'address'
            )
        extra_kwargs = {field: {'required': True} for field in required_fields}


class UserRemarkSerializer(serializers.HyperlinkedModelSerializer):
    model = UserRemark
    
    class Meta:
        # fields = '__all__'
        model = UserRemark
        fields = ( 'user', 'userremark', 
            'created', 'updated',)
        read_only_fields = ('created', 'updated')
        required_fields = (
            'user',  'userremark'
            )
        extra_kwargs = {field: {'required': True} for field in required_fields}
