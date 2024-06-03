import pandas as pd
import os
def replace_special_chars(df):
    return df.applymap(lambda x: x.replace('à', 'a').replace('é', 'e') if isinstance(x, str) else x)

def xls_to_csv(directory, sheet_name=None):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if filename.endswith('.xls'):
                df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')
            elif filename.endswith('.xlsx'):
                df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
            else:
                continue

            df = replace_special_chars(df)
            csv_file_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '.csv')
            df.to_csv(csv_file_path, index=False)
            print(f'Transformed {file_path} to {csv_file_path}')
        except Exception as e:
            print(f'Error processing file {file_path} as Excel: {e}')
            try:
                df = pd.read_csv(file_path, sep=None, engine='python')  
                df = replace_special_chars(df)
                csv_file_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '.csv')

                df.to_csv(csv_file_path, index=False)
                print(f'Transformed {file_path} to {csv_file_path} (read as CSV)')
            except Exception as e:
                print(f'Error processing file {file_path} as CSV: {e}')


directory = 'dataset/Elections_eu/'

sheet_name = 'Départements'

xls_to_csv(directory, sheet_name)