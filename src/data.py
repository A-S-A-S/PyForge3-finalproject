import os
import requests
import logging
from urllib.parse import urljoin
from time import sleep
from sqlalchemy import create_engine, inspect, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from pandas import json_normalize, read_sql, set_option

BASE_URL = "https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/"
COMPOUNDS = {"ADP", "ATP", "STI", "ZID", "DPM", "XP9", "18W", "29P"}
DB_URL = os.environ.get('DATABASE_URL')
logging.basicConfig(filename='logs.txt', filemode='w', level=logging.INFO)

if not DB_URL:
    print("Something wrong with DB URI, couldn't start")
else:
    engine = create_engine(DB_URL, echo=False)
    Base = declarative_base()


    class Compound(Base):
        __tablename__ = 'compounds'

        compound = Column(String, primary_key=True)
        name = Column(String)
        formula = Column(String)
        inchi = Column(String)
        inchi_key = Column(String)
        smiles = Column(String)
        cross_links_count = Column(Integer)


    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

def get_info(key="ADP"):
    """
    Get info from "BASE_URL" for a stated "key"
    :param key: Compound of interest code. By default it is the first one of COMPOUNDS tuple.
    :return: pandas.Series filled with full response
    """
    response = requests.get(urljoin(BASE_URL, key)).json()
    logging.info(f"Response got: {response}")
    sr = json_normalize(response, key).iloc[0]
    logging.info(f"Series we got: {sr}")
    return sr


def save_info(compounds: tuple) -> None:
    """
    Create a query to save to the db coulumns of interest from get_info.
    Execute it with a timeout to lower API workload
    :param compounds: (const) tuple of compound of interest
    :return: None
    """
    for x in COMPOUNDS:
        print("Now processing", x)
        sr = get_info(x)
        x = Compound(
            compound=x,
            name=sr["name"],
            formula=sr["formula"],
            inchi=sr["inchi"],
            inchi_key=sr["inchi_key"],
            smiles=sr["smiles"],
            cross_links_count=len(sr["cross_links"])
        )
        with Session() as session:
            if session.query(Compound.compound).filter_by(compound=x.compound).scalar() is None:
                session.add(x)
                session.commit()
            else:
                print("This one exists and I won't update it that way.")
        sleep(1)


def represent() -> None:
    """
    Read table "compounds" from Database into DataFrame.
    If any value is longer than 13 characters - limit it to 10 characters and add "..."
    :return: None
    """
    set_option("max_colwidth", 14)
    set_option('display.colheader_justify', 'center')
    df = read_sql("compounds", engine)
    print(df)
