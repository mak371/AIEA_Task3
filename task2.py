from pyswip import Prolog

# Initialize Prolog engine
prolog = Prolog()

prolog.consult('kb.pl')

# Query 1: Check if Paris is the capital of France
query1 = list(prolog.query("capital_of(france, paris)"))
print(f"Query 1 (capital_of(france, paris)): {query1}")

# Query 2: Check if Berlin is the capital of Germany
query2 = list(prolog.query("capital_of(germany, berlin)"))
print(f"Query 2 (capital_of(germany, berlin)): {query2}")

# Query 3: Check if Madrid is the capital of a European country
query3 = list(prolog.query("capital_of_europe(madrid)"))
print(f"Query 3 (capital_of_europe(madrid)): {query3}")

# Query 4: Find all European capitals
query4 = list(prolog.query("capital_of_europe(Capital)"))
print(f"Query 4 (All European capitals): {query4}")

# Query 5: Check if Tokyo is the capital of a European country
query5 = list(prolog.query("capital_of_europe(tokyo)"))
print(f"Query 5 (capital_of_europe(tokyo)): {query5}")
