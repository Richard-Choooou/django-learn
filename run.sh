#!/bin/bash

mv ./static/* ./static_dir

gunicorn todos.wsgi -b 0.0.0.0:8000