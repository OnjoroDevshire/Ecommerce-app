from rest_framework import serializers
from .models import Product, Repair, SamsungRepair, InfinixRepair, IphoneRepair, OppoRepair,RealmeRepair, RedmiRepair, TecnoRepair, XiomiRepair

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'

class SamsungRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'

class IphoneRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'

class InfinixRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'

class OppoRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'
class XiomiRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'
class RealmeRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'
class TecnoRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'
class RedmiRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model= Repair
        fields = '__all__'
