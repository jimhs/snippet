// mongorc.js
print("~/.mongorc.js actived");

// connection wrap
// only can use as func(27017,example), why?
var connectTo = function(port, dbname) {
    if (!port) {
        port = 27017;
    }

    if (!dbname) {
        dbname = "test";
    }

    db = connect("localhost:"+port+"/"+dbname);
    return db;
};

prompt = function() {
    if (typeof db == 'undefined') {
        return '(nodb)> ';
    }

    // check last db op
    try {
        nodelete();
        db.runCommand({getLastError:1});
    }
    catch (e) {
        print(e);
    }

    return db+"> ";
};

// override some dangerous "delete" command
var nodelete = function() {

    var no = function() {
        print("can't delete..");
    };

    // forbid: delete database
    db.dropDatabase = DB.prototype.dropDatabase = no;
    // forbid: delete collection
    DBCollection.prototype.drop = no;
    // forfid: delete index
    DBCollection.prototype.dropIndex = no;
};

//default editor
EDITOR = "/usr/bin/vi";
