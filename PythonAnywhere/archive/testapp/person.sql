-- person table
create table member (
    id int primary key auto_increment,
    firstname varchar(25) not null,
    lastname varchar(25) not null,
    email varchar(50) not null,
    notes text
);

-- blog table
create table blog (
    id int primary key auto_increment,
    member_id int not null references member(id),
    bdate date not null,
    entry text
);
