import csv
import os
import random 

class Handler_CSV:
    def __init__(self, name, separator=','):
        self.name = name
        self.separator = separator
        self.data = []
        self.headers = []
        self._load_file()
        
    def _load_file(self):
        try:
            with open(self.name, newline='', encoding='utf-8') as f:
                r = csv.reader(f, delimiter = self.separator)
                self.headers = next(r)
                self.data = [row for row in r]
        except FileNotFoundError:
            print(f"file'{self.filename}' not found")
        except Exception as e:
            print(f" File downloud error: {e} ")
            
            
    def Show(self, output_type = 'top', n = 5, seporator = None):
        if seporator:
            self.separator = separator
            self._load_file()
            
        print("\n|"+"|".join(self.headers)+"|")
        print("-" * (len(self.headers)*12))
        
        rows = []
        if len(self.data) < n:
            print(f"in fail {len(self.data)}, print all")
            rows = self.data
        elif output_type == "top":
            rows = self.data[:n]
        elif output_type == "bottom":
            rows = self.data[-n:]
        elif output_type == "random":
            rows = random.sample(self.data,n)
            
        for row in rows:
            print("|" + "|".join(row) + "|")
        print()
        
        
    def inf_type(self, values):
        if not values:
            return "unknown"
        try:
            [int(v) for v in values]
            return "int"
        except:
            pass
        
        try:
            [float(v) for v in values]
            return "float"
        except:
            pass
        return "string"    
    
    
    def Info(self):
        print(f"{len(self.data)}  x {len(self.headers)}")
        col_data = list(zip(*self.data)) 
        for i, col in enumerate(col_data):
            non_empty = sum(1 for val in col if val.strip != "")
            col_type = self.inf_type([val for val in col if val.strip() != ""])
            print(f"{self.headers[i]:<15} {non_empty:<5} {col_type}")
            
            
    def DelNaN(self):
        original_len = len(self.data)
        self.data = [row for row in self.data if all(field.strip() != "" for field in row)]
        removed = original_len - len(self.data)
        print(f"delete empty row: {removed}")
        
    
    def write_csv(self, path, rows):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(self.headers)
            w.writerows(rows)
    
        
    def MakeDS(self):
        random.shuffle(self.data)
        split_point = int(len(self.data)*0.7)
        learning_data = self.data[:split_point]
        testing_data = self.data[split_point:]
        
        os.makedirs('workdata/Learning', exist_ok=True)   
        os.makedirs('workdata/Testing', exist_ok=True)  
        
        self.write_csv('workdata/Learning/train.csv', learning_data)
        self.write_csv('workdata/Testing/test.csv', testing_data)
        print('save')
        
                      
    

handler = Handler_CSV("Employees.csv")
handler.Show( output_type = 'random')
handler.Info()
handler.DelNaN()
handler.MakeDS()