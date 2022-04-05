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

---

### Sample

We used a sample from [xbrlsite.com](http://www.xbrlsite.com/US-GAAP/BasicExample/2010-09-30/Landing.html), which is downloaded to the ./sample directory by the `make` command and can be run using `make run-sample` which is equivalent to `./xbrl2oracle ./sample/abc-20101231.xml`

```shell
make
make run-sample
```
