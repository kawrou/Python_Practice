CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

-- When a record is deleted (e.g when a row in artists is deleted), 
-- we can configure the database to automatically remove related records 
-- referencing it (e.g delete all related albums), so there are no "orphans" records 
-- - this is done using the on delete cascade SQL option, when creating the table:

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);
