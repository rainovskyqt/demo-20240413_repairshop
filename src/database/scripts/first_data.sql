INSERT INTO posts(id, name)
VALUES(1, "Администратор"),
      (2, "Менеджер"),
      (3, "Исполнитель");

INSERT INTO users (login, password, name, post_id)
VALUES("admin", "admin", "Администратор", 1),
      ("manager", "manager", "Менеджер", 2),
      ("user1", "user1", "Николай", 3),
      ("user2", "user2", "Петр", 3);

INSERT INTO equipment(id, name)
VALUES(1, "Телефон"),
      (2, "Компьютер"),
      (3, "Радиостанция");

INSERT INTO fault(id, name)
VALUES(1, "Слабая батарея"),
      (2, "Не работает экран"),
      (3, "Нет звука");

INSERT INTO status(id, name)
VALUES(1, "Принята"),
      (2, "В работе"),
      (3, "Завершена");

INSERT INTO clients(id, name, phone)
VALUES(1, "Иванов Василий","+79010001112"),
      (2, "Петров Никита", "+79220019912");

INSERT INTO orders (add_date, resolve_date, equipment_id, fault_id, description, client_id, status_id)
VALUES("2024-04-15", "2024-04-19", 1, 1, "Описание", 1, 1);
INSERT INTO orders (add_date, resolve_date, equipment_id, fault_id, description, client_id, status_id)
VALUES("2024-04-16", "", 2, 3, "Описание Другое", 2, 2);