/*CREATE DATABASE IF4100_TURRIALBA_B03103;
USE IF4100_TURRIALBA_B03103;
*/

/*
CREATE TABLE AUTOR (
    CODIGO INT PRIMARY KEY NOT NULL,
    NOMBRE VARCHAR(30) NOT NULL
);


CREATE TABLE LIBRO (
    CODIGO_LIBRO INT PRIMARY KEY NOT NULL,
    TITULO VARCHAR(50) NOT NULL,
    ISBN VARCHAR(15) NOT NULL,
    PAGINAS INT NOT NULL,
    EDITORIAL VARCHAR(25)
);


CREATE TABLE AUTOR_LIBRO (
    CODIGO_AUTOR INT NOT NULL,
    CODIGO_LIBRO INT NOT NULL,
    PRIMARY KEY (CODIGO_AUTOR, CODIGO_LIBRO),
    FOREIGN KEY (CODIGO_AUTOR) REFERENCES AUTOR(CODIGO),
    FOREIGN KEY (CODIGO_LIBRO) REFERENCES LIBRO(CODIGO_LIBRO)
);


CREATE TABLE EJEMPLAR (
    CODIGO_EJEMPLAR INT PRIMARY KEY NOT NULL,
    CODIGO_LIBRO INT NOT NULL,
    LOCALIZACION VARCHAR(30),
    FOREIGN KEY (CODIGO_LIBRO) REFERENCES LIBRO(CODIGO_LIBRO)
);


CREATE TABLE USUARIO (
    CODIGO_USUARIO INT PRIMARY KEY NOT NULL,
    NOMBRE VARCHAR(20) NOT NULL,
    APELLIDOS VARCHAR(40) NOT NULL,
    TELEFONO VARCHAR(10),
    DIRECCION VARCHAR(100) NOT NULL,
    CARRERA VARCHAR(40) NOT NULL
);


CREATE TABLE PRESTAMO (
    ID_PRESTAMO INT AUTO_INCREMENT PRIMARY KEY,
    CODIGO_USUARIO INT NOT NULL,
    CODIGO_EJEMPLAR INT NOT NULL,
    FECHA_PRESTAMO DATE NOT NULL,
    FECHA_DEVOLUCION DATE NOT NULL,
    FOREIGN KEY (CODIGO_USUARIO) REFERENCES USUARIO(CODIGO_USUARIO),
    FOREIGN KEY (CODIGO_EJEMPLAR) REFERENCES EJEMPLAR(CODIGO_EJEMPLAR)
);*/

/*INSERT INTO AUTOR (CODIGO, NOMBRE) VALUES
(1, 'Gabriel García Márquez'),
(2, 'Isabel Allende'),
(3, 'Mario Vargas Llosa');*/

/*INSERT INTO LIBRO (CODIGO_LIBRO, TITULO, ISBN, PAGINAS, EDITORIAL) VALUES
(1, 'Cien Años de Soledad', '978-1234567890', 471, 'Sudamericana'),
(2, 'La Casa de los Espíritus', '978-9876543210', 432, 'Debolsillo');
*/

/*INSERT INTO EJEMPLAR (CODIGO_EJEMPLAR, CODIGO_LIBRO, LOCALIZACION) VALUES
(1, 1, 'Turrialba'),
(2, 2, 'San Pedro');


INSERT INTO USUARIO (CODIGO_USUARIO, NOMBRE, APELLIDOS, TELEFONO, DIRECCION, CARRERA) VALUES
(10000, 'Aracely', 'Soto', '84848484', 'Cartago, Turrialba', 'Informática'),
(10001, 'Fabricio', 'Castillo', '25529696', 'San José, San Pedro', 'Dirección Empresas');

INSERT INTO PRESTAMO (CODIGO_USUARIO, CODIGO_EJEMPLAR, FECHA_PRESTAMO, FECHA_DEVOLUCION) VALUES
(10000, 1, '2024-11-01', '2024-11-15'),
(10001, 2, '2024-11-03', '2024-11-17');
*/

SELECT * FROM AUTOR;

/*SELECT * FROM USUARIO;


SELECT L.TITULO, E.CODIGO_EJEMPLAR, E.LOCALIZACION
FROM LIBRO L
JOIN EJEMPLAR E ON L.CODIGO_LIBRO = E.CODIGO_LIBRO;

SELECT P.ID_PRESTAMO, U.NOMBRE, L.TITULO, P.FECHA_PRESTAMO, P.FECHA_DEVOLUCION
FROM PRESTAMO P
INNER JOIN USUARIO U ON P.CODIGO_USUARIO = U.CODIGO_USUARIO
INNER JOIN EJEMPLAR E ON P.CODIGO_EJEMPLAR = E.CODIGO_EJEMPLAR
INNER JOIN LIBRO L ON E.CODIGO_LIBRO = L.CODIGO_LIBRO;
*/

/*
DELIMITER $$

CREATE PROCEDURE InsertarPrestamo(
    IN codigo_usuario INT,
    IN codigo_ejemplar INT
)
BEGIN
    INSERT INTO PRESTAMO (CODIGO_USUARIO, CODIGO_EJEMPLAR, FECHA_PRESTAMO, FECHA_DEVOLUCION)
    VALUES (codigo_usuario, codigo_ejemplar, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 15 DAY));
END$$

DELIMITER ;

CALL InsertarPrestamo(10003, 1);
*/

/*
Procedimiento para Consultar Libros
DELIMITER $$

CREATE PROCEDURE ConsultarLibros(
    IN p_codigo_libro INT,
    IN p_titulo VARCHAR(50),
    IN p_isbn VARCHAR(15),
    IN p_paginas INT,
    IN p_editorial VARCHAR(25)
)
BEGIN
    SELECT *
    FROM LIBRO
    WHERE (p_codigo_libro IS NULL OR CODIGO_LIBRO = p_codigo_libro)
      AND (p_titulo IS NULL OR TITULO LIKE CONCAT('%', p_titulo, '%'))
      AND (p_isbn IS NULL OR ISBN = p_isbn)
      AND (p_paginas IS NULL OR PAGINAS = p_paginas)
      AND (p_editorial IS NULL OR EDITORIAL LIKE CONCAT('%', p_editorial, '%'));
END$$

DELIMITER ;

CALL ConsultarLibros(NULL, 'Cien Años', NULL, NULL, NULL); -- Busca libros por título
CALL ConsultarLibros(1, NULL, NULL, NULL, NULL); -- Busca por ID del libro
*/

/*procedimiento para actualizar autores

DELIMITER $$

CREATE PROCEDURE ActualizarAutor(
    IN p_codigo_autor INT,
    IN p_nombre VARCHAR(30)
)
BEGIN
    UPDATE AUTOR
    SET NOMBRE = p_nombre
    WHERE CODIGO = p_codigo_autor;
END$$

DELIMITER ;

CALL ActualizarAutor(1, 'Gabriel García Márquez');
*/

/*procedimiento para borrar estudiantes

DELIMITER $$

CREATE PROCEDURE BorrarEstudiante(
    IN p_codigo_usuario INT
)
BEGIN
    DELETE FROM USUARIO
    WHERE CODIGO_USUARIO = p_codigo_usuario;
END$$

DELIMITER ;
*/

/*
INSERT INTO USUARIO (CODIGO_USUARIO, NOMBRE, APELLIDOS, TELEFONO, DIRECCION, CARRERA)
VALUES
(10004, 'Ana', 'Castro', '88001122', 'San José, Central', 'Medicina'),
(10005, 'Luis', 'Ramírez', '87003344', 'Cartago, Occidental', 'Ingeniería'),
(10006, 'María', 'Chacón', '85002233', 'Alajuela, Central', 'Derecho'),
(10007, 'Pedro', 'Sánchez', '84009988', 'Heredia, Santo Domingo', 'Arquitectura'),
(10008, 'Laura', 'Vargas', '83007755', 'Limón, Central', 'Biología');


SELECT * FROM AUTOR;

INSERT INTO AUTOR (CODIGO, NOMBRE)
VALUES
(4, 'J.K. Rowling'),
(5, 'Stephen King');
*/

/*
SELECT * FROM LIBRO;

INSERT INTO LIBRO (CODIGO_LIBRO, TITULO, ISBN, PAGINAS, EDITORIAL)
VALUES
(3, 'Harry Potter y la Piedra Filosofal', '978-0439554930', 309, 'Bloomsbury'),
(4, 'El Resplandor', '978-0450040184', 447, 'Hodder & Stoughton'),
(5, 'Conversación en La Catedral', '978-8432204119', 608, 'Alfaguara');
*/

/*
SELECT * FROM USUARIO;
INSERT INTO EJEMPLAR (CODIGO_EJEMPLAR, CODIGO_LIBRO, LOCALIZACION)
VALUES
(3, 3, 'Cartago'),
(4, 4, 'Alajuela'),
(5, 5, 'Heredia');

INSERT INTO USUARIO (CODIGO_USUARIO, NOMBRE, APELLIDOS, TELEFONO, DIRECCION, CARRERA)
VALUES
(10009, 'Andrés', 'Gómez', '88993311', 'Limón, Calle Central', 'Administración'),
(10010, 'Mariana', 'Lopez', '85113344', 'San Carlos, Quesada', 'Enfermería'),
(10011, 'Carlos', 'Hernández', '88774455', 'Pérez Zeledón, Calle Sur', 'Psicología'),
(10012, 'Rocío', 'Méndez', '88665544', 'Puntarenas, Centro', 'Ingeniería');

INSERT INTO AUTOR_LIBRO (CODIGO_AUTOR, CODIGO_LIBRO)
VALUES
(1, 1), -- Gabriel García Márquez - Cien Años de Soledad
(2, 2), -- Isabel Allende - La Casa de los Espíritus
(3, 5), -- Mario Vargas Llosa - Conversación en La Catedral
(4, 3), -- J.K. Rowling - Harry Potter y la Piedra Filosofal
(5, 4); -- Stephen King - El Resplandor
*/







CALL InsertarPrestamo(10001, 2);

CALL ConsultarLibros(NULL, 'Cien', NULL, NULL, NULL);

CALL ActualizarAutor(2, 'Isabel Allende Actualizada');

CALL BorrarEstudiante(10001);

SELECT * FROM AUTOR;
SELECT * FROM LIBRO;
SELECT * FROM EJEMPLAR;
SELECT * FROM USUARIO;
SELECT * FROM AUTOR_LIBRO;
SELECT * FROM PRESTAMO;

CALL InsertarPrestamo(10010, 3);

CALL BorrarEstudiante(10012);

CALL ConsultarLibros(NULL, 'Cien', NULL, NULL, NULL);


CALL ActualizarAutor(2, 'Rolando Herrera');

CALL ConsultarLibros(NULL, 'Cien', NULL, NULL, NULL);


