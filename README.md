# 🚀 Microservicio de Usuarios - CineMusic

## 📋 Descripción
Este microservicio es parte del ecosistema de CineMusic y se encarga de gestionar toda la lógica relacionada con los usuarios del sistema. Está desarrollado usando FastAPI y sigue los principios de arquitectura hexagonal.

## 🛠️ Tecnologías Principales

- 🐍 Python
- 🚀 FastAPI
- 🔐 SQLAlchemy
- 📦 Pydantic
- 🐳 Docker 
- 🗄️ MySQL

## 📦 Estructura del Proyecto

```
microservice-user/
├── app/
│   ├── configuration/     # 🛠️ Configuración del servidor
│   └── src/
│       ├── application/   # 📱 Lógica de aplicación
│       ├── domain/       # 📚 Dominio y modelos
│       └── infrastructure/ # 🏗️ Infraestructura
├── docker/              # 🐳 Configuración Docker
├── docker-compose.yml   # 📋 Orquestación de servicios
└── requirements.txt     # 📦 Dependencias
```
## 📊 Modelo de Usuario

El modelo de usuario incluye los siguientes campos y caracteristicas:

| Campo     | Tipo de Dato | Descripción | Requerido | Restricciones |
|-----------|--------------|-------------|-----------|---------------|
| `id`      | `string`     | Identificador único del usuario | ✅ | UUID v4 |
| `name`    | `string`     | Nombre completo del usuario | ✅ | Mínimo 2 caracteres |
| `email`   | `string`     | Email del usuario | ✅ | Formato email válido, único |
| `password`| `string`     | Contraseña encriptada | ✅ | Mínimo 8 caracteres |
| `roles`   | `list[str]`  | Lista de roles del usuario | ✅ | Debe contener al menos un rol |

## 🚀 Configuración y Ejecución


### 📝 Variables de Entorno

El microservicio utiliza las siguientes variables de entorno:

#### 🔧 Servidor
- `HOST`: Host del servidor (default: 0.0.0.0)
- `PORT`: Puerto del servidor (default: 2000)
- `DEBUG`: Modo debug (true/false)

#### 🗄️ Base de Datos

**Desarrollo**
- `DATABASE_URL_DEV`: URL de la base de datos en desarrollo

**Producción**
- `DATABASE_URL`: URL completa de la base de datos
- `MYSQL_DATABASE`: Nombre de la base de datos
- `MYSQL_USER`: Usuario de MySQL
- `MYSQL_PASSWORD`: Contraseña de MySQL
- `MYSQL_ROOT_PASSWORD`: Contraseña root de MySQL

#### 📡 CORS
- `ALLOW_ORIGINS`: Orígenes permitidos
- `ALLOW_CREDENTIALS`: Permite credenciales
- `ALLOW_METHODS`: Métodos HTTP permitidos
- `ALLOW_HEADERS`: Headers permitidos

#### 📚 Swagger
- `VERSION`: Versión de la API
- `TITLE`: Título de la documentación


### 🐳 Docker

Para ejecutar el servicio usando Docker:

```bash
# Construir y ejecutar los servicios
docker-compose up --build

# Detener los servicios
docker-compose down
```

### 📋 Requisitos

1. 🐳 Docker y Docker Compose instalados
2. 🐍 Python 3.8+
3. 📦 Dependencias del proyecto (ver requirements.txt)

## 🛠️ Desarrollo Local

Para ejecutar el servicio en modo desarrollo:

```bash
#Crear un entorno con python
python -m venv env

# Activar el entorno en linux y mac
source env/bin/activate

# Activar el entorno en windows
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python main.py
```

```python
#se usar el comando (python main.py) ya que el archivo main.py es el punto de entrada del microservicio y esta configurado para que automaticamente arranque uvicorn en modo --reload

if __name__ == "__main__":
    os.system(f"uvicorn main:app --host {HOST} --port {PORT} --reload")
```

Recuerda tener presente que se necesita un archivo `.env` en la raiz del proyecto con las variables de entorno para que docker automaticamente pueda levantar el contenedor con dichas variables.


## 📚 Documentación API

La documentación de la API está disponible en:

- 🌐 Swagger UI: http://localhost:2000/docs
- 📄 Redoc: http://localhost:2000/redoc

## 🛡️ Seguridad

El microservicio implementa:

- 🔒 Encriptación de contraseñas
- 🛡️ Manejo de errores global
- 📡 CORS configurado

## 🚀 Características Principales

- 📱 Gestión completa de usuarios
- 📦 Inyección de dependencias
- 📊 Manejo de errores
- 🔄 Contexto asíncrono