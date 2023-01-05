import pandas as pd 
import json
import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
database = client["aps"]

# Collection  Name
collection = database['sensor']

# file path

dataset_path='/config/workspace/aps_failure_training_set1.csv'

if __name__=='__main__':

    #read csv file
    df=pd.read_csv(dataset_path)
    print(f"Rows and Columns are {df.shape}") 

    # convert df to json fromat in order to dump data in mongodb db
    df.reset_index(drop=True,inplace=True)
    json_rec = list(json.loads(df.T.to_json()).values())

    # print 1st row
    print(json_rec[0])

    collection.insert_many(json_rec)


