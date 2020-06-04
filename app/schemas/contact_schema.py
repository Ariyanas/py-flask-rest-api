from app import ma

class ContactSchema(ma.Schema) :
    class Meta:
        fields = ('id', 'name', 'email')