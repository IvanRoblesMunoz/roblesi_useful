

def EDA(data):

    ''' 
    
    Returns a review of the column types, number and percentages of Null and unique values
    
    Args:
      data (pandasDataFrame) : data to be evaluated
    
    Returns:
      Columns (pandasDataFrame) : a pandas dataframe with the overview of the data as mentioned above, it contains a row per column in the orginal dataframe to evaluate
      
    '''

    # search column names, types, Nulls
    Columns=pd.DataFrame(columns=['col_name'],data=data.columns)
    Columns['col_type']=pd.DataFrame(columns=['col_type'],data=data.dtypes).set_index(Columns.index)
      
    # Columns with missing values
    Nulls= pd.DataFrame(data.isnull().sum(), columns=['Null'])
    Nulls['Null_perc']=Nulls['Null']/len(data)*100
    Nulls=Nulls.reset_index().rename(columns={"index": "col_name"})
    Columns=Columns.merge(Nulls, left_on='col_name', right_on='col_name', how='outer')
    
    # Count Number of unique values
    nunique=pd.DataFrame( data[list(Columns['col_name'])].nunique(), columns=['unique_count'])
    nunique['unique_count_perc']=nunique['unique_count']/len(data)*100
    nunique=nunique.reset_index().rename(columns={"index": "col_name"})
    Columns=Columns.merge(nunique, left_on='col_name', right_on='col_name', how='outer')
    return Columns




