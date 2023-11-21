import csv
from django.conf import settings
from django.http import HttpResponse

import os

class CSVFileReader:
    def __init__(self, request_file):
        self.request_file = request_file
        self.file = request_file.FILES['csv_file']
        self.csv_data = self.read_csv_file()
        self.feature_data = self.read_feature_data()
        self.world_data = self.read_world_data()

    def read_csv_file(self):
        if self.request_file.method == 'POST':
            if self.file:
                # 讀取上傳的 CSV 檔案
                csv_data = self.file.read().decode('utf-8')
                # 將 CSV 數據解析為列表（每一行是一個字典）
                csv_reader = csv_data.splitlines()
                output_csv = []
                for row in csv_reader:
                    output_csv.append(row.split(','))
                print('csv_size: ', len(output_csv))
            return output_csv
        return None
                
    def read_feature_data(self):
        feature_point_list = []
        for row_data in self.csv_data:
            row_data_list = []
            for col_data in range(len(row_data)):
                if col_data %5 ==1 :
                    feature_point = [row_data[col_data], row_data[col_data+1]]
                    row_data_list.append(feature_point)
            feature_point_list.append(row_data_list)       
        return feature_point_list
    
    def read_world_data(self):
        world_point_list = []
        for row_data in self.csv_data:
            row_data_list = []
            for col_data in range(len(row_data)):
                if col_data %5 ==3 :
                    feature_point = [row_data[col_data], row_data[col_data+1], row_data[col_data+2]]
                    row_data_list.append(feature_point)
            world_point_list.append(row_data_list)       
        return world_point_list