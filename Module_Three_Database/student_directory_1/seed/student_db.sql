CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name text,
    cohort_name text
);


INSERT INTO students (student_name, cohort_name) VALUES
('John Doe', 'Cohort A'),
('Jane Smith', 'Cohort B'),
('Bob Johnson', 'Cohort C'),
('Alice Brown', 'Cohort A'),
('Charlie Davis', 'Cohort B'),
('Eva Garcia', 'Cohort C'),
('Frank Miller', 'Cohort A'),
('Grace Taylor', 'Cohort B'),
('Henry White', 'Cohort C'),
('Ivy Robinson', 'Cohort A');