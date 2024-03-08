# students cohorts two tables recipe:

<!-- 1. Extract nouns from the user stories or specification -->
# User Story:
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

# Nouns:
TABLE 1: Students
student_name, cohort_id

TABLE 2: Cohorts
cohort_name, start_date



<!-- 2. Infer the Table Name and Columns -->

---------------------------------------------
|Record  | properties                        |
---------------------------------------------
|Student | student_name,cohort_id           |
---------------------------------------------
|Cohort  | cohort_name, start_date           |
---------------------------------------------


Table 1 name: students
Column names: student_name, cohort_id

Table 2 name: cohorts
Columns names: cohort_name, start_date

<!-- 3. Decide the column types -->

Table 1: students
id: SERIAL
student_name: text
cohort_id: int

Table 2: cohort
id: SERIAL
cohort_name: text
start_date: date

<!-- 5. Relationship -->
Cohorts has many students
Therefore, the foreign key is on the students table. 

<!-- 5. Write the SQL -->

-- file: students_table.sql

CREATE TABLE cohorts(
    id SERIAL PRIMARY KEY, 
    cohort_name text, 
    start_date date, 
)



CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int, 
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

<!-- 5. Create the table -->

`psql -h 127.0.0.1 recipes_directory < recipes.sql`

<!-- (1) make sure to run an INSERT query to insert a new movie record, -->

INSERT INTO movies (recipe_name, cooking_time, rating) VALUES ('Pizzs', 25, 10);

<!-- (2) and then a SELECT query to list the records. -->

SELECT * FROM recipes;
SELECT recipe_name FROM recipes WHERE id = 3;