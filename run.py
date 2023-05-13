# THIS FOR RUN APP
from far_app import app
#from far_app import routes #I GOT AN ISSUE IMPORT ROUTE FROM PACKAGE FAR_APP

# Check if run.py file has excuted file directly
if __name__ == '__main__':
    app.run(debug=True)
