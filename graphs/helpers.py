import pandas as pd


def file_type_check(data, **form_name):
    for k,v in form_name.items():
        if k == 'form_name':
            form = v
        file_name = form.cleaned_data[data]
        
        if file_name.name[-3:] in ['csv']:
            data = pd.read_csv(file_name)
            #print('csv')
        if file_name.name[-3:] in ['lsx', 'xls']:
            data = pd.read_excel(file_name)
            #print('xls')
        
    return data
    
def split_into(df, root, branches, token, file_name):
    dictionary = {}
    if token.isalpha():
        token = token.lower()
        if token == 'blank':
            token = None
    for a,b in enumerate(branches):
        df[b] = None
        dictionary[a] = b
        
    
    df['middle'] = df[root].apply(lambda x : x.split(token) if isinstance(x,str) else x)
    for k,v in dictionary.items():
        for index in range(len(df)):
            try:
                df.loc[index, v] = df.loc[index, 'middle'][k]
            except:
                df.loc[index, v] = ''
                continue
    df.drop('middle', axis=1, inplace=True)
    df.to_csv(file_name, index=False)
    return df

def merge_func(**fields):
    for k, v in fields.items():
        if k == 'file_name':
            file_name = v
        if k == 'left':
            left = v
        if k == 'right':
            right = v
        if k == 'join_type':
            join_type = v
        if k == 'data_0':
            data_0 = v
        if k == 'data_1':
            data_1 = v
    if join_type == 'inner':
        composite = data_0.merge(data_1, left_on=left, right_on=right)
    if join_type == 'left':
        composite = data_0.merge(data_1, left_on=left, right_on=right, how='left')
    if join_type == 'right':
        composite = data_0.merge(data_1, left_on=left, right_on=right, how='right')
    composite.to_csv(file_name, index=False)
    return composite



       
    
        
    
