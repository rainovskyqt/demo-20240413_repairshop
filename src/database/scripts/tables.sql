CREATE TABLE "posts" (
	"id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "users" (
	"id"	INTEGER,
	"login"	TEXT,
	"password"	TEXT,
	"name"	TEXT,
	"post_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY(post_id) REFERENCES posts(id) ON DELETE NO ACTION
);