## XBRL to Oracle

Simple example of parsing xbrl document and storing some of its data into an oracle database

**[WIP] THIS IS A WORK IN PROGRESS**

---

### Running

Fist you need to edit config.json file to contain db string, user, and password

You can also have `drop_tables` key as `true` to drop current tables

Then init using `make` and run the script with the only argument being the filepath of the xbrl file

```shell
make
./xbrl2oracle /path/to/file.xml
```

---

### Server Mode

When run without arguments, the script runs in server mode, which serves a default web ui at `http://localhost:5000/`

The server supports the following REST endpoints:

- **POST** `/xbrl2oracle` - parameters :
  - `file`
  - `db_path`
  - `db_user`
  - `db_pass`

- **GET** `/facts` - no parameters (returns json string of facts in db)


#### Detailed explanation of server mode

The program shows a web interface (form) for the user

When the user fills the form with files to upload, entry file (xbrl file) and database connection details, This data is sent to the program

The program then uploads the selected files in same directory structure as they were in user's computer

Then it parses the entry file using python library [py-xbrl](https://github.com/manusimidt/py-xbrl)

And then it saves the facts to the database in the following tables:
  - xbrlfiles table  : this table only has one column for filename (along with the id column and creation time column)
  -   - xbrlfacts table : this table has a column for file id, a column for fact name, and one for fact value (along with the id column and creation time column)

When data is saved to the db, an entry is saved to the xbrlfiles table with the entry file name as filename (the file id is used in the next step)

And then for each fact parsed from the xbrl file, an entry is saved to the xbrlfacts table with the fact name/value and the file id from the file entry saved just before (previous step), so that we know that these facts belong to that file

---

### Sample

We used a sample from [xbrlsite.com](http://www.xbrlsite.com/US-GAAP/BasicExample/2010-09-30/Landing.html), which is downloaded to the ./sample directory by the `make` command and can be run using `make run-sample` which is equivalent to `./xbrl2oracle ./sample/abc-20101231.xml`

```shell
make
make run-sample
```
