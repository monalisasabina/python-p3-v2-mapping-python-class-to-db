#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

# USING save()
# payroll = Department("Payroll", "Building A, 5th Floor")
# print(payroll)  # <Department None: Payroll, Building A, 5th Floor>

# payroll.save()  # Persist to db, assign object id attribute
# print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

# hr = Department("Human Resources", "Building C, East Wing")
# print(hr)  # <Department None: Human Resources, Building C, East Wing>

# hr.save()  # Persist to db, assign object id attribute
# print(hr)  # <Department 2: Human Resources, Building C, East Wing>


# CREATING
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

engineering= Department.create("Engineering", "Building B, East Wing")
print(engineering) 

animation = Department.create("Animation", "Building E, 2Oth Floor")
print(animation)  

IT = Department.create("IT", "Building A, 1st Floor")
print(IT) 



# UPDATING
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

engineering.name = 'Mech Engineering'
engineering.location = "Building F, 7th Floor"
engineering.update()
print(engineering)  



# DELETING
print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>





ipdb.set_trace()
