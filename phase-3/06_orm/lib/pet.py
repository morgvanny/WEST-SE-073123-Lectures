# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect("lib/resources.db")

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()


class Pet:
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id"
    # (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, owner_id, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.owner_id = owner_id
        self.id = id

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already
    # Exist

    def owner(self):
        from owner import Owner

        return Owner.find_by_id(self.owner_id)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
            (id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            temperament TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """
        CURSOR.execute(sql)
        CONN.commit()

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):
        if self.id:
            sql = """
                UPDATE pets
                SET name = ?, breed = ?, species = ?, temperament = ?, owner_id = ?
                WHERE id = ?
            """
            CURSOR.execute(
                sql,
                (
                    self.name,
                    self.species,
                    self.breed,
                    self.temperament,
                    self.owner_id,
                    self.id,
                ),
            )
        else:
            sql = """
                INSERT INTO pets (name, species, breed, temperament, owner_id)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(
                sql,
                (self.name, self.species, self.breed, self.temperament, self.owner_id),
            )
            self.id = CURSOR.lastrowid
        CONN.commit()

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament, owner_id):
        pet = cls(name, species, breed, temperament, owner_id)
        pet.save()
        return pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/
    # Attributes From DB
    @classmethod
    def new_from_db(cls, row):
        return cls(row[1], row[2], row[3], row[4], row[5], row[0])

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * from pets
        """
        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name"
    # Attribute From DB
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * from pets WHERE name = ? LIMIT 1
        """

        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.new_from_db(row)

    # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute
    # From DB

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * from pets WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.new_from_db(row)

    # @classmethod
    # def find_by(cls, attr, val):
    #     sql = """
    #         SELECT * from pets WHERE ? = ?
    #     """

    #     row = CURSOR.execute(sql, (attr, val)).fetchone()

    #     if row:
    #         return cls.new_from_db(row)

    # If No "pet" Found, return "None"

    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by(
        cls, name=None, species=None, breed=None, temperament=None, owner_id=None
    ):
        sql = """
            SELECT * FROM pets
            WHERE name = ? AND species = ? AND breed = ? AND temperament = ? AND owner_id = ?
            LIMIT 1
        """

        row = CURSOR.execute(
            sql, (name, species, breed, temperament, owner_id)
        ).fetchone()

        if row:
            return cls.new_from_db(row)
        else:
            return cls.create(name, species, breed, temperament, owner_id)

    #  Find and Retrieve "pet" Instance w/ All Attributes

    # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All
    # Attributes
    def update(
        self, name=None, species=None, breed=None, temperament=None, owner_id=None
    ):
        self.name = name or self.name
        self.species = species or self.species
        self.breed = breed or self.breed
        self.temperament = temperament or self.temperament
        self.owner_id = owner_id or self.owner_id
        self.save()

    def delete(self):
        sql = """
            DELETE FROM pets WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
