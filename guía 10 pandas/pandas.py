# Función                Definición                                                Ejemplo de Uso
# ---------            --------------                                              ----------------
# read_csv()    Lee un archivo CSV y lo carga en un DataFrame             |        df = pd.read_csv('data.csv')

# head()        Muestra las primeras filas del DataFrame. 
#               Se le puede pasar un númeropara pedirle una N cantidad de filas.|   df.head()
#                                                                                  df.head(7)

# tail()        Muestra las últimas filas del DataFrame                       |     df.tail()

# shape         Devuelve la forma (número de filas y columnas) del DataFrame  |     shape = df.shape

# info()        Muestra información sobre el DataFrame                       |      df.info()

# describe()    Genera estadísticas descriptivas del DataFrame                |     df.describe()

# columns       Devuelve los nombres de las columnas del DataFrame            |     columns = df.columns

# dtypes        Devuelve los tipos de datos de las columnas del DataFrame    |      dtypes = df.dtypes

# dropna()      Elimina filas con valores faltantes del DataFrame            |      df.dropna()

# fillna()      Rellena los valores faltantes del DataFrame con un valor dado |     df.fillna(0)

# groupby()     Agrupa el DataFrame según una o varias columnas          |      grouped = df.groupby('columna')

# sum()         Calcula la suma de los valores en el DataFrame           |      total = df['columna'].sum()

# mean()        Calcula la media de los valores en el DataFrame          |      average = df['columna'].mean()

# max()         Encuentra el valor máximo en el DataFrame                |      max_value = df['columna'].max()

# min()         Encuentra el valor mínimo en el DataFrame      |                min_value = df['columna'].min()

# unique() Devuelve los valores únicos en una columna del DataFrame                                                      |    unique_values = df['columna']. unique()

# nunique() Devuelve el número de valores únicos en una columna del DataFrame
#                                                               |    num_unique = df['columna'].nunique()

# sort_values()  Ordena el DataFrame por una o varias columnas  |    df.sort_values('columna')
#                                                                   df.sort_values(by=['columna1','columna2'],
#                                                                   ascending=[True,False])

# merge()       Combina dos DataFrames en función de una o varias columnas
#                                                            |    merged_df = pd.merge(df1, df2, on='columna')

# to_csv()      Guarda el DataFrame en un archivo CSV       |    df.to_csv('output.csv', index=False)

# size()       Devuelve el número total de elementos en el objeto    |   total_elements = df.size

# count()    Devuelve el número de elementos no nulos en el objeto   
#                                                                   |   non_null_count = df['columna'].count()

# map()     Aplica una función o un diccionario a los elementos del objeto  
#                                                                  |    mapped_values = df['columna'].map(func)

# value_counts()   Devuelve una serie que contiene recuentos de valores únicos
#                                                             |   value_counts = df['columna'].value_counts()

# isnull()    Devuelve una máscara booleana que indica valores nulos |  is_null_mask = df['columna'].isnull()

# notnull()   Devuelve una máscara booleana que indica valores no nulos  
#                                                                   |   not_null_mask = df['columna'].notnull()
# reset_index()   Restablece los índices del DataFrame              |   df_reset = df.reset_index()

# loc[ ]        Permite la indexación y selección de datos por etiquetas. |      df.loc[2]
#                                                                               df.loc[1:3, 'columna']

# iloc[ ]      Permite la indexación y selección de datos por posición. |        df.iloc[2]
#                                                                               df.iloc[1:3, 0]

# get()     Devuelve el valor correspondiente a una clave dada      |             value = df.get('columna')