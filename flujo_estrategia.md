# 🗓️ Flujo Diario de la Estrategia de Trading

A continuación se explica claramente el flujo y la lógica utilizada para realizar predicciones y decisiones diarias en nuestra estrategia de trading basada en modelos de clasificación:

## 📍 Contexto Diario

Cada día tenemos disponible toda la información histórica hasta el momento actual (al cierre del día). A partir de esta información, nuestro modelo predice si el precio del activo subirá o bajará **al día siguiente**.

La decisión de compra o venta se toma inmediatamente después de realizar esta predicción, utilizando el precio de cierre del día actual como referencia.

---

## 📌 Ejemplo ilustrativo

### Supongamos hoy es **lunes 1 de abril**:

- Al final del día (al cierre de mercado), tenemos todos los datos actualizados hasta hoy.
- Con estos datos, aplicamos nuestro modelo, que predice el movimiento del precio para el día siguiente (martes 2 de abril).  
- Supongamos que el modelo predice con alta confianza (`probabilidad = 0.73`) que el precio **subirá mañana**.

Dado que la predicción es clara y supera nuestro umbral (probabilidad > 0.6), decidimos tomar una posición:

- **Compramos** el activo (por ejemplo, Bitcoin) al precio de cierre del lunes.

---

### Ahora es **martes 2 de abril**:

- Al cierre del día vemos el nuevo precio del activo.
- Nuestra ganancia o pérdida se calcula de la siguiente forma:

\[
\text{Retorno diario} = \frac{\text{Precio cierre martes} - \text{Precio cierre lunes}}{\text{Precio cierre lunes}}
\]

- Este retorno diario representa nuestra rentabilidad real para esta operación.
- Al cierre del martes, repetimos nuevamente el proceso para predecir y decidir qué hacer respecto al miércoles.

---

## 🔁 Flujo resumido del proceso diario

| Momento             | Acción                                                                     |
|---------------------|----------------------------------------------------------------------------|
| Cierre día actual   | Recolectar datos históricos y generar predicción para día siguiente.       |
| Cierre día actual   | Ejecutar compra/venta en función de la predicción generada.                |
| Cierre día siguiente| Liquidar posición, calcular rendimiento y repetir ciclo con nuevo día.     |

---

Este flujo diario asegura claridad y consistencia al momento de implementar nuestra estrategia de inversión automatizada.