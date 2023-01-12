from datetime import datetime
import graphene
from graphene_django.types import DjangoObjectType
from .models import Staff


class StaffType(DjangoObjectType):
    class Meta:
        model = Staff
        fields = '__all__'

class Query(graphene.ObjectType):
    all_staff = graphene.List(StaffType)
    staff = graphene.Field(StaffType, id=graphene.Int())

    def resolve_all_staff(self, info, **kwargs):
        return Staff.objects.all()

    def resolve_staff(self, info, id):
        return Staff.objects.get(pk=id)


class StaffMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        companyName = graphene.String(required=True)
        positionName = graphene.String(required=True)
        hireDate = graphene.Date(required=True)
        fireDate = graphene.Date(required=False)
        salary = graphene.Int(required=True)
        fraction = graphene.Int(required=True)
        base = graphene.Int(required=True)
        advance = graphene.Int(required=True)
        by_hours = graphene.Boolean(required=True)


    staff = graphene.Field(StaffType)

    @classmethod
    def mutate(cls, root, info, **user_data):
        staff = Staff(
            name=user_data.get('name'),
            companyName=user_data.get('companyName'),
            positionName=user_data.get('positionName'),
            hireDate=user_data.get('hireDate'),
            fireDate=user_data.get('fireDate'),
            salary=user_data.get('salary'),
            fraction=user_data.get('fraction'),
            base=user_data.get('base'),
            advance=user_data.get('advance'),
            by_hours=user_data.get('by_hours')
        )
        staff.save()
        return StaffMutation(staff=staff)

class UpdateMutation(graphene.Mutation):
        class Arguments:
            id = graphene.ID()
            salary = graphene.Int(required=True)
            fraction = graphene.Int(required=True)
            base = graphene.Int(required=True)
            advance = graphene.Int(required=True)
            by_hours = graphene.Boolean(required=True)

        staff = graphene.Field(StaffType)

        @classmethod
        def mutate(cls, root, info, salary, fraction, base, advance, by_hours, id):
            staff = Staff.objects.get(id=id)
            staff.salary = salary
            staff.fraction = fraction
            staff.base = base
            staff.advance = advance
            staff.by_hours = by_hours
            staff.save()
            return UpdateMutation(staff=staff)


class UpdateFireDateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    staff = graphene.Field(StaffType)

    @classmethod
    def mutate(cls, root, info, id):
        staff = Staff.objects.get(id=id)
        staff.fireDate = datetime.now()

        staff.save()
        return UpdateMutation(staff=staff)

class Mutation(graphene.ObjectType):
    add_occupation = StaffMutation.Field()
    update_occupation = UpdateMutation.Field()
    update_firedate = UpdateFireDateMutation.Field()
