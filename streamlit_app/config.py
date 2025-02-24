"""

Config file for Streamlit App

"""

from member import Member


TITLE = "Deep in the clouds"

TEAM_MEMBERS = [
    Member(
        name="Julien Lent",
        linkedin_url="https://fr.linkedin.com/in/julien-lent-627b14b0",
        github_url="https://github.com/JlnLNT",
    ),
    Member("Marc Lacourt",
           linkedin_url="https://www.linkedin.com/in/marc-lacourt/"),
    Member(name="Gabriel Kirié",
    linkedin_url="https://www.linkedin.com/in/gabriel-kirie-064ab0176/")
]

PROMOTION = "Promotion Data Scientist - Avril 2021"
