# Answers Module 5
## Create a new collection document with several nested fields. 
- Create

    `use climate`
    >
  > switched to db climate
 
- Create a collection with Nested data

  ``` python
  db.infoweather.insertOne({"city": {
                                        "name": 'Granada',
                                        "coord" : { "lat": 20, "lon" : 30},
                                        "temp" : [{"temp": 20}, {"temp_min": 19}]
                                        },
                                    "day" : 1
                            })     
   ```
  ```json
  {
    "acknowledged": true,
    "insertedId": ObjectId("620264458a6a858db7713b92")
  }
   ```

- Find non-nested field

  - Mongo
  
  ``` python
  db.infoweather.find({"day":{ $eq:1}})
  ```

  ```json
  {
      "_id": ObjectId("620264458a6a858db7713b92"),
      "city": {
          "name": "Granada",
          "coord": {
              "lat": 20,
              "lon": 30
          },
          "temp": [{
              "temp": 20
          }, {
              "temp_min": 19
          }]
      },
      "day": 1
  }
  ```

  - Pymongo
    
  ```python
  pprint.pprint(infoweather.find_one({'day': 1}))
  ```
    
  ``` shell
  (env) pablomoreno@nucleoo-OptiPlex-3050:~/Documents/weatherApp-master$ python api/models/answers.py 
      {
        '_id': ObjectId('6202678763b5121bb22ff9d7'),
        'city': {
            'coord': {
                'lat': 20.0,
                'lon': 30.0
            },
            'name': 'Granada',
            'temp': [{
                'temp': 20.0
            }, {
                'temp_min': 19.0
            }]
        },
        'day': 1.0
    }
  ```

- Find a document by a nested field

  - Mongo
  
  ``` shell
  db.infoweather.find({'city.name':{$exists:true,$in:["Granada"]}})
  ```
  
  ```json
  {
      "_id": ObjectId("6202678763b5121bb22ff9d7"),
      "city": {
          "name": "Granada",
          "coord": {
              "lat": 20,
              "lon": 30
          },
          "temp": [{
              "temp": 20
          }, {
              "temp_min": 19
          }]
      },
      "day": 1
  }
  ```

  - Pymongo
  
  ```python
  pprint.pprint(infoweather.find_one({'city.name':{"$exists": True,"$in":["Granada"]}}))
  ```
  
  ```json
  {'_id': ObjectId('6202678763b5121bb22ff9d7'),
   'city': {'coord': {'lat': 20.0, 'lon': 30.0},
            'name': 'Granada',
            'temp': [{'temp': 20.0}, {'temp_min': 19.0}]},
   'day': 1.0}

  ```
- Insert a new document

  - Mongo
  
  ``` shell
  db.infoweather.insertOne({"city": {
                                        "name": 'Granada',
                                        "coord" : { "lat": 20, "lon" : 30},
                                        "temp" : [{"temp": 20}, {"temp_min": 19}]
                                        },
                                    "day" : 1
                            })     
   ```

  ```json
  {
    "acknowledged": true,
    "insertedId": ObjectId("620264458a6a858db7713b92")
  }
   ```

  - PyMongo 
  ```python
  infoweather.insert_one({"city": {
                                          "name": 'Cordoba',
                                          "coord" : { "lat": 45, "lon" : 67},
                                          "temp" : [{"temp": 40}, {"temp_min": 30}]
                                          },
                                      "day" : 1
                              })
  ```
- Update a non-nested field
  - Mongo
  ```shell
  db.infoweather.updateOne({ "city.name": "Granada"}, { $set: {"day": 2 } })
  ```
  ```shell
  { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
  ```
  - Pymongo
  ```python
  infoweather.update_one({'city.name': "Granada"}, {"$set": {"day": 3}})
  ```
  
  Salida en Robo3T
  ```json
  {
      "_id" : ObjectId("6202678763b5121bb22ff9d7"),
      "city" : {
          "name" : "Granada",
          "coord" : {
              "lat" : 20.0,
              "lon" : 30.0
          },
          "temp" : [ 
              {
                  "temp" : 20.0
              }, 
              {
                  "temp_min" : 19.0
              }
          ]
      },
      "day" : 3
  }
  ```
- Update a nested field
  - Mongo
  ```shell
  db.infoweather.updateOne({ "city.name": "Granada"}, { $set: {"city.name": "Granada Capital" } })
  ```
  
  ```shell
  { "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
  ```
  
  - Pymongo

  ```python
  infoweather.update_one({'city.name': "Cordoba"}, { "$set": {"city.name": "Cordoba Capital" } })
  ```
  
  ```json
  {'_id': ObjectId('62038738516496388d84f6ff'),
   'city': {'coord': {'lat': 45, 'lon': 67},
            'name': 'Cordoba Capital',
            'temp': [{'temp': 40}, {'temp_min': 30}]},
   'day': 1}
  
  ```
- Calculate the sum or average of a numerical field

  - Mongo
  
  ```shell
  db.infoweather.aggregate([{$unwind : "$city.temp"},{ $group: { _id: "$day", total_temp:{$sum: "$city.temp.temp" }}}])
  ```
  
  ```json
  { "_id" : 3, "total_temp" : 143 }
  { "_id" : 1, "total_temp" : 40 }

  ```
  - Pymongo
  
  ```python
  exit = infoweather.aggregate([{"$unwind" : "$city.temp"},{ "$group": { "_id": "$day", "total_temp":{"$sum": "$city.temp.temp" }}}])
  for x in exit:
    print(x)
  ```
  
  ```json
  {'_id': 3, 'total_temp': 143.0}
  {'_id': 1, 'total_temp': 40}
  ```
- Calculate the max or min of a numerical field, stored in a nested field
  - Mongo
  
  ```shell
  db.infoweather.aggregate([{$unwind : "$city.temp"},{ $group: { _id: "$day", total_temp:{$max: "$city.temp.temp" }}}])
  ```
  
  ```json
  {'_id': 3, 'max_temp': 67}
  {'_id': 1, 'max_temp': 40}
  ```
  - Pymongo
  
  ```python
  exit = infoweather.aggregate([{"$unwind" : "$city.temp"},{ "$group": { "_id": "$day", "max_temp":{"$max": "$city.temp.temp" }}}])
  for x in exit:
    print(x)
  ```
  
  ```json
  {'_id': 3, 'max_temp': 67}
  {'_id': 1, 'max_temp': 40}
  ```
- Remove all elements in a collection, matching a certain criteria.
  - Mongo
  ```shell
  db.infoweather.deleteMany({ day : 1 })
  ```
  - Pymongo
  ```python
  infoweather.deleteMany({ "day" : 1 })
  ```
- Remove all elements in a collection
  - Mongo
  ```
  db.infoweather.delete_many({})
  ```
  - Pymongo
  ```python
  x = infoweather.delete_many({})
  ```

  

  