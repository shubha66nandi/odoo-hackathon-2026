CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employee_id VARCHAR(20) UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role VARCHAR(20) DEFAULT 'Employee',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE employees (
    employee_id VARCHAR(20) PRIMARY KEY,
    department VARCHAR(100),
    designation VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    salary NUMERIC,
    profile_image TEXT,
    joining_date DATE
);

CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employee_id VARCHAR(20),
    attendance_date DATE,
    check_in TIME,
    check_out TIME,
    status VARCHAR(20),
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);

CREATE TABLE leave_requests (
    leave_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employee_id VARCHAR(20),
    leave_type VARCHAR(30),
    start_date DATE,
    end_date DATE,
    reason TEXT,
    status VARCHAR(20) DEFAULT 'Pending',
    admin_comment TEXT,
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);

CREATE TABLE payroll (
    payroll_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    employee_id VARCHAR(20),
    month VARCHAR(20),
    basic_salary NUMERIC,
    bonus NUMERIC,
    deduction NUMERIC,
    net_salary NUMERIC,
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);

INSERT INTO users
(employee_id,name,email,password,role)

VALUES
(
'ADMIN001',
'Administrator',
'admin@gmail.com',
'admin123',
'Admin'
);
