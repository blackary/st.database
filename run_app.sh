#!/bin/bash
set -e

# Restore the database if it does not already exist.
if [ -f .streamlit/database.sqlite ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
    litestream restore -v -if-replica-exists -o .streamlit/database.sqlite s3://streamlit-zcb/st-database/db
fi

# Run litestream with streamlit as the subprocess.
exec litestream replicate -exec "streamlit run --server.port 8080 --server.enableCORS false streamlit_app.py"