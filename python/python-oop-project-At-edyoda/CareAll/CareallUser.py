class Alluser:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender =gender
        self.status = True
    
        
    def setRating(self, rating):
        self.rating = rating
        
    def getRating(self):
        return self.rating
   

    def setReview(self,review):
        self.review = review

    def getReview(self):
        return self.review
        
    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def display(self):
        print("""available for adoption:- 
                 name: {}, 
                 Age: {},
                 gender: {},
                 """.format(self.name, self.name, self.gender))
        print("Status: {}".format(self.status))

        print("Rating: {}".format(self.rating))
        print("Review : {}".format(self.review))
    
        
        