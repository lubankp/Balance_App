# Imports libraries and files
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DateTime
from flask import Flask

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///balance_database.db"

# Create the extension
class DataBase(SQLAlchemy):

    def __init__(self):
        super().__init__(model_class=Base)

db = DataBase()
# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Balance(db.Model):
    """Creates Model of Database"""
    Id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    Date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    PKOSA: Mapped[float] = mapped_column(Float, nullable=False)
    Mbank: Mapped[float] = mapped_column(Float, nullable=False)
    Revolut: Mapped[float] = mapped_column(Float, nullable=False)
    Balance: Mapped[float] = mapped_column(Float, nullable=False)


def read_all():
    """Reads all records from Database"""
    with app.app_context():
        result = db.session.execute(db.select(Balance).order_by(Balance.Id))
        records = result.fetchall()
        return records

def organize_red_data():
    """Organizes red data"""
    fun_id = ['Id']
    fun_date = ['Date']
    fun_PKOSA = ['PKOSA']
    fun_Mbank = ['Mbank']
    fun_Revolut = ['Revolut']
    fun_Balance = ['Balance']

    records = read_all()
    for record in records:
        row_dict = dict(record._mapping)
        row_object = row_dict['Balance']
        fun_id.append(row_object.Id)
        fun_date.append(row_object.Date)
        fun_PKOSA.append(row_object.PKOSA)
        fun_Mbank.append(row_object.Mbank)
        fun_Revolut.append(row_object.Revolut)
        fun_Balance.append(row_object.Balance)

    return [fun_id, fun_date, fun_PKOSA, fun_Mbank, fun_Revolut, fun_Balance]


def create_table():
    """Create table schema in the database. Requires application context"""
    with app.app_context():
        db.create_all()

def create_record(date, pkosa, mbank, revolut):
    """Creates record and add to Database"""
    with app.app_context():
        balance = pkosa + mbank + revolut
        new_balance = Balance(Date=date, PKOSA=pkosa, Mbank=mbank, Revolut=revolut,
                              Balance=balance)
        db.session.add(new_balance)
        db.session.commit()

def update_record(position, new_value):
    """Allows to update value in table"""

    with app.app_context():

        if position[1] == 'PKOSA':
            value_to_update = db.session.execute(db.select(Balance).where(Balance.Id == int(position[0]))).scalar()
            value_to_update.Balance = value_to_update.Balance - value_to_update.PKOSA + float(new_value)
            value_to_update.PKOSA = new_value
        elif position[1] == 'Mbank':
            value_to_update = db.session.execute(db.select(Balance).where(Balance.Id == int(position[0]))).scalar()
            value_to_update.Balance = value_to_update.Balance - value_to_update.Mbank + float(new_value)
            value_to_update.Mbank = new_value
        elif position[1] == 'Revolut':
            value_to_update = db.session.execute(db.select(Balance).where(Balance.Id == int(position[0]))).scalar()
            value_to_update.Balance = value_to_update.Balance - value_to_update.Revolut + float(new_value)
            value_to_update.Revolut = new_value
        else:
            pass
        db.session.commit()

def delete_record(position):
    """Deletes record from table"""

    with app.app_context():
        book_to_delete = db.session.execute(db.select(Balance).where(Balance.Id == int(position[0]))).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()

def delete_all():
    """Delete all records from table"""
    with app.app_context():
        num_rows_deleted = db.session.query(Balance).delete()
        db.session.commit()



