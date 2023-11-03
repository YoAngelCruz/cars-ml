import pandas as pd

df = pd.read_csv('data_pakwheels_100.csv')

# Identificar las columnas categóricas
categorical_columns = ['company_name', 'model_name', 'location', 'engine_type', 'color', 'assembly', 'body_type', 'transmission_type', 'registration_status']

# Crear un mapeo de categorías únicas a números para cada columna categórica
category_mappings = {}
for column in categorical_columns:
    category_mappings[column] = {category: index for index, category in enumerate(df[column].unique())}

# Aplicar la codificación de categorías a cada columna categórica
for column in categorical_columns:
    new_column_name = f"{column}_category"
    df[new_column_name] = df[column].map(category_mappings[column])

#Eliminar columnas
columnas_a_eliminar = ['company_name', 'model_name', 'location', 'engine_type', 'color', 'assembly', 'body_type', 'transmission_type', 'registration_status','index']
df = df.drop(columns=columnas_a_eliminar)

print(df)

# Exportar
nombre_csv = 'data_pakwheels_e_100.csv'

df.to_csv(nombre_csv, index=False)