from app import app
from app.controllers.contacts_controller import get_contacts

# registering all contact routes with route handlers

app.route('/contacts', methods=['GET'])(get_contacts)

