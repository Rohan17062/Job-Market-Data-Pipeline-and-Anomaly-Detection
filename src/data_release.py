import pandas as pd
import os
import random

master=pd.read_csv("ai_job_market.csv")

if os.path.exists("jobs_incoming.csv") and os.path.getsize("jobs_incoming.csv")>0:
    incoming=pd.read_csv("jobs_incoming.csv")
else:
    incoming=pd.DataFrame(columns=master.columns)

current_size=len(incoming)
batch_size=random.choice([10,35,80,134,55,180])

end_index=min(current_size+batch_size,len(master))
next_batch=master.iloc[current_size:end_index]

if next_batch.empty:
    print("no more data left")
else:
    updated=pd.concat([incoming,next_batch],ignore_index=True)
    updated.to_csv("jobs_incoming.csv",index=False)
    print(f"added {len(next_batch)} new rows.now total rows are {len(updated)}")