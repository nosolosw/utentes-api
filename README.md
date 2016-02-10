API for utentes project

# Configuración inicial

    $ git clone ... utentes-api
    $ mkvirtualenv -a utentes-api utentes

    $ python setup.py develop


    $ psql -h localhost -U postgres -c "CREATE ROLE utentes LOGIN PASSWORD 'XXXX'"
    $ echo "" >> ~/.pgpass
    $ echo "*:*:*:utentes:XXXX" >> ~/.pgpass
    $ createdb -h localhost -U postgres -T template0 --owner utentes sixhiara


# Tests

 $ pg_prove -r --ext .sql -d sixhiara -U postgres -h localhost tests/

# Nomenclatura de virtualenvwrapper

Estas son las principales variables de entorno y terminología que se usa en virtualenv

*$WORKON_HOME* es el path al directorio donde estarán los distintos virtualenv que estemos usando. Es la localización donde se guardaran las librerías python que cada proyecto tenga como requisitos. El directorio debe existir, si no debemos crearlo.

*$PROJECT_HOME* es el path al directorio en el que tengamos habitualmente el código fuente de nuestros proyectos. Esta variable no es necesario fijarla. De hecho puede ser positivo no setearla para evitar "magia". Generamente será algo así como ~/projects o ~/devel.

*virtualenv* es el directorio donde estará el entorno virtual. Es decir donde estará el binario de python que estemos usando, las librerías que hayamos descargado, y también donde se _instalará_ nuestro proyecto, cuando hagamos un python setup.py develop. Cuando hayamos activado un virtualenv el path a este directorio estará recogido en la variable $VIRTUAL_ENV

*project directory* Es el directorio donde estará el código fuente del proyecto en el que estemos trabajando. Generalmente estará en una ruta del tipo. Si hemos vinculado un virtualenv a un project directory (muy recomendable) habrá un fichero .project dentro de $VIRTUAL_ENV con el path absoluto al project directory


## Instalación de virtualenv y virtualenvwrapper

    $ sudo pip install virtualenvwrapper

Añadir a .bashrc

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME= PATH_AL_DIRECTORIO_DE_PROYECTOS # No es imprescindible
    source /usr/local/bin/virtualenvwrapper.sh


Tras añadir las líneas a .bashrc hacer un:

    $ source ~/.bashrc

virtualenvwrapper permite añadir hooks tras la activación del entorno. Si, como mostramos a continuación ligamos un entorno virtual a un directorio de proyecto (donde tendremos el código fuente), podemos hacer que al activar el entorno hagamos cd automáticamente al proyecto:

    $ echo 'cdproject' >>  $WORKON_HOME/postactivate
