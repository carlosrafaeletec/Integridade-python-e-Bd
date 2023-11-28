create database PythonSQL;

use PythonSQL;

create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
)

select * from contato