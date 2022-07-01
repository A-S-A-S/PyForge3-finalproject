import os
import requests
from urllib.parse import urljoin
from time import sleep
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_URL = "https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/"
COMPOUNDS = {"ADP", "ATP", "STI", "ZID", "DPM", "XP9", "18W", "29P"}
DB_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()


class Compound(Base):
    __tablename__ = 'compounds'

    compound = Column(String, primary_key=True)  # works with id and name
    name = Column(String)
    formula = Column(String)
    inchi = Column(String)
    inchi_key = Column(String)
    smiles = Column(String)
    cross_links_count = Column(String)

    def __repr__(self):
        return f"{self.compound}: {self.code}"


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def get_info(key="ADP") -> dict:
    """
    Get info from "BASE_URL" for a stated "key"
    :param key: Compound of interest code
    :return: dictionary filled according to known headings
    """
    response = requests.get(urljoin(BASE_URL, key)).json()
    result = {
        "code": key,
        "name": response[key][0]["name"],
        "formula": response[key][0]["formula"],
        "inchi": response[key][0]["inchi"],
        "inchi_key": response[key][0]["inchi_key"],
        "smiles": response[key][0]["smiles"],
        "crss_lnk_cnt": len(response[key][0]["cross_links"])
    }
    return result


def save_info(compounds: tuple) -> None:
    """
    Create a query to save to the db info of compounds obtained by get_info.
    Execute it with a timeout to lower API workload
    :param compounds: (const) tuple of compound of interest
    :return: None
    """
    for x in COMPOUNDS:
        print("Now is", x)
        r = get_info(x)
        x = Compound(
            compound=r["code"],
            name=r["name"],
            formula=r["formula"],
            inchi=r["inchi"],
            inchi_key=r["inchi_key"],
            smiles=r["smiles"]
        )
        with Session() as session:
            session.add(x)
            session.commit()
        sleep(1)
