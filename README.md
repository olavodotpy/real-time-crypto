Here is a step-by-step guide to configuring and installing Django and the project.

# Install a Virtual Environment:

```bash
python -m venv my_virtual_environment
```

# Activate the virtual environment:

```bash
source my_virtual_environment/bin/
```

# Install the requirements:

```python
pip install -r requirements.txt
```

# Configuring Django: APPS and Projects

## Start a Django Project:

```python
django-admin startproject project_name .
```

## Start a Django APP:

```python
django-admin startapp app_name
```

## Put your APP in ```settings.py```

```python
INSTALLED_APPS = [
  'other apps...',
  'app_name',
]
```

