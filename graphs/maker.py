import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px
pd.set_option('mode.chained_assignment', None)
from plotly.subplots import make_subplots
#from validators import FieldName

class SankeyMaker: 
    def __init__(self, data):       
        self._data = data
   

    def _split_month(self,data):
        '''[!!!]is the neccessary[!!!]'''
        data['Month'] = data['Event Start Date'].apply(lambda x : x.split('/')[1])
        return data

    def _filter(self, filter_column, filter_row):
        if len(filter_column) > 0  and len(filter_row) > 0:
            data = self._data[(self._data[filter_column] == filter_row)]
        else:
            data = self._data
        return data
     
    def _source_target(self,data):
        first = list()
        second = list()
        for a,b in enumerate(data.index):
            for c,d in enumerate(data.columns,len(data.index)):
                if data.loc[data.index[a],data.columns[c-len(data.index)]] != 0.0:
                    first.append(a)
                    second.append(c)
        return first, second


    def _value(self,data):
        bag = []
        for a in range(len(data.values)):
            for b in data.values[a]:
                if b != 0.0:
                    bag.append(b)
        return bag

    def _label(self,data):
        one = list(data.index)
        two = list(data.columns)
        comp = one + two
        return comp
    
    def node_name_fix(self, df,col_one, col_two):
        col_one_lab = set(df[col_one])
        col_two_lab = set(df[col_two])
        intersect_lab = col_one_lab.intersection(col_two_lab)
        def conditions(x):
            if x in intersect_lab: 
                if not isinstance(x,float):
                    if not isinstance(x,type(None)):
                        return x+" "
            else:
                return x
        df[col_two] = df[col_two].apply(conditions)
        return df
        
    def column_index_link(self,df,cols):
        index = 0 
        while index < len(cols)-1:
            index2 = index + 1
            while index2 < len(cols):
                output_df = self.node_name_fix(df, cols[index], cols[index2])
                index2 += 1
            index += 1
        return output_df

    def _aggregator(self,cols_to_use,pos,exclude, filter_column, filter_row):
        '''this will need to be modified to take in the new filter method in place of _filter'''
        df = self._filter(filter_column, filter_row)
        df = self.column_index_link(df, cols_to_use)
        df_copy = df.copy()
      
        if len(pos) != 0:
            df_copy = df_copy.set_index(pos).drop(exclude)
            df_copy.reset_index(inplace=True)
    
        sources,targets,values,labels,bag = [],[],[],[],[]
        s_num, t_num = 0,0
        for cols in range(len(cols_to_use) - 1):
            df_copy.set_index(cols_to_use[cols],inplace=True)
            matrix = pd.get_dummies(df_copy[cols_to_use[cols + 1]])
            matrix = matrix.groupby(cols_to_use[cols])[matrix.columns].sum()
            source, target = self._source_target(matrix)
            sources += [a + s_num for a in source]
            targets += [a + s_num for a in target]
            label = self._label(matrix)
            labels += label
            value = self._value(matrix)
            values += value
            s_num = max(sources) + 1
            #t_num = s_num + len(set(df_copy.index))
          
        for a in labels:
            if a not in bag:
                bag.append(a)
        labels = [(b) for a,b in enumerate(bag)]
        return sources, targets, values, labels           
                    
    def _make_sankey(self,title,cols,exclude_column,exclude_value, filter_column, filter_row):
        source, target, value, label = self._aggregator(cols,exclude_column,exclude_value, filter_column, filter_row)
        link = dict(source=source, target=target,value=value)
        node = dict(label=label, pad=35, thickness=10)
        data = go.Sankey(link=link,node=node)
        
        fig = go.Figure(data)
        fig.update_layout(
            hovermode = 'x',
            title = title,
            font = dict(size = 10, color = 'blue')
            )
        
        return fig

    def _write(self, **fields):
        for k,v in fields.items():
            if k == 'file_name':
                file_name = v
        
            if k == 'figure_title':
                figure_title = v
             
            if k == 'exclude_column':
                exclude_column = v
            if k == 'columns':
                columns = v
              
            if k == 'exclude_value':
                exclude_value = v
              
            if k == 'filter_column':
                filter_column = v
           
            if k == 'filter_value':
                filter_row = v
             
        figure = self._make_sankey(figure_title, columns, exclude_column, exclude_value, filter_column, filter_row)
        file_name = file_name+'.html'
        figure.write_html(file_name)
        return figure.to_html


class TreeMapMaker:
    def __init__(self, data):
        self._data = data
        
    def _groupby(self, value, cols):   
        df = self._data.groupby(cols)[value].count().reset_index()
        df.rename({value:'Count'}, axis=1, inplace=True)
        return df
        
    #def _write(self, file_name, constant, value, *hoverdata, **cols):
    def _write(self, **fields):
        for k,v in fields.items():
            if k == 'file_name':
                file_name = v
            if k == 'constant':
                constant = v
            if k == 'value':
                value = v
            if k == 'hoverdata':
                hoverdata = v
            if k == 'cols':
                col_one = v
        
        if hoverdata[0] is None:
            groupby_cols = col_one
        else:
            #hoverdata = hoverdata[0] 
            groupby_cols = col_one + hoverdata
        
        df = self._groupby(value, groupby_cols)
        if constant is None:
            path = []
        else:
            path = [px.Constant(constant)]
        path += col_one
               
        fig = px.treemap(df, 
                         path=path,
                         hover_data=hoverdata,
                         values=df['Count'])
        file_name = file_name +'.html'
        fig.write_html(file_name)
        print('Saving',file_name)
         
        return fig.to_html

class TableMaker:
    def __init__(self, data):
        self._data = data
    
    def _table(self, *cols):
        fig = go.Figure(data=[go.Table(
            header=dict(values=cols[0], 
                fill_color='paleturquoise', 
                align='left'),
        cells=dict(values=[self._data[a] for a in cols[0]],
                   fill_color='lavender',
              align='left'))])
        return fig
       
    def _write(self, **field_names):
        for k,v in field_names.items():
            if k == 'file_name':
                file_name = v
            if k == 'columns':
                columns = v
                
        figure = self._table(columns)
        file_name = file_name + '.html'
        figure.write_html(file_name)
        print('Saving',file_name)
        return figure.to_html

class ScatterMaker:
    def __init__(self, data):
        self._data = data
    
    def _write(self, **fieldnames):
        for k,v in fieldnames.items():
            if k == 'x':
                x = v
            if k == 'y':
                y = v
            if k == 'color':
                color = v
            if k == 'size':
                size = v
            if k == 'file_name':
                file_name = v
        fig = px.scatter(self._data, x=x,y=y,color=color, size=size)
        file_name = file_name +'.html'
        fig.write_html(file_name)
        print('Saving', file_name)
        return fig.to_html

class DonutMaker:
    def __init__(self, data):
        self._data = data
        
    def _groupby(self, **groups):
        key_dict = {}
        for k,v in groups.items():
            if k == 'donuts' :
                donuts = v
                key_dict[k] = v
            if k == 'aggregator':
                aggregator = v
            if k == 'title_text':
                title_text = v
            if k == 'file_name':
                file_name = v +'.html'
            if k == 'method':
                method = v 
        if key_dict and aggregator:
            group_list = []
            for k,v in key_dict.items():
                group_list += v
            grouped_dict = {}
            for a,b in enumerate(group_list):
                try:
                    if method.lower() == 'count':
                        group = self._data.groupby(b)[aggregator].count().to_frame().reset_index()
                        grouped_dict[a] = group
                    if method.lower() == 'mean':
                        group = self._data.groupby(b)[aggregator].mean().to_frame().reset_index()
                        grouped_dict[a] = group
                    if method.lower() == 'median':
                        group = self._data.groupby(b)[aggregator].median().to_frame().reset_index()
                        grouped_dict[a] = group
                except:
                    grouped_dict[a] = None

        return aggregator, group_list, grouped_dict, title_text, file_name

    def _build(self, **groups):
        aggregator, group_list, grouped_dict, title_text, file_name = self._groupby(**groups)
        length = len(group_list)
        if grouped_dict[0] is not None:
            fig = go.Figure(data=[go.Pie(labels=grouped_dict[0][group_list[0]], values=grouped_dict[0][aggregator])])
            fig.add_trace(go.Pie(labels=grouped_dict[0][group_list[0]], values=grouped_dict[0][aggregator], 
                                     name=group_list[0]))
            fig.update_traces(hole=0.4, hoverinfo='label+percent+name')
            fig.update_layout(title_text=title_text,
                                  annotations = [dict(text=group_list[0],x=0.5,y=0.5,font_size=15,showarrow=False)])
            fig.write_html(file_name)
            return fig.to_html
        else:
            return None
     
    def _write(self, **groups):
        figure = self._build(**groups)
        return figure
    
    