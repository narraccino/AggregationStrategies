from collections import Counter
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import io


file = io.open("CATtrovati", mode="r", encoding="utf-32")
listCAT = file.read().splitlines()
print(Counter(listCAT))