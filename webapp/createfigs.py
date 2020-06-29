import numpy as np
import pandas as pd
import math
import plotly.express as px
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import plotly.graph_objects as go


def get_data(n_points=1000):
    accName='storagebigbyte'
    accKey='9kFGj5tyjdHdnxY4LfkmcLaAeygcjaaEm9rS+5UvUB741t4lnJ0zrqznx/hi2P3ptAZF1c20YKN6tMnWuFXayA=='

    table_service = TableService(account_name=accName, account_key=accKey)
    
    tasks = table_service.query_entities('timevssignal',num_results=n_points)
    
    df = pd.DataFrame()
    
    for task in tasks:
        df = df.append(pd.Series(task,name=task.RowKey))
    
    return df


def fig1(n_points=1000):
 
    fig = px.scatter(get_data(n_points), x="Time", y="signal", 
    color="signal", hover_name="Timestamp",)

    return fig




