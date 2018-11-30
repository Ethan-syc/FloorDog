-- create table Gender
-- 	(gender_choices varchar(5) primary key 
-- 	check (gender_choices = 'M' or gender_choices = 'W' or gender_choices = 'men' or gender_choices = 'woman'));

-- create table Type
-- 	(type_name varchar(50) primary key);

-- create table Accessory
-- 	(id integer primary key references Clothes(cid),
-- 	accessory_url1 varchar(500) default null,
-- 	accessory_url2 varchar(500) default null,
-- 	accessory_url3 varchar(500) default null,
-- 	accessory_url4 varchar(500) default null,
-- 	accessory_url5 varchar(500) default null,
-- 	accessory_url6 varchar(500) default null,
-- 	accessory_url7 varchar(500) default null,
-- 	accessory_url8 varchar(500) default null,
-- 	accessory_url9 varchar(500) default null,
-- 	accessory_url10 varchar(500) default null);

-- create table Material
-- 	(material_description varchar(200) primary key);

-- create table men_clothes
-- 	(mcid integer primary key,
-- 	item_url varchar(500) not null,
-- 	clothes_name varchar(100) not null,
-- 	gender varchar(5) references Gender(gender_choices),
-- 	type varchar(50) references Type(type_name),
-- 	pic_url varchar(500),
-- 	clothes_detail varchar(500) not null,
-- 	material varchar(200) references Material(material_description),
-- 	accessory1 varchar(500) default null references Accessory(accessory_url1),
-- 	accessory2 varchar(500) default null references Accessory(accessory_url2),
-- 	accessory3 varchar(500) default null references Accessory(accessory_url3),
-- 	accessory4 varchar(500) default null references Accessory(accessory_url4),
-- 	accessory5 varchar(500) default null references Accessory(accessory_url5),
-- 	accessory6 varchar(500) default null references Accessory(accessory_url6),
-- 	accessory7 varchar(500) default null references Accessory(accessory_url7),
-- 	accessory8 varchar(500) default null references Accessory(accessory_url8),
-- 	accessory9 varchar(500) default null references Accessory(accessory_url9),
-- 	accessory10 varchar(500) default null references Accessory(accessory_url10),
-- 	accessory11 varchar(500) default null references Accessory(accessory_url11),
-- 	accessory12 varchar(500) default null references Accessory(accessory_url12),
-- 	accessory13 varchar(500) default null references Accessory(accessory_url13));


create table men_clothes
	(mcid integer primary key,
	item_url varchar(500) not null,
	clothes_name varchar(100) not null,
	gender varchar(5),
	category varchar(50),
	pic_url varchar(500),
	clothes_detail varchar(500) not null,
	material varchar(500),
	accessory1 varchar(500) default null,
	accessory2 varchar(500) default null,
	accessory3 varchar(500) default null,
	accessory4 varchar(500) default null,
	accessory5 varchar(500) default null,
	accessory6 varchar(500) default null,
	accessory7 varchar(500) default null,
	accessory8 varchar(500) default null,
	accessory9 varchar(500) default null,
	accessory10 varchar(500) default null,
	accessory11 varchar(500) default null,
	accessory12 varchar(500) default null,
	accessory13 varchar(500) default null);

create table women_clothes
	(wcid integer primary key,
	item_url varchar(500) not null,
	clothes_name varchar(100) not null,
	gender varchar(5),
	category varchar(50),
	pic_url varchar(500),
	clothes_detail varchar(500) not null,
	material varchar(500),
	accessory1 varchar(500) default null,
	accessory2 varchar(500) default null,
	accessory3 varchar(500) default null,
	accessory4 varchar(500) default null,
	accessory5 varchar(500) default null,
	accessory6 varchar(500) default null,
	accessory7 varchar(500) default null,
	accessory8 varchar(500) default null,
	accessory9 varchar(500) default null,
	accessory10 varchar(500) default null,
	accessory11 varchar(500) default null,
	accessory12 varchar(500) default null,
	accessory13 varchar(500) default null);
	
create table men_color
	(id integer primary key references men_clothes(mcid),
	color1 varchar(7) default null,
	color2 varchar(7) default null,
	color3 varchar(7) default null,
	color4 varchar(7) default null,
	color5 varchar(7) default null,
	color6 varchar(7) default null,
	color7 varchar(7) default null,
	color8 varchar(7) default null,
	color9 varchar(7) default null,
	color10 varchar(7) default null);

create table women_color
	(id integer primary key references women_clothes(wcid),
	color1 varchar(7) default null,
	color2 varchar(7) default null,
	color3 varchar(7) default null,
	color4 varchar(7) default null,
	color5 varchar(7) default null,
	color6 varchar(7) default null,
	color7 varchar(7) default null,
	color8 varchar(7) default null,
	color9 varchar(7) default null,
	color10 varchar(7) default null);




\copy men_clothes from '/Users/shunli/Desktop/CS316/floordog/men.csv' delimiter ',' CSV;
\copy women_clothes from '/Users/shunli/Desktop/CS316/floordog/women.csv' delimiter ',' CSV;
\copy men_color from '/Users/shunli/Desktop/CS316/floordog/men_color.csv' delimiter ',' CSV;
\copy women_color from '/Users/shunli/Desktop/CS316/floordog/women_color.csv' delimiter ',' CSV;
