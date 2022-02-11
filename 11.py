import functools

emp_dict =  {
            101:{   'name': 'Anupriya Roy',
                    'depart_id':1,
                    'attendances':[{'date':1, 'hours':[3.5,4.5]},{'date':2, 'hours':[3.2,4.5]},{'date':3, 'hours':[3.2,4.6]},
                                 {'date':4, 'hours':[3.0,4.5]},{'date':5, 'hours':[2.5,4.5]},{'date':6, 'hours':[1.5,4.5]},
                                 {'date':7, 'hours':[2,3]},{'date':8, 'hours':[0,4.5]},{'date':9, 'hours':[2,3.5]},
                                 {'date':10, 'hours':[4,3.5]}],
                    'leaves':[{'date':7, 'no_of_hours':1.5},{'date':7, 'no_of_hours':1.5},{'date':8, 'no_of_hours':3}]
                },
            102:
             {   'name': 'Kadambari Sharma',
                 'depart_id':1,
                 'attendances':[{'date':1, 'hours': [0,4.5]},{'date':2, 'hours':[3.2,0]},{'date':3, 'hours':[3.2,4.6]},
                                {'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},{'date':6, 'hours':[1.5,1]},
                                {'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},{'date':9, 'hours':[2,2]},
                                {'date':10, 'hours':[2,3.5]}],
                 'leaves':[{'date':1, 'no_of_hours':3.5},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':2}]
             },
            103:
            {   'name': 'Abhishek Verma',
                'depart_id':1,
                'attendances':[{'date':3, 'hours':[3.2,4.6]},{'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},
                            {'date':6, 'hours':[1.5,1]},{'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},
                            {'date':9, 'hours':[2,2]},{'date':10, 'hours':[2,3.5]}
                ],
                'leaves':[{'date':1, 'no_of_hours':3},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':3}]
            }
}

emp_list = []
for k, v in emp_dict.items():
    tmp_list_attendance = emp_dict[k]['attendances']
    total_hrs_list_attendance = map(lambda hours: hours['hours'], tmp_list_attendance)
    total_hrs1 = sum(functools.reduce(lambda a, b: a + b, total_hrs_list_attendance))

    tmp_list_leave = emp_dict[k]['leaves']
    total_hrs_list_leave = map(lambda hours: hours['no_of_hours'], tmp_list_leave)
    total_hrs2 = sum(total_hrs_list_leave)

    emp_list.append({'employee_id': k, 'employee_name': emp_dict[k]['name'],
                     'total_attendance_hours': total_hrs1, 'total_leave_days': total_hrs2})

print(emp_list)
