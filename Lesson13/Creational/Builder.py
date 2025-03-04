class Form:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def __str__(self):
        return "\n".join(self.fields)
class User:
    def __init__(self):
        self.fields = []
    def __str__(self):
        return "\n".join(self.fields)        
class FormBuilder:
    def __init__(self):
        self.form = Form()

    def add_name_field(self,name):
        self.form.add_field(f"Name: [{name}]")
        return self

    def add_address_field(self,adressa):
        self.form.add_field(f"Address: [{adressa}]")
        return self

    def add_email_field(self,email):
        self.form.add_field(f"Email: [{email}]")
        return self

    def build(self):
        return self.form
class UserBuilder:
    def __init__(self):
        self.user = User()
    def add_name_field(self,name):
        self.user.fields.append(f"Name: [{name}]")
        return self
    def add_address_field(self,adressa):
        self.user.fields.append(f"Address: [{adressa}]")
        return self
    def add_age_field(self,age):
        self.user.fields.append(f"Age: [{age}]")
        return self
    def build(self):
        return self.user

form = FormBuilder().add_name_field('Roman').add_address_field('Moja adresa').add_email_field('moj email').build()
print(form)
print('----------------')
user = UserBuilder().add_name_field('Roman').add_age_field('39').add_address_field('Slovensko').build()
print(user)
print('----------------')
user2= UserBuilder().add_name_field('Peter').add_address_field('Slovensko').build()
print(user2)
