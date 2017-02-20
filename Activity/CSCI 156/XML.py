import xml.sax


class PetHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.breed = ""
        self.age = ""
        self.gender = ""
        self.size = ""
        self.color = ""
        self.housetrained = ""
        self.neutered = ""
        self.updatevaccinations = ""
        self.kidfriendly = ""
        self.catfriendly = ""
        self.dogfriendly = ""
        self.location = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "pet":
            print("*****New Pet*****")
            name = attributes["name"]
            print("Name:", name)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "breed":
            print("Breed:", self.breed)
        elif self.CurrentData == "age":
            print("Age:", self.age)
        elif self.CurrentData == "gender":
            print("Gender:", self.gender)
        elif self.CurrentData == "size":
            print("Size:", self.size)
        elif self.CurrentData == "color":
            print("Color:", self.color)
        elif self.CurrentData == "housetrained":
            print("House Trained:", self.housetrained)
        elif self.CurrentData == "neutered":
            print("Neutered:", self.neutered)
        elif self.CurrentData == "updatevaccinations":
            print("Up to Date Vaccinations:", self.updatevaccinations)
        elif self.CurrentData == "kidfriendly":
            print("Kid Friendly:", self.kidfriendly)
        elif self.CurrentData == "catfriendly":
            print("Cat Friendly:", self.catfriendly)
        elif self.CurrentData == "dogfriendly":
            print("Dog Friendly:", self.dogfriendly)
        elif self.CurrentData == "location":
            print("Located at:", self.location)
            print("\n")
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "breed":
            self.breed = content
        elif self.CurrentData == "age":
            self.age = content
        elif self.CurrentData == "gender":
            self.gender = content
        elif self.CurrentData == "size":
            self.size = content
        elif self.CurrentData == "color":
            self.color = content
        elif self.CurrentData == "housetrained":
            self.housetrained = content
        elif self.CurrentData == "neutered":
            self.neutered = content
        elif self.CurrentData == "updatevaccinations":
            self.updatevaccinations = content
        elif self.CurrentData == "kidfriendly":
            self.kidfriendly = content
        elif self.CurrentData == "catfriendly":
            self.catfriendly = content
        elif self.CurrentData == "dogfriendly":
            self.dogfriendly = content
        elif self.CurrentData == "location":
            self.location = content


if __name__ == "__main__":

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = PetHandler()
    parser.setContentHandler(Handler)

    parser.parse("Petfinder.xml")
