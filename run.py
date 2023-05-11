# THIS FOR RUN APP
from far_app import app
from far_app import routes

# Check if run.py file has excuted file directly
if __name__ == '__main__':
    app.run(debug=True)
