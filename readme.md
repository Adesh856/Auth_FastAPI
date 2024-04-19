# Python-FastAPI-Auth
```
FastAPI auth app learning .
```

## Packages
```
fastapi :- FastAPI is a modern web framework first released in 2018 for building RESTful APIs in Python. It is used for building APIs .

python-multipart:-It's lightweight, concurrent, and designed to serve fast web applications in the modern age.
(ASGI:- The Asynchronous Server Gateway Interface is a calling convention for web servers to forward requests to asynchronous-capable Python programming language frameworks, and applications)

python-jose[cryptography]:-

passlib[bcrypt]:- Hashing the password . 

pydantic:- Giving name to database .

psycopg2-binary:- 
sqlalchemy :- Sequelize App .
```


### Command to run 
```
uvicorn app.main:app --reload

```

## Database:
```
   MySQL :
          Migration Command :- 
                          Apply migrations to update the database: alembic upgrade head
                          Update the Schema :- alembic revision --autogenerate -m "Comment"                                                                       
```

