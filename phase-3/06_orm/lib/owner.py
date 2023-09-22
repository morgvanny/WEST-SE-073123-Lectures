# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes:
# name: string
# phone: string
# email: string
# address: string

import sqlite3

from pet import Pet

CONN = sqlite3.connect("lib/resources.db")
CURSOR = CONN.cursor()


class Owner:
    queried_all = False
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def pets(self):
        sql = """
            SELECT * from pets WHERE owner_id = ?
        """
        return [
            Pet.new_from_db(row) for row in CURSOR.execute(sql, (self.id,)).fetchall()
        ]

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners
            (id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            sql = """
                UPDATE owners
                SET name = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name,))
        else:
            sql = """
                INSERT INTO owners (name)
                VALUES (?)
            """
            CURSOR.execute(sql, (self.name,))
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        CONN.commit()

    @classmethod
    def create(cls, name):
        owner = cls(name)
        owner.save()
        return owner

    @classmethod
    def new_from_db(cls, row):
        return cls(row[1], row[0])

    @classmethod
    def get_all(cls):
        if not cls.queried_all:
            sql = """
                SELECT * from owners
            """

            for row in CURSOR.execute(sql).fetchall():
                owner = cls.new_from_db(row)
                cls.all[owner.id] = owner
        cls.queried_all = True
        return cls.all.values()

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * from owners WHERE name = ? LIMIT 1
        """

        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.new_from_db(row)

    @classmethod
    def find_by_id(cls, id):
        if cls.all.get(id):
            return cls.all[id]
        else:
            sql = """
                SELECT * from owners WHERE id = ?
            """

            row = CURSOR.execute(sql, (id,)).fetchone()

            if row:
                owner = cls.new_from_db(row)
                cls.all[id] = owner
                return owner

    def update(self, name=None):
        self.name = name or self.name
        self.save()

    def delete(self):
        sql = """
            DELETE FROM owners WHERE id = ?
        """
        del type(self).all[self.id]
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
