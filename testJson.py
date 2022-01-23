import json

studentJson ="""{
   "Daily": {
        "2020-07-24": {
            "1. open": "200.4200",
            "2. high": "202.8600",
            "3. low": "197.5100",
            "4. close": "201.3000",
            "5. volume": "39826989"
        },
        "2020-07-23": {
            "1. open": "207.1900",
            "2. high": "210.9200",
            "3. low": "202.1500",
            "4. close": "202.5400",
            "5. volume": "67457035"
        }
}"""

#print("Checking if percentage key exists in JSON")
data = json.loads(studentJson)
print(data["daily"])

