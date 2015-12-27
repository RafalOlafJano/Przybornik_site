# Przybornik_site
Pliki strony Przybornik - projekt jeszcze nie skonczony.

Aby uruchomić stronę na silniku SQLITE proszę wkleić w pliku
mysite/setting.py kod :

DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}
