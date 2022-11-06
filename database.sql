DROP DATABASE IF EXISTS  middleware_quickbooks_test;
CREATE DATABASE middleware_quickbooks_test;

USE middleware_quickbooks_test;
DROP USER IF EXISTS 'middleware_quickbooks_admin'@'%';
CREATE USER 'middleware_quickbooks_admin'@'%' IDENTIFIED BY 'root123';
GRANT SELECT ON middleware_quickbooks_test.* TO 'middleware_quickbooks_admin'@'%';
GRANT INSERT ON middleware_quickbooks_test.* TO 'middleware_quickbooks_admin'@'%';
GRANT UPDATE ON middleware_quickbooks_test.* TO 'middleware_quickbooks_admin'@'%';
GRANT DELETE ON middleware_quickbooks_test.* TO 'middleware_quickbooks_admin'@'%';
GRANT CREATE ON middleware_quickbooks_test.* TO 'middleware_quickbooks_admin'@'%';

CREATE TABLE deliveries (
    id_delivery int NOT NULL AUTO_INCREMENT,
    direction TEXT NOT NULL,
    generation_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_delivery)
);

CREATE TABLE document_kind(
    id_kind INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_kind)
);

CREATE TABLE documents_delivery (
    id_documents_delivery INT NOT NULL AUTO_INCREMENT,
    delivery_id int NOT NULL,
    document_name text NOT NULL,
    document_type VARCHAR(100) NOT NULL,
    document_kind int NOT NULL,
    PRIMARY KEY (id_documents_delivery),
    CONSTRAINT `delivery_id` FOREIGN KEY (`delivery_id`) REFERENCES `deliveries` (`id_delivery`),
    CONSTRAINT `document_kind` FOREIGN KEY (`document_kind`) REFERENCES `document_kind` (`id_kind`)
);

INSERT INTO document_kind(description) VALUES ("DELIVERY_ORDER");
INSERT INTO document_kind(description) VALUES ("CERTIFICATE");
INSERT INTO document_kind(description) VALUES ("PICTURE");
INSERT INTO document_kind(description) VALUES ("RECEIPT");
INSERT INTO deliveries(direction) VALUES ("direccion 1");
INSERT INTO documents_delivery(delivery_id,document_name,document_type,document_kind) VALUES(1,'filepdf.pdf','application/pdf',1);
INSERT INTO documents_delivery(delivery_id,document_name,document_type,document_kind) VALUES(1,'filetxt.txt','text/plain',2);

