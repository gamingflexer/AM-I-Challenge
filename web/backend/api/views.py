from flask_restful import Resource

class helloworld(Resource):
    def get(self):
        return "Hello World!"
    
'''
    crime_ref = db.collection(u'crimes')
    docs = crime_ref.stream()

    for doc in docs:
        data1 = data.update({doc.id : doc.to_dict()})
        
    db.collection("cluster_test").add(test)
    
    "lastUpdated":firestore.SERVER_TIMESTAMP
    
    delete_collection(cluster_ref,3)
'''