# pwt_backup

This project is the sibling project of "pwt_app" for the Personal Workout Tracker (pwt).
The goal of this project is to provide a local SQL database that allows synchronization
(1-way sync) from the client (an Android Smartphone) to the SQL database running on 
a local desktop (in the same WLAN network). The project uses:
-  FastAPI: Endpoints for receiving client data
-  pyodbc & sqlalchemy & alembic: Dealing with SQL database

#### ToDo:
- No authentication in place 