# crispy-tailwind-select-issue

This repository is a demo project to verify the fixes applied in this [pull request](https://github.com/django-crispy-forms/crispy-tailwind/pull/150) of the crispy-tailwind repository.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

- Python 3.8 or higher
- pdm

### Installing

A step by step series of examples that tell you how to get a development environment running

1. Clone the repository

```bash
git clone https://github.com/blasferna/crispy-tailwind-select-issue.git
```

2. Navigate into the cloned repository

```bash
cd crispy-tailwind-select-issue
```

3. Install dependencies

```bash
pdm install
```

4. Run migrations

```bash
pdm run python manage.py migrate
```

5. Install fixtures

```bash
pdm run python manage.py loaddata person_test_data
```

### Running the project

After installing the dependencies, you can start the project using:

```bash	
pdm start
```

This will start the server and you can navigate to http://localhost:8000 to view the project.
