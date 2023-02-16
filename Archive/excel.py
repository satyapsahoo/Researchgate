import pandas as pd
import ast
import openpyxl
from email_finder import EmailFinder
import time
import datetime

topic = "genomics"

# Get email id and prepare final excel
df = pd.read_csv(f"{topic}.csv")
df['Author_Institution'] = df['Author_Institution'].apply(lambda x: ast.literal_eval(x))

clean_df = pd.DataFrame(columns=["Title", "Author", "Author_Profile", "Institute", "Institute_Link", "Website", "Email"])

for n in range(0, 100):
    if df["Title"][n] != "NotFound":
        article_title = df["Title"][n]
        for a in range(len(df["Author_Institution"][n])):
            author = df["Author_Institution"][n][a][0]
            author_profile = df["Author_Institution"][n][a][1]
            institute = df["Author_Institution"][n][a][2]
            institute_link = df["Author_Institution"][n][a][3]
            email_finder = EmailFinder()
            email_finder.get_email(author, institute_link)
            time.sleep(1)
            email = email_finder.email_id
            website = email_finder.website
            new_row = pd.Series({'Title': article_title,
                                 'Author': author,
                                 'Author_Profile': author_profile,
                                 'Institute': institute,
                                 'Institute_Link': institute_link,
                                 'Website': website,
                                 'Email': email
                                 })
            clean_df = pd.concat([clean_df, new_row.to_frame().T], ignore_index=False)

        with pd.ExcelWriter(f'{topic}.xlsx') as article_info:
            clean_df.to_excel(article_info, index=False)
