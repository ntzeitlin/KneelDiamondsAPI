-- Run this block if you already have a database and need to re-create it
DELETE FROM Metals;
DELETE FROM Sizes;
DELETE FROM Styles;
DELETE FROM Orders;

DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Orders;


-- End block

-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,

    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO 'Metals' VALUES (null, "nickel", 2);
INSERT INTO 'Metals' VALUES (null, "silver", 200);
INSERT INTO 'Metals' VALUES (null, "gold", 500);
INSERT INTO 'Metals' VALUES (null, "platinum", 5000);

INSERT INTO 'Sizes' VALUES (null, "5 caret", 200);
INSERT INTO 'Sizes' VALUES (null, "10 caret", 2000);
INSERT INTO 'Sizes' VALUES (null, "14 caret", 20000);

INSERT INTO 'Styles' VALUES (null, "retro", 200);
INSERT INTO 'Styles' VALUES (null, "modern", 200);
INSERT INTO 'Styles' VALUES (null, "futuristic", 200);

INSERT INTO 'Orders' VALUES (null, 1, 1, 1);
INSERT INTO 'Orders' VALUES (null, 1, 2, 2);
INSERT INTO 'Orders' VALUES (null, 2, 0, 0);

-- End Block