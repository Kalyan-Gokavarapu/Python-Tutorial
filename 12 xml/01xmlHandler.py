import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentMovie=""
        self.type=""
        self.format=""
        self.year=""
        self.rating=""
        self.stars=""
        self.description=""
        self.counter = 0
    def startElement(self,name,attrs):
        # print ("start ele- name :", name)
        self.CurrentMovie =name        
        if name == "movie":
            self.counter+=1
            print("Movie : ",self.counter)
            title=attrs["title"]
            print("Title:", title)
        else: 
            print (attrs)              
            # description=attrs["description"]
            # print("Description:", description)

            # format=attrs["format"]
            # print("Format:", format)

            # year=attrs["year"]
            # print("Year:", year)

            # rating=attrs["rating"]
            # print("Rating:", rating)

            # stars=attrs["starts"]
            # print("Stars:", stars)
    def endElement(self,name):
        pass
        # print("end ele- name:", name)
        # if self.CurrentMovie =="type":
            # print("Type:",self.type)

#check whether executed as a script or as a module
if(__name__=="__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    Handler=MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("movies.xml")