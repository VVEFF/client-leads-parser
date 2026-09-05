import pandas as pd
import json

df = pd.read_csv(
    "clients.csv",
    header=None,
    names=["name", "email", "telegram", "source", "message"]
)

required = ["name", "email", "telegram", "source", "message"]

invalid_df = df[df[required].isna().any(axis=1)]
invalid_df = invalid_df.drop_duplicates(subset=["message", "email"])

valid_df = df[~df[required].isna().any(axis=1)]
valid_df = valid_df.drop_duplicates(subset=["message", "email"])

application_account = valid_df["source"].value_counts()
clients = valid_df.to_dict(orient="records")
print("\nCLIENTS FOR CRM:")
print(clients)
valid_df.to_csv("valid_clients.csv", index=False)
invalid_df.to_csv("invalid_clients.csv", index=False)

with open("crm_clients.json", "w", encoding="utf-8") as file:
    json.dump(clients, file, ensure_ascii=False, indent=4)

'''  
    # This was supposed to be a submission to the CRM.for client in clients:  
    response = requests.post( CRM_URL,headers=HEADERS,json=client)  
    print(response.status_code)'''

print(
    "VALID\n",
    valid_df,
    "\n\nINVALID\n",
    invalid_df,
    "\n\nSTATS\n",
    application_account.to_string()
)
