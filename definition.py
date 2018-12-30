import unirest

#With the help of an api, this method gets the definition of the user defined word
def word(x):
    try:
        grandL = []
        response = unirest.get("twin word dictionary API" + x,
                               headers={
                                   "USING A FREE API KEY"
                               }
                               )

        return response.body['meaning']


    except:
        l = ["Such a word does not exist in this dictionary"]
        return l



#Method sends back a list of all the definitions
def organizer(dict):
    finalList = []
    for key in dict:
        if '\n' in dict[key]:
            l = dict[key].split('\n')
            finalList.extend(l)
        else:
            finalList.append(dict[key])

    return finalList


