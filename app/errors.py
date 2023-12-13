from flask import render_template
from app import app


# Gestionnaire d'erreur 404 (Page non trouvée)
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


# Gestionnaire d'erreur 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500
