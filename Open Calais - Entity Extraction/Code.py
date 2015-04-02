import io,sys
from calais import Calais
API_KEY = "rg72c9882ypfjm24tvrfu6ab"
calais = Calais(API_KEY, submitter="python-calais demo")

##read text file
with open('file3.txt', 'r') as content_file:
    content = content_file.read()

##perform analysis on text
result = calais.analyze(content)
result.print_entities()

html_file = open("HTMLFile3.html", "w")

##the resulting entities obtained are not sorted, so we sort them here:
def comp(x,y):
    return y['instances'][0]['offset'] - x['instances'][0]['offset']
sorted_results = sorted (result.entities,cmp=comp)

b = content.decode("utf-8")

for i in range (len(sorted_results)):   #for each entity
    offset = sorted_results[i]['instances'][0]['offset']    #find offset
    length = sorted_results[i]['instances'][0]['length']    #find length
    total = offset + length                                 #find total length

    if offset != sorted_results[i-1]['instances'][0]['offset']: #to prevent same words being linked twice
        if 'resolutions' in sorted_results[i]:  #if rdf document exists
            link = sorted_results[i]['resolutions'][0]['id']
            data = "<a href = \"" + link + "\" target=\"_blank\">" + sorted_results[i]['name'] + "</a>"
        else:   #if rdf document does not exist, show wikipedia page
            data = "<a href = \"http://en.wikipedia.org/wiki/" + sorted_results[i]["name"].replace (" ","_") + "\" target=\"_blank\">" + sorted_results[i]['name'] + "</a>"

        b = b[:offset] + data + b[total:]
html_file.write(b.encode('utf-8'))
html_file.close()
    
