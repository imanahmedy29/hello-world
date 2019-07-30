CREATE database customers;
USE customers;
-- see how many customers are in our table: (use back ticks for strings)
select count(*) as `Customer Count` from Customer;

-- how many unique companies are in our table?
select count(distinct company) as 'Distinct Companies' from Customer;

-- add an Id to the customer table
alter table Customer add CustomerId int not null primary key auto_increment;

-- add a column for the CompanyID to the customers table
alter table Customer add CompanyID int;

-- notice that the companyId is null
select companyID, company from Customer;

-- create a table for the companies
-- this statement will also create a companyID column which will
-- increment when you insert a new record
create table Company (
companyID int NOT NULL AUTO_INCREMENT,
Company varchar(255),
primary key (companyID)
);

-- see what's in your company table now
select * from Company;

-- generate a sql statement which shows which companies will be added to the new customer table
select distinct company from Customer where length(company)>0 and company is not null  order by company;

-- add the above companies from customers to the company table
insert into Company (company) select distinct company from Customer where length(company)>0 and company is not null  order by company;

-- look at what you've done
select * from Company;


-- update the companyId in the customers table
update Customer c set c.companyID = (select t.companyID from
Company t where t.company=c.company);

-- query to check your data
select c.companyID,c.company,t.companyID,t.Company from
Customer c inner join Company t on c.CompanyID=t.CompanyID;

-- remove the company column from the customers table. It is no longer needed
alter table Customer drop column company;

-- also remove fullname, we don't need calculated columns. They're a maintenance headache
alter table Customer drop column fullname;

-- You can generate fullname more efficiently as:
select CONCAT(`FirstName`,' ',`LastName`) as `Full Name` from Customer;
select * from Customer;

-- notice you won't see the company (or fullname) column
select * from Customer;

-- the company column and the id are in Company
select * from Company;

-- a query to bring it all back together
select CONCAT(`FirstName`,' ',`LastName`) as `Full Name`, company from Customer 
inner join Company on 
customer.companyid=Company.companyid;

-- EXERCISE --


select * from Customer;
-- There are 300 customers total

-- how many unique cities and states are in our table? 288 cities and 46 states
select count(distinct City) as 'Distinct Cities' from Customer;
select count(distinct State) as 'Disinct States' from Customer;

-- add a column for the CityID and one for the StateID to the customers table
alter table Customer add CityID int;
alter table Customer add StateID int;

-- create cities table
create table Cities (
CityID int NOT NULL AUTO_INCREMENT,
City varchar(288),
primary key (CityID)
);

select * from Cities;

-- create states table
create table States (
StateID int NOT NULL AUTO_INCREMENT,
State varchar(46),
primary key (StateID)
);

select * from States;


-- generate a sql statement which shows which cities/states will be added to the new customer table
select distinct City from Customer where length(City)>0 and City is not null  order by City;
select distinct State from Customer where length(State)>0 and State is not null  order by State;

-- add the above cities/states from customers to the appropriate table
insert into Cities (City) select distinct City from Customer where length(City)>0 and City is not null  order by City;

insert into States (State) select distinct State from Customer where length(State)>0 and State is not null  order by State;


-- update the CityID and StateID in the customers table
update Customer c set c.CityID = (select y.CityID from
Cities y where y.City=c.City);

update Customer c set c.StateID = (select m.StateID from
States m where m.State=c.State);

-- query to check your data
select c.CityID,c.City,y.CityID,y.City from
Customer c inner join Cities y on c.CityID=y.CityID;

select c.StateID,c.State,m.StateID,m.State from
Customer c inner join States m on c.StateID=m.StateID;

-- remove the City and State columns from the customers table. It is no longer needed
alter table Customer drop column City;
alter table Customer drop column State;

select * from Customer;
select * from City;

-- a query to bring it all back together
select CONCAT(`FirstName`,' ',`LastName`) as `Full Name`, 
City from Customer inner join City on customer.CityID=Cities.CityID;

select CONCAT(`FirstName`,' ',`LastName`) as `Full Name`, company from Customer 
inner join Company on 
customer.companyid=Company.companyid;
