import pandas as pd
import tabula.io as tabula

pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

df_read = tabula.read_pdf(pdf_path, stream=True)
# len(df_read[0])
df_pandas = pd.DataFrame(df_read[0])

df_pandas.to_csv(r'car.csv')
