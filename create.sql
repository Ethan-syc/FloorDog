create table Gender
	(gender_choices char(5) primary key 
	check (gender_choices = 'M' or gender_choices = 'W' or gender_choices = 'men' or gender_choices = 'woman'));

create table Type
	(type_name char(50) primary key);

create table Accessory
	(id integer primary key references Clothes(cid),
	accessory_url1 char(500) default null,
	accessory_url2 char(500) default null,
	accessory_url3 char(500) default null,
	accessory_url4 char(500) default null,
	accessory_url5 char(500) default null,
	accessory_url6 char(500) default null,
	accessory_url7 char(500) default null,
	accessory_url8 char(500) default null,
	accessory_url9 char(500) default null,
	accessory_url10 char(500) default null);

create table Colors
	(id integer primary key references Clothes(cid),
	gender char(5) not null references Gender(gender_choices),
	color1 char(7) default null,
	color2 char(7) default null,
	color3 char(7) default null,
	color4 char(7) default null,
	color5 char(7) default null,
	color6 char(7) default null,
	color7 char(7) default null,
	color8 char(7) default null,
	color9 char(7) default null,
	color10 char(7) default null);

create table Material
	(id integer primary key references Clothes(cid),
	material_description char(200));

create table Clothes
	(cid integer primary key,
	item_url char(500) not null,
	clothes_name char(100) not null,
	gender char(5) references Gender(gender_choices),
	type char(50) references Type(type_name),
	pic_url char(500),
	clothes_detail char(500) not null,
	material char(200) references Material(material_description),
	accessory1 char(500) default null references Accessory(accessory_url1),
	accessory2 char(500) default null references Accessory(accessory_url2),
	accessory3 char(500) default null references Accessory(accessory_url3),
	accessory4 char(500) default null references Accessory(accessory_url4),
	accessory5 char(500) default null references Accessory(accessory_url5),
	accessory6 char(500) default null references Accessory(accessory_url6),
	accessory7 char(500) default null references Accessory(accessory_url7),
	accessory8 char(500) default null references Accessory(accessory_url8),
	accessory9 char(500) default null references Accessory(accessory_url9),
	accessory10 char(500) default null references Accessory(accessory_url10));


\copy Color from '/Users/shunli/Desktop/CS316/floordog/total_color.csv' delimiter ',' CSV;
\copy Clothes from '/Users/shunli/Desktop/CS316/floordog/total_clothes.csv' delimiter ',' CSV;
