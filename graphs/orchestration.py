from .maker import *

class OrchestrationLayer:
    def __init__(self, **payload):
        self.payload = payload
    
    def build(self):
        if self.payload['genus'].lower() == 'tree':
            fig = TreeMapMaker(self.payload['data'])
            return fig._write(file_name = self.payload['file_name'], 
                               constant = self.payload['constant'], 
                               value = self.payload['value'], 
                               hoverdata = self.payload['hover_data'],
                               cols = self.payload['cols'])
        
        if self.payload['genus'].lower() == 'sankey':
            fig = SankeyMaker(self.payload['data'])
            return fig._write(file_name = self.payload['file_name'],
                              figure_title = self.payload['figure_title'],
                              columns = self.payload['columns'],
                              exclude_column = self.payload['exclude_column'],
                              exclude_value = self.payload['exclude_value'],
                              filter_column = self.payload['filter_column'],
                              filter_value = self.payload['filter_value']
                             )
        
        if self.payload['genus'].lower() == 'table':
            fig = TableMaker(self.payload['data'])
            return fig._write(file_name = self.payload['file_name'],
                             columns = self.payload['columns'])
                             
        
        if self.payload['genus'].lower() == 'scatter':
            fig = ScatterMaker(self.payload['data'])
            return fig._write(file_name = self.payload['file_name'],
                              x = self.payload['x'],
                              y = self.payload['y'],
                              color = self.payload['color'],
                              size = self.payload['size']
                             )
        
        if self.payload['genus'].lower() == 'donut':
            fig = DonutMaker(self.payload['data'])
            return fig._write(
                              donuts = self.payload['donuts'],
                              aggregator = self.payload['aggregator'],
                              title_text = self.payload['title_text'],
                              file_name = self.payload['file_name'],
                              method = self.payload['method']
                             )