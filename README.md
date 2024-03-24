Генерация номеров через REST и WS сервисы


### Установка:
```
python -m venv venv  
.\venv\Scripts\activate (Windows)  
source venv/bin/activate  (Ubuntu)  
pip install -r requirements.txt  

для запуска REST-сервиса: uvicorn rest_numbers_service:app
для запуска REST-клиента: python.exe numbers_client.py (Windows) или python3 numbers_client.py (Ubuntu)

для запуска WS-сервиса: python.exe rest_numbers_service.py (Windows) или python3 rest_numbers_service.py (Ubuntu)
для запуска REST-клиента: python.exe ws_numbers_client.py (Windows) или python3 ws_numbers_client.py (Ubuntu) 
```

