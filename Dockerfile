# Utilizează o imagine oficială de Python ca bază
FROM python:3.9-slim

# Informații despre autor
LABEL authors="Adamo"

# Setează directorul de lucru în container
WORKDIR /app

# Copiază fișierul aplicației în container
COPY app.py /app/app.py

# Instalează pachetele necesare
RUN pip install streamlit psutil matplotlib

# Expune portul utilizat de Streamlit
EXPOSE 8501

# Setează comanda implicită pentru rularea aplicației
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
