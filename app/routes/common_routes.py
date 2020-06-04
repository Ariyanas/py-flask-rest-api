from app import app
from app.controllers.common_controller import index

# Registering common routes with handlers

app.route('/')(index)
