
# Créez une plateforme pour amateurs de Nutella

La startup Pur Beurre, avec laquelle vous avez déjà travaillé, souhaite développer une plateforme web à destination de ses clients. Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop salé" (même si nous savons tous que le gras c’est la vie).

## Badges
<br><br>
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

![](https://img.shields.io/badge/Version-v1.2.1-orange)
<br><br>

## Support

For support, email [Contact Us](mailto:kololasouris@hotmail.com) or by my [Github](https://github.com/Gotha01)

<br><br>
# Color Reference

| Color             | Hex                                                       |
| ----------------- | ----------------------------------------------------------|
| Rooibos chocolat  | ![](https://via.placeholder.com/10/c45525?text=+) #c45525 |
| Moules frites     | ![](https://via.placeholder.com/10/345A61?text=+) #345A61 |
| Caramel mou       | ![](https://via.placeholder.com/10/de9440?text=+) #de9440 |
| Biscuit trempé    | ![](https://via.placeholder.com/10/e8a75d?text=+) #e8a75d |
| Bonbon rigolo     | ![](https://via.placeholder.com/10/86ebe6?text=+) #86ebe6 |

<br><br>

## Run Locally on DEBUG = True
<br>
1/ Clone the project

```bash
  git clone https://github.com/Gotha01/OCR-Project8.git
```

2/ Go to the project directory

```bash
  cd my-project
```

3/ Install dependencies

```bash
  py -m pip install -r requirements.txt
```

4/ Create database and user with 
[pgAdmin](https://www.pgadmin.org/download/pgadmin-4-windows/ "www.pgadmin.org")<br>
*__Don't forget to reconfigure the 'DATABASES' part of the /purbeurre-app/settings.py file with your information (user, db name, password).__*

5/ Make migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

6/ Fill in the database
```bash
  python manage.py incr_db 'categorie' --nbr_datas int
```
Where 'categories' is the name of a product category used by [OpenFoodFacts](https://fr.openfoodfacts.org/ "https://fr.openfoodfacts.org/"),
and "int" the maximum number of products you want to add per category.
<br><br>

7/ Start the server

```bash
  python manage.py runserver
```

8/ Open website on a browser

```browser
  http://127.0.0.1:8000/
```

## Test and coverage

Running test

```bash
coverage run --source='.' manage.py test
```

Test report

```bash
coverage report
```

## Github link

All my repositories on [Github](https://github.com/Gotha01?tab=repositories).