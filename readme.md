# 📈 Estrategia de Trading

## 🎯 Objetivo General

Desarrollar una estrategia de inversión automatizada basada en modelos de clasificación para predecir si un activo subirá o bajará al día siguiente. Las decisiones de trading se toman utilizando probabilidades generadas por modelos de boosting (LightGBM, XGBoost, CatBoost, AdaBoost).

---

## 🧺 Portafolio de Activos

Cada integrante del grupo trabaja con un activo distinto, representando distintos mercados:

| Integrante | Activo            | Ticker        | Tipo                  |
|------------|-------------------|---------------|-----------------------|
| Roberth    | Bitcoin           | BTC-USD       | Criptomoneda          |
| Marie      | SPLV              | SPLV          | ETF (baja volatilidad)|
| Emi        | Johnson & Johnson | JNJ           | Acción (salud)        |
| Mel        | TLT               | TLT           | ETF (bonos largos)    |

---

## 🔁 Frecuencia de Trading

- **Frecuencia diaria**: se toma una decisión de inversión por día hábil.
- Las decisiones se basan en información disponible al **cierre del día actual** (`Close`).
- El modelo predice el movimiento del activo **para el siguiente día hábil**.

---

## 🧠 Estrategia Híbrida Basada en Probabilidades

Se implementa una estrategia **probabilística** que combina predicción de modelos y condiciones de confianza:

### Reglas de Decisión

| Acción     | Condición                                                             | Precio de ejecución       |
|------------|-----------------------------------------------------------------------|---------------------------|
| **Comprar**| Si `prob(subida)` > 0.6                                               | Precio de cierre actual   |
| **Vender** | Si `prob(bajada)` > 0.6 **y** se mantiene una posición abierta        | Precio de cierre actual   |
| **Hold**   | Si la probabilidad está entre 0.4 y 0.6 (zona neutra)                 | No se ejecuta transacción |

> Se asume una sola posición abierta a la vez y sin apalancamiento.

---

## 🧾 Supuestos

- Todas las operaciones se ejecutan al **precio de cierre (`Close`) del día actual**.
- No se contemplan costos de transacción, comisiones ni slippage.
- No se permite el acumulado de posiciones: solo se mantiene una posición a la vez.
- El retorno diario se calcula como:  
  \[
  \text{Return} = \frac{\text{Precio Venta} - \text{Precio Compra}}{\text{Precio Compra}}
  \]

---

## ✅ Ventajas de esta estrategia

- Evita decisiones precipitadas en zonas de baja confianza.
- Puede capturar ganancias tanto en subidas como bajadas (long/short).
- Flexible para adaptar distintos modelos y condiciones técnicas.

---