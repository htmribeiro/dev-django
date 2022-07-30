# Python - Iniciando com DB API

## Aulas

### 02 - Escolhendo biblioteca para trabalhar com MySQL

#### Referências

* [PEP 249 – Python Database API Specification v2.0][1]
* [MySQLdb User’s Guide][2]
* [MySQLClient][3]

[1]: https://peps.python.org/pep-0249/
[2]: https://mysqlclient.readthedocs.io/user_guide.html#mysqldb-user-s-guide
[3]: https://github.com/PyMySQL/mysqlclient

---

### 04 - Instalando `mysqlclient-python` no Linux

Seguir as instruções conforme descrito no [README.md](https://github.com/PyMySQL/mysqlclient#linux>) do projeto.

* Install the MySQL development headers and libraries

  ```sh
  sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
  ```

* Install mysqlclient
  
  ```sh
  pip install mysqlclient
  ```

* Clonar o repositório

  ```sh
  git clone https://github.com/PyMySQL/mysqlclient.git
  ```

  * Acessar a pasta baixada

    ```sh
    cd mysqlclient
    ```

  * rodar o comando para instalar o `mysqlclient` na biblioteca do python.
    
    ```sh
    sudo python3 setup.py install
    ```

* Instalar o servidor MySQL
  
  ```sh
  sudo apt install mysql-server
  ```

#### Solve issue

* no módulo **`setuptools`**

  ```sh
  sudo apt install python3-setuptools
  ```

<center>

  [<< previous](#02---escolhendo-biblioteca-para-trabalhar-com-mysql) | [home](#python---iniciando-com-db-api) | [next >>](#06---testando-conexão-com-o-mysql)
  -|-|-|

</center>

---

### 06 - Testando conexão com o MySQL

* Realizando a importação do módulo MySQLdb

  ```py
  import MySQLdb
  ```

* Do módulo importado iremos utilizar a função chamada **`connect()`**
  * onde passaremos os parâmetros de conexão com o db.
    * `user='${USER_NAME}'`
    * `passwd='${USER_PASSWORD}'`
    * `db='${TARGET_DB}'`
  
  ```py
  MySQLdb.connect(user='root', passwd='root#4034', db='son_python_db_api')
  ```

* Para finalizar o arquivo de teste
  * vamos exibir uma msg de conexão bem sucedida, se a conexão estiver OK.

  ```py
  print('Conexão bem sucedida.')
  ```

* Salvar o arquivo como `teste.py` e rodar no terminal.

  ```sh
  python3 teste.py
  ```

#### Solve issue

* [How to Solve MySQL Error: Access denied for user root@localhost][1]

[1]: https://phoenixnap.com/kb/access-denied-for-user-root-localhost

<center>

  [previous](#04---instalando-mysqlclient-python-no-linux) | [home](#python---iniciando-com-db-api) | [next]()
  -|-|-|

</center>

---
