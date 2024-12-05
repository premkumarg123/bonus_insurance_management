#!/bin/bash

for file in split_chunk_*.sql; do
    echo "Uploading $file..."
    heroku pg:psql < $file
    if [ $? -ne 0 ]; then
        echo "Error uploading $file. Stopping."
        exit 1
    fi
done

echo "All files uploaded successfully!"

