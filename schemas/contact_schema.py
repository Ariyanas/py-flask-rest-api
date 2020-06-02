class ContactSchema(ma.Schema) :
    class Meta:
        fields = ('id', 'name', 'email')