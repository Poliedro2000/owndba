
def main(agrv):
    if not (4 <= len(argv) <= 5):
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (agrv[1:] + [None][:4])
    if verb  not in {'get', 'set', 'delete'}:
        usage()
        return BAD_ARGS

    db = dbdb.connect(dbname)
    try:
        if verb == 'get':
            sys.stdout.write(db[key])
        elif verb == 'set':
            db[key] = value
            db.commit()
        else:
            del db[key]
            db.commit()
    except KeyError:
        print("Key not found", file=sys.stderr)
        return BAD_KEY
    return OK