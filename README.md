necessary step to install the project and configure a Django.

## Install a Virtual Environment:

```python
python -m venv my_virtual_environment
```

## Activate the virtual environment:

```bash
source my_virtual_environment/bin/
```

## Install the requirements:

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

