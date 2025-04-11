import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

# Crear carpeta de salida en "data/raw"
os.makedirs("data/raw", exist_ok=True)

# Definir ticker y fechas
ticker = "JNJ"
start_date = "2010-12-24"
# Calcular la fecha de ayer
end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

try:
    # Descargar datos SIN group_by='ticker'
    df = yf.download(ticker, start=start_date, end=end_date)
    
    # Verificamos que el DataFrame no esté vacío
    if not df.empty:
        # Si, por algún motivo, tuviera un MultiIndex en columnas, lo "aplanamos":
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)

        # Convertimos el índice 'Date' en una columna normal
        df.reset_index(inplace=True)
        
        # Guardar a CSV
        csv_path = f"data/raw/{ticker}.csv"
        df.to_csv(csv_path, index=False)
        print(f"{ticker}: ✅ Datos guardados en {csv_path}")
    else:
        print(f"{ticker}: ⚠️ No se descargaron datos en el rango especificado")
except Exception as e:
    print(f"{ticker}: ❌ Error - {e}")





