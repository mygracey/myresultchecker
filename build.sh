set -o errexit

pip install -r requirements.txt


python manage.py collectstatic --no-input

python manage.py migrate


# Note: these three commands are relevant django deployment on any platform