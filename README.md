## Acortador de URL

acortador de URL realizado en python usando la API de [Bitly](https://bitly.com/)



 Configuración:

 Una vez clonado el repo se deben ejecutar los siguientes comandos dentro del directorio 


```
pip install virtualenv
```
```
python -m virtualenv env
```
```
.\env\Scripts\activate
```

Una vez activado el environment procedemos a instalar todas las libs necesarias para que el script se ejecute correctamente

```
pip install -r requirements.txt
```

Por ultimo corremos el script. Se le debe pasar como argumento la URL (real) que necesitemos acortar.

```
python acortador_url.py https://exampleurl/test
```