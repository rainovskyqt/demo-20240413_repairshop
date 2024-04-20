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

CREATE TABLE "equipment" (
	"id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "fault" (
	"id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "clients" (
	"id"	INTEGER,
	"name"	TEXT,
	"phone"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "status" (
	"id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "orders" (
	"id"	INTEGER,
	"add_date"	TEXT,
	"resolve_date"	TEXT,
	"equipment_id"	INTEGER,
	"fault_id"	INTEGER,
	"description"	TEXT,
	"client_id"	INTEGER,
	"status_id"	INTEGER,
	"worker_id"	INTEGER DEFAULT 2,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY(equipment_id) REFERENCES equipment(id) ON DELETE NO ACTION,
	FOREIGN KEY(fault_id) REFERENCES fault(id) ON DELETE NO ACTION,
	FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE NO ACTION,
	FOREIGN KEY(status_id) REFERENCES status(id) ON DELETE NO ACTION
	FOREIGN KEY(worker_id) REFERENCES users(id) ON DELETE NO ACTION
);